from settings import *

class Character(pygame.sprite.Sprite):
    def __init__(self, character_type, pos, extra_width = 0, extra_height = 0): 
        super().__init__()

        self.extra_width = extra_width
        self.extra_height = extra_height
        
        self.pos = pos        
        self.name = self.character_type = character_type
        self.image = CHARACTERS[self.character_type]['image'].convert_alpha()
        self.image = pygame.transform.flip(self.image, True, False) if self.character_type == 'player' else self.image
        self.rect = self.image.get_frect(center = self.pos)

        
        self.attack_spells = CHARACTERS[character_type]['attack_spells'] if character_type == 'player' else None
        self.defense_spells = CHARACTERS[character_type]['defense_spells'] if character_type == 'player' else None
        
        self.mana = self.max_mana = CHARACTERS[character_type]['mana'] if character_type == 'player' else None
        self.health = self.max_health = CHARACTERS[character_type]['health']

        self.direction = -1 if self.name != 'player' else 0
        self.speed = 300

class InfoSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.font = pygame.font.Font(None, 30)
        self.surf = self.font.render(
            '''
                                                                            READ THE GAME INSTRUCTIONS
                Welcome dear participant,

                You are now going to take part in the ultimate battle of wizardry where your skills and strategies are on high stake.
                You have 150 mana points to begin with but be aware that as you cast spells, this value will drop significantly.
                The same applies for your health which is initially going to be 150.
                If you run out of mana or health points, you instantly die.
                To help ease your death, you have the option to change spells and you are not stuck with the same spells.

                A little hint for you to know: the most valuable spells are the ones that cost a lot.

                I would say good luck but I don't think you can stand the four most dangerous beings from the Harry Potter franchise.
            ''',
            True,
            COLORS['white'],
            COLORS['black']
        )

        self.next_surf = self.font.render('PRESS ENTER ->', True, COLORS['white'], COLORS['green'])
        self.next_event = None

        self.rect = self.surf.get_frect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.next_rect = self.next_surf.get_frect(bottomright = (SCREEN_WIDTH - 50, SCREEN_HEIGHT - 50)) 

        
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, spell, character, animation, animation_assets):
        super().__init__()

        self.spell = spell
        self.character = character
        self.animation = animation
        self.animation_assets = animation_assets
        self.pos = self.character.rect.center
        
        self.image = SPELLS[self.spell]['animation image'].convert_alpha()
        self.rect = self.image.get_frect(center = self.pos)

    def update(self):
        self.rect.center = self.character.rect.center + pygame.Vector2(self.character.extra_width, self.character.extra_height)

class TextSprite(pygame.sprite.Sprite):
    def __init__(self, text, font_size, text_color, text_bg_color, size = (400, 200), pos = (SCREEN_WIDTH / 2, SCREEN_HEIGHT /2), extra_width = 0, extra_height = 0):
        super().__init__()
        
        self.extra_width = extra_width
        self.extra_height = extra_height
        self.pos = pos

        textbox = pygame.Surface(size)
        self.textbox_rect = textbox.get_frect(center = self.pos + pygame.Vector2(self.extra_width, self.extra_height))

        font = pygame.font.Font(None, font_size)
        self.surf = font.render(text, True, text_color, text_bg_color)
        self.rect = self.surf.get_frect(center = self.textbox_rect.center)
        self.message = ''
    
    def update(self):
        self.textbox_rect.center = self.pos + pygame.Vector2(self.extra_width, self.extra_height)
        self.rect.center = self.textbox_rect.center