import conditions.Dementors as de
import conditions.Door as do
import conditions.Dragon as dr
import conditions.Knowledge_Test as kt
import conditions.Voldemort as vo
import spells as s
from intro import introduction


def main():
    introduction()
    global health, mana
    health = 30
    mana = 10
    print(f"You start with {health} health points and {mana} mana points.\n")
    health, mana = vo.challenge_1(health, mana)
    if health <= 0 or mana <= 0:
        print("You have lost the game. Better luck next time!")
    else:
        health, mana = de.challenge_2(health, mana)
        if health <= 0 or mana <= s.get_min_mana():
            print("You have lost the game. Better luck next time!")
        else:
            health, mana = dr.challenge_3(health, mana)
            if health <= 0 or mana <= s.get_min_mana():
                print("You have lost the game. Better luck next time!")
            else:
                health, mana = do.challenge_4(health, mana)
                if health <= 0 or mana <= s.get_min_mana():
                    print("You have lost the game. Better luck next time!")
                else:
                    health, mana = kt.challenge_5(health, mana)
                    if health <= 0 or mana <= s.get_min_mana():
                        print("You have lost the game. Better luck next time!")
                    else:
                        print(
                            "Congratulations! You have successfully completed all the challenges and won the game!"
                        )


if __name__ == "__main__":
    main()
