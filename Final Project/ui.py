from settings import *

class Common_UI:
    def draw_bar(self, character, attribute_type, attribute, max_attribute, weak_color, decent_color, energetic_color, pos, extra_width = 0, extra_height = 0):
    
        # bg
        self.rect = pygame.FRect(0, 0, 200, 70).move_to(center = (pos + pygame.Vector2(extra_width, extra_height)))
        pygame.draw.rect(self.screen, COLORS['white'], self.rect, 0, 4)
        
        # menu
        text_font = pygame.font.Font(None, 26)
        text_surf = text_font.render(attribute_type.capitalize(), True, COLORS['black'])
        text_rect = text_surf.get_frect(topleft = self.rect.topleft + pygame.Vector2(10, 10))
        self.screen.blit(text_surf, text_rect)
        
        if character == self.player:
            if 0 < attribute < 50: color = weak_color
            elif 50 <= attribute <= 100: color = decent_color
            else: color = energetic_color
        else:
            if attribute == self.enemy.health:
                if self.enemy.health < 20: color = weak_color
                elif 20 <= self.enemy.health <= 50: color = decent_color
                else: color = energetic_color

        if attribute >= 0:
            bar_rect = pygame.FRect(0,0, 180, 20).move_to(midbottom = self.rect.midbottom + pygame.Vector2(0, -10))
            pygame.draw.rect(self.screen, COLORS['gray'], bar_rect, 0, 8)
            updated_bar_rect = pygame.FRect(bar_rect.left, bar_rect.top, attribute + (bar_rect.width - max_attribute), bar_rect.height)
            pygame.draw.rect(self.screen, color, updated_bar_rect, 0, 8)

class UI(Common_UI):
    def __init__(self, player):
        
        # Basic setup
        self.screen = pygame.display.get_surface()
        self.player = player
        self.font = pygame.font.Font(None, 36)
        

        # Padding
        self.left_padding = (SCREEN_WIDTH - 50)
        self.bottom_padding = (SCREEN_HEIGHT - 50)
        
        # UI Controls
        self.options = ['attack', 'defend', 'change spells', 'show spells info']
        self.current_state = 'start'
        self.general_menu_index = self.attack_menu_index = self.defense_menu_index = {'rows': 0}
        self.rows = 4
        self.attack_option = sample(self.player.attack_spells, 4)
        self.defense_option = sample(self.player.defense_spells, 4)

        self.chosen_spell = None

    def input(self, _):
        keys = pygame.key.get_just_pressed()
        if self.current_state == 'start': # General menu input

            # Logic to limit the row index to the value of self.rows
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
        
        if self.current_state != 'change spells':
            if keys[pygame.K_ESCAPE]: self.current_state = 'start'
        
        else:
            self.attack_option = sample(self.player.attack_spells, 4)
            self.defense_option = sample(self.player.defense_spells, 4)
            self.general_menu_index = self.attack_menu_index = self.defense_menu_index = {'rows': 0}
            self.current_state = 'start'

        ''' Explanation of the current state logic

        If state is not current state: the state would be set to start if the escape key is pressed.
        Although if state is current state: we renew the spells and set the value for all three index to 0 and we also set the current state to start
        then draw method is triggered and the attack option is selected.
        then input is triggered and checks for what we are doing inside of the current state and the process keeps repeating.
        '''
        
        '''Explanation of the row index logic
        
        For numbers 0-3 we get the normal index but after 4 we get the remainder as the index.
        
        For negative numbers, we go backwards. For example if the index is -2, we get index 2.
        '''

    def menu(self, index, option, _, extra_width, extra_height):
        rect = pygame.FRect(0, 0, 400, 300).move_to(bottomright = (self.left_padding + extra_width, self.bottom_padding + extra_height))
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

    ''' Explanation of the y-coordinate logic

    y = rect.top + rect.height / (self.rows) + rect.height / self.rows * (self.rows - (self.rows - i))
    This is wrong because the rows will then be spaced unevenly and the whole thing would go down due to wrong spacing between each cell.

    y = rect.top + rect.height / (self.rows * 2) + rect.height / self.rows * (self.rows - (self.rows - i))
    This is the correct one because the whole thing is spaced evenly and all of the options fit in the space because we start at the required position for everything to fit in. 
        
    '''

    def display_spell_info(self, extra_width, extra_height):
        # bg
        rect = pygame.FRect(0, 0, 1000, 700).move_to(center = (SCREEN_WIDTH / 2 + extra_width, SCREEN_HEIGHT / 2 + extra_height))
        pygame.draw.rect(self.screen, COLORS['white'], rect, 0, 4)

        # menu
        for spell_name in SPELLS:
            spell_detail = f'{spell_name}: Damage: {SPELLS[spell_name]['damage']}, Mana Cost: {SPELLS[spell_name]['mana_cost']}'
            x = rect.centerx
            y = rect.top + rect.height / (len(SPELLS) * 2) + rect.height / len(SPELLS) * list(SPELLS).index(spell_name)
            text_surf = self.font.render(spell_detail, True, COLORS['black'])
            text_rect = text_surf.get_frect(center = (x, y))
            self.screen.blit(text_surf, text_rect)

    def draw(self, _, extra_width = 0, extra_height = 0):
        self.extra_width = extra_width
        self.extra_height = extra_height

        match self.current_state:
            case 'start': self.menu(self.general_menu_index, self.options, 'start', self.extra_width, self.extra_height)
            case 'attack': self.menu(self.attack_menu_index, self.attack_option, 'attack', self.extra_width, self.extra_height)
            case 'defend': self.menu(self.defense_menu_index, self.defense_option, 'defend', self.extra_width, self.extra_height)
            case 'change spells': self.menu(self.general_menu_index, self.options, 'start', self.extra_width, self.extra_height)
        
        self.draw_bar(self.player, 'health', self.player.health, self.player.max_health, COLORS['red'], COLORS['yellow'], COLORS['green'], (self.player.rect.midright + pygame.Vector2(140, -50)), self.extra_width, self.extra_height)
        self.draw_bar(self.player, 'mana', self.player.mana, self.player.max_mana, COLORS['red'], COLORS['green'], COLORS['blue'], (self.player.rect.midright + pygame.Vector2(140, 50)), self.extra_width, (self.extra_height + 10 if self.extra_height != 0 else self.extra_height))

        if self.current_state == 'show spells info': self.display_spell_info(self.extra_width, self.extra_height)


class Opponent_UI(Common_UI):
    def __init__(self, enemy, player):
        self.screen = pygame.display.get_surface()
        self.enemy = enemy
        self.player = player