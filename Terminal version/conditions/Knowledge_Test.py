def challenge_5(health, mana):
    print("\nIn this final challenge, you must answer a series of knowledge questions to prove your worthiness.")
    questions = {
        "What is the spell to disarm an opponent?": "Expelliarmus",
        "What spell is used to summon objects?": "Accio",
        "What is the incantation for the Patronus Charm?": "Expecto Patronum",
        "Which spell creates water?": "Aguamenti",
        "What spell is used to unlock doors?": "Alohomora",
        "What spell is used to reveal hidden objects or information?": "Revelio",
        "What spell is used to shield against spells?": "Protego",
        "What spell is used to stun an opponent?": "Stupefy",
        "What spell is used to break objects?": "Reducto",
    }
    correct_answers = 0
    for question in questions:
        print(question)
        real_answer = questions[question]
        answer = input('What is the answer to the question: ')
        if answer.lower() == real_answer.lower():
            print("Correct!")
            correct_answers += 1
            health += 5
            mana += 5
        else:
            print(f"Wrong! The correct answer was {answer}.")
            health -= 10
            mana -= 10

    print(f"You answered {correct_answers} out of {len(questions)} questions correctly.")
    print(f"Current Health: {health}, Current Mana: {mana}")
    return health, mana