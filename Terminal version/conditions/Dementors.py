import spells
def challenge_2(health, mana):
    print("\nIn this challenge you encounter a group of Dementors. They are trying to suck out your soul.")
    options = ["Run Away","Fight Them"]
    print(f'Here are your options: {options}')
    choice = input("> ").title()
    spell_list = spells.Cast_Spell()
    if choice == 'Run Away':
        print("You try to run away but the Dementors catch you and suck your soul.")
        health -= 10
    elif choice == "Fight Them":
        print("Here are your spells and the mana points they cost")
        print(spell_list)
        spell_cast = input('> ').title()
        if spell_cast in spell_list:
            print(f'You cast {spell_cast}.')
            if spell_cast == "Expecto Patronum":
                print("You have successfully driven away the Dementors with your Patronus!")
                health += 5
            elif spell_cast == "Stupefy":
                print("You have stunned the Dementors temporarily, but they will recover soon.")
                health -= 2
            elif spell_cast == "Protego":
                print("You have protected yourself from the Dementors, but they are still around.")
                health -= 3
            else:
                print("Your spell had no effect on the Dementors. They overpowered you and sucked your soul.")
                health -= 10
            mana -= spell_list[spell_cast]

    else:
        print("Invalid choice. You lose 5 health for hesitation.")
        health -= 5

    print(f"Current Health: {health}, Current Mana: {mana}")
    return health, mana