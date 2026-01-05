from settings import *
from sprites import *
from timer import Timer
from ui import *
from importer import *


class Game:
    def __init__(self):
        
        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Magical Harry')
        self.info = InfoSprite()
        self.running = True
        self.player_active = False 
   
        # Loading assets and animated sprite logic
        self.load_assets()
        
        # Timers
        self.timers = {
            'Player Turn': Timer(1000, self.enemy_turn, False),  # Timer for player to attack
            'Opponent Turn': Timer(2000, self.player_turn, False), # Timer for enemy to attack
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
        self.opponent_ui = Opponent_UI(self.enemy)

        # Animation setup
        self.animation_assets = import_images('Images', 'Animation')
        for animation in list(self.animation_assets.keys()):
            for spell in SPELLS:
                if animation == SPELLS[spell]['animation image']:
                    try: SPELLS[spell]['animation image'] = self.animation_assets[animation]
                    except Exception as e: print(f'Error for this surface: {e}')

    def handle_ui_input(self):
        if self.ui.chosen_spell != None:    
            self.player_active = False
              
            # Starting the Player Turn timer
            self.timers['Player Turn'].start()

            if SPELLS[self.ui.chosen_spell]['spell_on'] == 'player': self.protect_player()
            else: self.attack_opponent(self.ui.chosen_spell, self.enemy, SPELLS[self.ui.chosen_spell]['animation image'])
            
    def enemy_turn(self):  
        if self.enemy.health > 0:
            if self.enemy.name in ['voldemort', 'death eater']:
                self.enemy_spell = choice(list(SPELLS.keys()))
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
                self.opponent_ui = Opponent_UI(self.enemy)
                self.enemy_turn()
            except IndexError: self.available_enemies = 0
            
    def attack_opponent(self, spell, target, attack):
        self.animated_sprite = AnimatedSprite(spell, target, attack, self.animation_assets)
        self.animated_sprite_destroyer = Timer(1000, self.animated_sprite.kill, True)       
        
        target.health -= SPELLS[spell]['damage'] if target == self.enemy else randint(20, 30)
        self.player.mana -= SPELLS[spell]['mana_cost'] if target == self.enemy else 0        
        self.timers['Opponent Turn'].start()

        # Alternate ways to get the same result with different steps involved for each ... explained in attacking logic explanation 
            # if target == self.player: self.timers['Opponent Turn'].start()
            # if target == self.enemy: self.timers['Opponent Turn'].start()

    ''' Attacking logic explanation
    target: self.player
    enemy attacks player
    the timer starts
    player turn
    target is self.enemy

    target: self.enemy
    player chooses spell
    player attacks enemy
    the timer starts
    enemy turn
    target is self.player

    protecting player
    timer has already started
    destroy health and mana
    enemy turn
    target is self.player
    '''
    
    def player_turn(self): 
        self.ui.chosen_spell = None
        self.player_active = True

    def protect_player(self):  
        self.animated_sprite = AnimatedSprite(self.ui.chosen_spell, self.player, SPELLS[self.ui.chosen_spell]['animation image'], self.animation_assets)       
        self.animated_sprite.destroyer = Timer(1000, self.animated_sprite.kill, True)
        
        self.enemy.health -= randint(1, 6)
        self.player.mana -= SPELLS[self.ui.chosen_spell]['mana_cost']

    def enemy_movement(self, dt):  
        if self.enemy.rect.collidepoint(240, self.enemy.rect.centery): self.enemy.direction = 1
        elif self.enemy.rect.collidepoint(780, self.enemy.rect.centery): self.enemy.direction = -1
        
        if 240 <= self.enemy.rect.centerx <= 780: self.enemy.rect.centerx += self.enemy.direction * self.enemy.speed * dt

    def draw(self):
        self.screen.blit(self.enemy.image, self.enemy.rect) 
        self.screen.blit(self.player.image, self.player.rect)
        try: self.screen.blit(self.animated_sprite.image, self.animated_sprite.rect)
        except AttributeError: pass
        self.opponent_ui.draw_bar()
        self.ui.draw(self.screen)

    def run(self):   
        while self.running: # Main game loop from the tutorial
            dt = self.clock.tick() / 1000  # Converting dt to seconds
            
            for event in pygame.event.get(): # Exit logic
                if event.type == pygame.QUIT: self.running = False

                # if event.type == pygame.FULLSCREEN:
                #     pygame.display.toggle_fullscreen()

            self.screen.blit(self.image_assets['bg'], (0, 0))
            
            # update
            try: 
                self.animated_sprite_destroyer.update()
                self.animated_sprite.update(dt)
            except AttributeError: pass
            
            for timer in self.timers.values(): timer.update()
            self.enemy_movement(dt)                    
            
            if self.player_active:
                self.ui.update(dt)
                self.handle_ui_input()
        
            
            # draw
            if self.running:
                if self.info.next_event == None:
                    self.screen.blit(self.info.surf, self.info.rect)
                    self.screen.blit(self.info.next_surf, self.info.next_rect)
                    if self.info.next_rect.collidepoint(pygame.mouse.get_pos()): 
                        self.info.next_event = 'Next' 
                        self.player_active = True
                        self.draw()
                else: self.draw()


            # Losing section
            try:
                if self.player.health == 0 or self.player.mana == 0:
                    self.player_active = False
                    text_box_surf = pygame.Surface((400, 200))
                    text_box_rect = text_box_surf.get_frect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT /2))

                    self.winner_font = pygame.font.Font(None, 30)
                    self.winner_surf = self.winner_font.render('You lost the battle!', True, COLORS['black'], COLORS['green'])
                    self.winner_rect = self.winner_surf.get_frect(center = text_box_rect.center)
                    self.screen.blit(self.winner_surf, self.winner_rect)
                    self.running = False
            except AttributeError: pass

            # Winning section
            try:
                if self.available_enemies == 0:
                    self.player_active = False
                    text_box_surf = pygame.Surface((400, 200))
                    text_box_rect = text_box_surf.get_frect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT /2))

                    self.winner_font = pygame.font.Font(None, 30)
                    self.winner_surf = self.winner_font.render('You won the battle!', True, COLORS['black'], COLORS['green'])
                    self.winner_rect = self.winner_surf.get_frect(center = text_box_rect.center)
                    self.screen.blit(self.winner_surf, self.winner_rect)
                    self.running = False            
            except AttributeError: pass

            # Surrender section
            if self.ui.current_state == 'surrender':
                self.killed_textbox_surf = pygame.Surface((400, 200))
                self.killed_textbox_rect = self.killed_textbox_surf.get_frect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

                self.killed_font = pygame.font.Font(None, 30)
                self.killed_surf = self.killed_font.render('You died!', True, COLORS['white'], COLORS['green'])
                self.killed_rect = self.killed_surf.get_frect(center = self.killed_textbox_rect.center)
                self.screen.blit(self.killed_surf, self.killed_rect)
                self.running = False

            # update() the display to display everything on screen
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__': # Common Python practice to allow or prevent parts of code from being run when the modules are imported
    game = Game()
    game.run()