import spells

def challenge_1(health, mana):
    print("In this challenge you are facing the Dark Lord : Lord Voldemort")
    options = ["Run Away", "Fight Him", "Join Him"]
    print(f'Here are your options: {options}')
    choice = input("What will you do: ").title()
    spell_list = spells.Cast_Spell()
    global health_cost
    health_cost = 0
    if choice == "Run Away":
        print("You made the wrong choice, Voldemort caught you and killed you...")
        health_cost = 10
        health -= health_cost
    elif choice == "Join Him":
        print("You have betrayed your fellow wizards and the Aurors succeeded in killing you...")
        health_cost = 20
        health -= health_cost
    elif choice == "Fight Him":
        print("Here are your spells and the mana points they cost")
        print(spell_list)
        spell_cast = input('> ').title()
        if spell_cast in spell_list:
            print(f'You cast {spell_cast}.')
            if spell_cast == "Expelliarmus" or spell_cast == "Stupefy":
                print("You have overpowered Voldemort and won the duel!")
                health_cost = 2
                health += health_cost
            elif spell_cast == "Expecto Patronum" or spell_cast == "Protego":
                print("You protected yourself from Voldemort's killing curse and won the duel!")
                health_cost = 3
                health += health_cost
            else:
                print("Your spell had no effect on Voldemort. He overpowered you and killed you...")
                health_cost = 5
                health -= health_cost
            mana -= spell_list[spell_cast]
        else:
            print('Invalid Choice')
    else:
        print("Not a valid choice.")

    print(f'You have {mana} mana points left and {health} health points left')
    return health, mana
