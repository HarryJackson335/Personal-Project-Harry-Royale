from settings import *

class UI:
    def __init__(self, player, running):
        
        # Basic setup
        self.screen = pygame.display.get_surface()
        self.player = player
        self.font = pygame.font.Font(None, 36)
        self.running = running

        # Padding
        self.left_padding = SCREEN_WIDTH - 50
        self.bottom_padding = SCREEN_HEIGHT - 50
        
        # UI Controls
        self.options = ['attack', 'defend', 'change spells', 'surrender']
        self.current_state = 'start'
        self.general_menu_index = self.attack_menu_index = self.defense_menu_index = {'rows': 0}
        self.rows = 4
        self.attack_option = sample(self.player.attack_spells, 4)
        self.defense_option = sample(self.player.defense_spells, 4)

        self.chosen_spell = None

    def input(self, _):
        keys = pygame.key.get_just_pressed()
        if self.current_state == 'start': # General menu input
            self.general_menu_index['rows'] = (self.general_menu_index['rows'] + int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])) % self.rows
            if keys[pygame.K_SPACE]: self.current_state = self.options[self.general_menu_index['rows']]

        elif self.current_state == 'attack': # Attack menu input
            self.attack_menu_index['rows'] = (self.attack_menu_index['rows'] + int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])) % self.rows
            if keys[pygame.K_SPACE]:
                self.chosen_spell = self.attack_option[self.attack_menu_index['rows']]
                self.current_state = 'start'

        elif self.current_state == 'defend': # Defense menu input
            self.defense_menu_index['rows'] = (self.defense_menu_index['rows'] + int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])) % self.rows
            if keys[pygame.K_SPACE]:
                self.chosen_spell = self.defense_option[self.defense_menu_index['rows']]
                self.current_state = 'start'
        
        elif self.current_state == 'change spells': # Change spells menu input
            self.attack_option = sample(self.player.attack_spells, 4)
            self.defense_option = sample(self.player.defense_spells, 4)
            self.general_menu_index['rows'] = (self.general_menu_index['rows'] + int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])) % self.rows
            if keys[pygame.K_SPACE]: self.current_state = self.options[self.general_menu_index['rows']]

    def menu(self, index, option, _):
        rect = pygame.FRect(0, 0, 400, 300).move_to(bottomright = (self.left_padding, self.bottom_padding))
        pygame.draw.rect(self.screen, COLORS['white'], rect, 0, 10)
        pygame.draw.rect(self.screen, COLORS['black'], rect, 5, 10)

        for i in range(self.rows):
            x = rect.centerx
            y = rect.top + rect.height / (self.rows * 2) + rect.height / self.rows * (self.rows - (self.rows - i))
            color = COLORS['gray'] if i == index['rows'] else COLORS['black']
            
            try:
                text_surf = self.font.render(option[i], True, color)
                text_rect = text_surf.get_frect(center = (x, y))
                self.screen.blit(text_surf, text_rect)
            except Exception as e: print(f"Error rendering menu options: {e}")

    def draw_bar(self, attribute_type, attribute, max_attribute, weak_color, decent_color, energetic_color, padding = 0):
    
        # bg
        rect = pygame.FRect(0, 0, 200, 70).move_to(center = self.player.rect.midright + pygame.Vector2(140, -50) + pygame.Vector2(0, padding))
        pygame.draw.rect(self.screen, COLORS['white'], rect, 0, 4)
        
        # menu
        text_font = pygame.font.Font(None, 26)
        text_surf = text_font.render(attribute_type.capitalize(), True, COLORS['black'])
        text_rect = text_surf.get_frect(topleft = rect.topleft + pygame.Vector2(10, 10))
        self.screen.blit(text_surf, text_rect)
        
        if 0 < attribute < 50: color = weak_color
        elif 50 <= attribute <= 100: color = decent_color
        else: color = energetic_color

        if attribute >= 0:
            bar_rect = pygame.FRect(0,0, 180, 20).move_to(midbottom = rect.midbottom + pygame.Vector2(0, -10))
            pygame.draw.rect(self.screen, COLORS['gray'], bar_rect, 0, 8)
            updated_bar_rect = pygame.FRect(bar_rect.left, bar_rect.top, attribute + (bar_rect.width - max_attribute), bar_rect.height)
            pygame.draw.rect(self.screen, color, updated_bar_rect, 0, 8)
        else: 
            self.running = False
        print(attribute_type, attribute)

    def update(self, dt):
        self.input(dt)
        self.draw(self.screen)

    def draw(self, surface):
        match self.current_state:
            case 'start': self.menu(self.general_menu_index, self.options, 'start')
            case 'attack': self.menu(self.attack_menu_index, self.attack_option, 'attack')
            case 'defend': self.menu(self.defense_menu_index, self.defense_option, 'defend')
            case 'change spells': self.menu(self.general_menu_index, self.options, 'start')
            case 'surrender': return self.current_state
        
        self.draw_bar('health', self.player.health, self.player.max_health, COLORS['red'], COLORS['yellow'], COLORS['green'])
        self.draw_bar('mana', self.player.mana, self.player.max_mana, COLORS['red'], COLORS['green'], COLORS['blue'], 100)


class Opponent_UI:
    def __init__(self, enemy):
        self.screen = pygame.display.get_surface()
        self.enemy = enemy

    def draw_bar(self):
        # bg
        rect = pygame.FRect(0, 0, 200, 70).move_to(center = (200, self.enemy.rect.height))
        pygame.draw.rect(self.screen, COLORS['white'], rect, 0, 4)
        
        # menu
        text_font = pygame.font.Font(None, 26)
        text_surf = text_font.render('Health:', True, COLORS['black'])
        text_rect = text_surf.get_frect(topleft = rect.topleft + pygame.Vector2(10, 10))
        self.screen.blit(text_surf, text_rect)
        

        if self.enemy.health == 0: color = COLORS['gray']
        elif self.enemy.health < 20: color = COLORS['red']
        elif 20 <= self.enemy.health <= 50: color = COLORS['yellow']
        else: color = COLORS['green']
        
        bar_rect = pygame.FRect(0,0, 180, 20).move_to(midbottom = rect.midbottom + pygame.Vector2(0, -10))
        pygame.draw.rect(self.screen, COLORS['gray'], bar_rect, 0, 8)
        updated_bar_rect = pygame.FRect(bar_rect.left, bar_rect.top, self.enemy.health + (bar_rect.width - self.enemy.max_health), bar_rect.height)
        pygame.draw.rect(self.screen, color, updated_bar_rect, 0, 8)