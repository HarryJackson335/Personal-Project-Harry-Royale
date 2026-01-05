import pygame
from os.path import join
from os import walk
from random import sample, randint, choice

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT= 1280, 720

# Colors
COLORS = {
    'white': '#ffffff',
    'black': '#000000',
    'red': '#ff0000',
    'green': '#00ff00',
    'blue': "#00FFFF",
    'yellow': "#eeff00",
    'gray': 'gray'
}

# Spells
SPELLS = {
    'Expecto Patronum': {'element': 'defense', 'damage': 50, 'mana_cost': 30, 'animation image': 'white light', 'spell_on': 'opponent'},
    'Stupefy': {'element': 'attack', 'damage': 30, 'mana_cost': 20, 'animation image': 'blue bolt', 'spell_on': 'opponent'},
    'Expelliarmus': {'element': 'attack', 'damage': 50, 'mana_cost': 30, 'animation image': 'red bolt', 'spell_on': 'opponent'},
    'Reducto': {'element': 'attack', 'damage': 70, 'mana_cost': 40, 'animation image': 'explosion', 'spell_on': 'opponent'},
    'Avada Kedavra': {'element': 'attack', 'damage': 100, 'mana_cost': 50, 'animation image': 'green bolt', 'spell_on': 'opponent'},
    'Crucio': {'element': 'attack', 'damage': 80, 'mana_cost': 40, 'animation image': 'red bolt', 'spell_on': 'opponent'},
    'Imperio': {'element': 'attack', 'damage': 70, 'mana_cost': 40, 'animation image': 'red bolt', 'spell_on': 'opponent'},
    'Aguamenti': {'element': 'defense', 'damage': 30, 'mana_cost': 20, 'animation image': 'blue bolt', 'spell_on': 'opponent'},
    'Confringo': {'element': 'attack', 'damage': 45, 'mana_cost': 30, 'animation image': 'explosion', 'spell_on': 'opponent'},
    'Petrificus Totalus': {'element': 'attack', 'damage': 40, 'mana_cost': 30, 'animation image': 'blue bolt', 'spell_on': 'opponent'},
    'Protego': {'element': 'defense', 'damage': 4, 'mana_cost': 5, 'animation image': 'shield', 'spell_on': 'player'},
    'Protego Totalum': {'element': 'defense', 'damage': 10, 'mana_cost': 20, 'animation image': 'shield', 'spell_on': 'player'},
}

# Enemy data
CHARACTERS = {
    'dementor': {'health': 100, 'animation image': 'blue bolt'},
    'dragon': {'health': 100, 'animation image': 'blue bolt'},
    'voldemort': {'health': 100},
    'death eater': {'health': 100},
    'player': {
        'health': 150, 
        'mana': 150, 
        'attack_spells': [spell for spell in SPELLS if SPELLS[spell]['element'] == 'attack'], 
        'defense_spells': [spell for spell in SPELLS if SPELLS[spell]['element'] == 'defense'], 
    }
}