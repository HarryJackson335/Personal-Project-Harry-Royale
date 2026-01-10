import spells

def challenge_4(health, mana):
    print("In this challenge you have been trapped in a room with a locked door that you need to get through.")
    options = ["Open the door", "Shout for help", "Wait and see what happens"]
    print(f'Here are your options: {options}')
    choice = input("What will you do: ").title()
    spell_list = spells.Cast_Spell()
    global health_cost
    health_cost = 0
    if choice == "Shout for help":
        print("The person who trapped you in the room heard your shout and killed you...")
        health_cost = 20
        health -= health_cost
    elif choice == "Wait and see what happens":
        print("No one came to help you and you eventually died of starvation...")
        health_cost = 10
        health -= health_cost
    elif choice == "Open the door".title():
        print("Here are your spells and the mana points they cost")
        print(spell_list)
        spell_cast = input('> ').title()
        if spell_cast in spell_list:
            print(f'You cast {spell_cast}.')
            if spell_cast == "Alohomora":
                print("You escaped the door and got through quietly!")
                health_cost = 3
                health += health_cost
            elif spell_cast == "Reducto" or spell_cast == "Stupefy":
                print("You made a lot of noise and now you need to duel the person who trapped you..")
                health_cost = 5
                health -= health_cost
                if spell_cast == "Stupefy" or spell_cast == "Expelliarmus":
                    print("You have overpowered your opponent and won the duel!")
                    health_cost = 5
                    health += health_cost
                else:
                    print("Your spell had no effect on your opponent. He overpowered you and killed you...")
                    health_cost = 5
                    health -= health_cost
            else:
                print("Your spell had no effect on the door. You are still trapped and eventually died of starvation...")
                health_cost = 10
                health -= health_cost
            mana -= spell_list[spell_cast]
    else:
        print("Not a valid choice.")

    print(f"Current Health: {health}, Current Mana: {mana}")
    return health, mana