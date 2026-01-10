import spells

def challenge_3(health, mana):
    print("In this challenge you are facing the mighty dragon : Hungarian Horntail")
    options = ["Run Away", "Fight It", "Tame It"]
    print(f'Here are your options: {options}')
    choice = input("What will you do: ").title()
    spell_list = spells.Cast_Spell()
    global health_cost
    health_cost = 0
    if choice == "Run Away":
        print("You made the wrong choice, the dragon caught you and burned you to ashes...")
        health_cost = 10
        health-= health_cost
    elif choice == "Tame It":
        print("You have tried to tame the dragon but it overpowered you and burned you to ashes...")
        health_cost = 20
        health -= health_cost
    elif choice == "Fight It":
        print("Here are your spells and the mana points they cost")
        print(spell_list)
        spell_cast = input('> ').title()
        if spell_cast in spell_list:
            print(f'You cast {spell_cast}.')
            if spell_cast == "Stupefy":
                print("You have successfully stunned the dragon and won the duel!")
                health_cost = 3
                health += health_cost
            elif spell_cast == "Aguamenti" or spell_cast == "Protego":
                print("You protected yourself from the dragon's fire and won the duel!")
                health_cost = 2
                health += health_cost
            else:
                print("Your spell had no effect on the dragon. It overpowered you and burned you to ashes...")
                health_cost = 20
                health -= health_cost
            mana -= spell_list[spell_cast]
    else:
        print("Not a valid choice.")

    print(f"Current Health: {health}, Current Mana: {mana}")
    return health, mana