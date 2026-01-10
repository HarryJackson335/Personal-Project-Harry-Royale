from settings import *
from sprites import *
from timer import Timer
from ui import *
from importer import *


class Game:
    def __init__(self):
        
        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Harry Royale')
        self.running = True
        self.player_active = False

        self.info = InfoSprite()

        # Loading assets and animated sprite logic
        self.load_assets()
        
        # Timers
        self.timers = {
            'Player Turn': Timer(2000, self.enemy_turn, False),
            'Opponent Turn': Timer(2000, self.player_turn, False),
            'destroy_textbox': Timer(2000, self.endgame, False),
            'warning_destructor' : Timer(2000, auto_start= False),
            'animated_sprite_destroyer': Timer(1000, auto_start= False) 
            }        
        
    def load_assets(self):
       
        # Character images
        self.image_assets = import_images('Images')
        for name in self.image_assets: 
            if name in CHARACTERS: CHARACTERS[name]['image'] = self.image_assets[name]

        # Player setup
        try: self.player = Character('player', (250, SCREEN_HEIGHT - 180))
        except TypeError as e: print(f"Error: {e}")
        except AttributeError as e: print(f"Error: {e}")
        
        # Opponent setup
        try: self.enemy = Character(*(sample(list(CHARACTERS.keys())[0:-1], 1)), (SCREEN_WIDTH / 2, 300)) # Exclude 'Player' from enemies
        except TypeError as e: print(f"Error: {e}")
        except AttributeError as e: print(f"Error: {e}")
        
        # UI Setup
        self.ui = UI(self.player)
        self.opponent_ui = Opponent_UI(self.enemy, self.player)

        # Animation setup
        self.animation_assets = import_images('Images', 'Animation')
        for animation in list(self.animation_assets.keys()):
            for spell in SPELLS:
                if animation == SPELLS[spell]['animation image']:
                    try: SPELLS[spell]['animation image'] = self.animation_assets[animation]
                    except Exception as e: print(f'Error for this surface: {e}')

        # Audio setup
        self.audio_assets = audio_loader('Audio')
        self.audio_assets['game music'].set_volume(100)

    def handle_ui_input(self):
        if self.ui.chosen_spell != None:    
            self.player_active = False
            
            if self.player.mana >= SPELLS[self.ui.chosen_spell]['mana_cost']:
                if SPELLS[self.ui.chosen_spell]['spell_on'] == 'player': self.protect_player()
                else: self.attack_opponent(self.ui.chosen_spell, self.enemy, SPELLS[self.ui.chosen_spell]['animation image'])
                
                # Starting the Player Turn timer
                self.timers['Player Turn'].start()
            
            else:
                self.warning = TextSprite('Not enough mana! Choose another spell', 30, COLORS['white'], COLORS['green'], extra_width= self.extra_width, extra_height= self.extra_height)
                self.player_turn()
            
    def enemy_turn(self):
        if self.enemy.health > 0:
            if self.enemy.name in ['voldemort', 'death eater']:
                self.enemy_spell = choice([spell for spell in SPELLS if SPELLS[spell]['element'] == 'attack'])
                self.attack_opponent(self.enemy_spell, self.player, SPELLS[self.enemy_spell]['animation image']) 
            else:
                self.enemy_attack = self.animation_assets['blue bolt']
                possible_spells = [spell for spell in SPELLS if SPELLS[spell]['animation image'] == self.animation_assets['blue bolt']]
                self.attack_opponent(possible_spells[randint(0, len(possible_spells) - 1)], self.player, self.enemy_attack)
        
        else:  
            CHARACTERS[self.enemy.name]['health'] = 0
            self.available_enemies = [enemy for enemy in list(CHARACTERS.keys())[0:-1] if enemy != self.enemy.name and CHARACTERS[enemy]['health'] > 0]
            
            try: 
                self.enemy = Character(choice(self.available_enemies), (SCREEN_WIDTH / 2, 300))
                self.opponent_ui = Opponent_UI(self.enemy, self.player)
                self.enemy_turn()
            except IndexError: self.available_enemies = 0
            
    def attack_opponent(self, spell, target, attack):
        self.animated_sprite = AnimatedSprite(spell, target, attack, self.animation_assets)
        self.timers['animated_sprite_destroyer'].start() 
        
        if target == self.enemy:
            target.health -= SPELLS[spell]['damage']
            self.player.mana -= SPELLS[spell]['mana_cost']
       
        else: 
            target.health -= SPELLS[spell]['damage']
            self.timers['Opponent Turn'].start()
    
    def player_turn(self):
        self.ui.chosen_spell = None
        self.player_active = True

    def protect_player(self):
        self.animated_sprite = AnimatedSprite(self.ui.chosen_spell, self.player, SPELLS[self.ui.chosen_spell]['animation image'], self.animation_assets)       
        self.animated_sprite.destroyer = Timer(1000, self.animated_sprite.kill, True)
        
        self.enemy.health -= randint(1, 6)
        self.player.mana -= SPELLS[self.ui.chosen_spell]['mana_cost']

    ''' Attacking logic explanation
    player turn
    target is enemy
    choose a spell
    
    check for mana validation and destroy health and mana
        and then timer starts
        and then enemy turn
        and then target is player
    
    else display the warning message
        player turn
        target is enemy

    enemy turn
    target is player
    health is destroyed
    timer starts
    player turn

    protecting player
    creating and destroying sprite
    destroying health and mana
    timer starts
    enemy turn

    '''

    def enemy_movement(self, dt):  
        if (SCREEN_WIDTH, SCREEN_HEIGHT) <= pygame.display.get_window_size() and self.info.next_event == 'Next':
            if self.enemy.rect.collidepoint(240, self.enemy.rect.centery): self.enemy.direction = 1
            elif self.enemy.rect.collidepoint(780, self.enemy.rect.centery): self.enemy.direction = -1
            
            if 240 <= self.enemy.rect.centerx <= 780: self.enemy.rect.centerx += self.enemy.direction * self.enemy.speed * dt
            else:
                text_box = TextSprite('Too much user interference', 30, COLORS['black'], COLORS['green'], extra_width= self.extra_width, extra_height= self.extra_height)
                self.screen.blit(text_box.surf, text_box.rect)
                self.player_active = False
                self.running = False
        
        else: self.enemy.rect.centerx += 0

    def check_ending(self):
        # Losing section
        try:
            if self.player.health <= 0 or self.player.mana < min([SPELLS[spell]['mana_cost'] for spell in SPELLS]):
                self.player_active = False
                self.text_box = TextSprite('You lost the battle!', 30, COLORS['black'], COLORS['green'], extra_width = self.extra_width, extra_height = self.extra_height)
                self.screen.blit(self.text_box.surf, self.text_box.rect)
                self.text_box.message = 'Endgame'
                self.destroy_textbox = Timer(2000, self.endgame, True)
        except AttributeError: pass

        # Winning section
        try:
            if self.available_enemies == 0:
                self.player_active = False
                self.text_box = TextSprite('You won the battle!', 30, COLORS['black'], COLORS['green'], extra_width = self.extra_width, extra_height = self.extra_height)
                self.screen.blit(self.text_box.surf, self.text_box.rect)
                self.text_box.message = 'Endgame'
                self.destroy_textbox = Timer(2000, self.endgame, True)
        except AttributeError: pass

    def endgame(self):
        self.running = False

    def handle_game_info(self):
        self.screen.blit(self.info.surf, self.info.rect)
        self.screen.blit(self.info.next_surf, self.info.next_rect)
        keys = pygame.key.get_just_pressed()
        if keys[pygame.K_RETURN]: 
            self.info.next_event = 'Next' 
            self.player_active = True
            try: self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
            except: print('Error')
            self.audio_assets['game music'].play(loops = -1)

    def draw(self):
        self.screen.blit(self.image_assets['bg'], (0, 0) + pygame.Vector2(self.extra_width, self.extra_height))
        self.screen.blit(self.enemy.image, self.enemy.rect.center + pygame.Vector2(self.enemy.extra_width if self.extra_width != 0 else 0, self.enemy.extra_height if self.extra_height != 0 else 0)) if self.extra_width != 0 and self.extra_height != 0 else self.screen.blit(self.enemy.image, self.enemy.rect)
        self.screen.blit(self.player.image, self.player.rect.center + pygame.Vector2(self.player.extra_width if self.extra_width != 0 else 0, self.player.extra_height if self.extra_height != 0 else 0)) if self.extra_width != 0 and self.extra_height != 0 else self.screen.blit(self.player.image, self.player.rect)
        
        try: 
            self.animated_sprite.update()
            if self.animated_sprite.character == self.player: self.screen.blit(self.animated_sprite.image, self.animated_sprite.rect.topleft + pygame.Vector2(self.extra_width - 20 if self.extra_width != 0 else 0, self.extra_height + 100 if self.extra_height != 0 else 0))
            else: self.screen.blit(self.animated_sprite.image, self.animated_sprite.rect.topleft + pygame.Vector2(self.extra_width - 45 if self.extra_width != 0 else 0, self.extra_height + 40 if self.extra_height != 0 else 0))
        except AttributeError: pass
        
        self.opponent_ui.draw_bar(self.enemy, 'health', self.enemy.health, self.enemy.max_health, COLORS['red'], COLORS['yellow'], COLORS['green'], (200, self.enemy.rect.height) + pygame.Vector2(self.extra_width, self.extra_height))
        self.ui.draw(self.screen, self.extra_width, self.extra_height)
        
        try: 
            if self.warning.message == '' and not self.warning_destructor:
                self.screen.blit(self.warning.surf, self.warning.rect)
                self.warning.message = 'Displayed'
                self.timers['warning_destructor'].start()
        
        except AttributeError: pass

    def handle_window_resizing(self):
        if (SCREEN_WIDTH, SCREEN_HEIGHT) > pygame.display.get_window_size() or (SCREEN_WIDTH, SCREEN_HEIGHT) < pygame.display.get_window_size() != (1536, 841):
            if not self.timers['destroy_textbox']:
                self.message = TextSprite('The window needs to be in default size or fullscreen to play', 30, COLORS['black'], COLORS['white'])
                self.timers['destroy_textbox'].start()
                self.screen.blit(self.message.surf, self.message.rect)
            
        else:
            self.UPDATED_SCREEN_WIDTH, self.UPDATED_SCREEN_HEIGHT = pygame.display.get_window_size()
            self.extra_width = (self.UPDATED_SCREEN_WIDTH - SCREEN_WIDTH) / 2
            self.extra_height = (self.UPDATED_SCREEN_HEIGHT - SCREEN_HEIGHT) / 2                
            self.player.extra_width, self.player.extra_height = (self.extra_width - 150 if self.extra_width != 0 else 0), -(self.extra_height + 40 if self.extra_height != 0 else 0)
            self.enemy.extra_width, self.enemy.extra_height = (self.extra_width if self.extra_width != 0 else 0, -(self.extra_height) if self.extra_height != 0 else 0)
            self.draw()

    def run(self):
        while self.running: # Main game loop from the tutorial
            dt = self.clock.tick() / 1000  # Converting dt to seconds  

            for event in pygame.event.get(): # Exit logic
                if event.type == pygame.QUIT: self.endgame()

            
            # update and draw
            if self.info.next_event == None: self.handle_game_info()
            else:
                for timer in self.timers.values(): timer.update()
                self.handle_window_resizing()
                self.enemy_movement(dt)
                if self.player_active:
                    self.ui.input(dt)
                    self.handle_ui_input()

            # ending
            self.check_ending()

            # update() the display to display everything on screen
            pygame.display.update()

        pygame.quit()
        
if __name__ == '__main__': # Common Python practice to allow or prevent parts of code from being run when the modules are imported
    game = Game()
    game.run() 