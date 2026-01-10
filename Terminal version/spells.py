def Cast_Spell():
    global spell_list
    spell_list = {
        "Expelliarmus": 5,
        "Expecto Patronum": 4,
        "Alohomora": 3,
        "Reducto": 5,
        "Accio": 3,
        "Aguamenti": 4,
        "Protego": 4,
        "Stupefy": 5,
        "Revelio": 3
    }
    return spell_list

def get_min_mana():
    minimum_mana = min(spell_list.values())
    return minimum_mana

if __name__ == '__main__':
    Cast_Spell()
