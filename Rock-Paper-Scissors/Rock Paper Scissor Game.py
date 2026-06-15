
import random

def rock_paper_scissor(system, user):
    if user == system:
        return "tie"
    elif (user == "R" and system == "S"):
        return "win"
    elif (user == "P" and system == "R"):
        return "win"
    elif (user == "S" and system == "P"):
        return "win"
    else:
        return "lose"


play_game = True  

while play_game:

    user_score = 0
    system_score = 0
    tie_score = 0

    while True:
        user = input("Enter Your Choice (Rock(R), Paper(P), Scissor(S), Quit(Q)): ").upper()

        if user == "Q":
            print("\nFinal Score")
            print(f"You: {user_score} | System: {system_score} | Tie: {tie_score}")
            break

        if user not in ["R", "P", "S"]:
            print("Invalid Input")
            continue

        system = random.choice(["R", "P", "S"])
        print("System Choice:", system)

        result = rock_paper_scissor(system, user)

        if result == "win":
            user_score += 1
            print("You Win")
        elif result == "lose":
            system_score += 1
            print("You Lose")
        else:
            tie_score += 1
            print("Match Tie")

        print(f"Live Score| You: {user_score} | System: {system_score} | Tie: {tie_score}")
        print("-" * 40)

    
    choice = input("\nPlay again? (Y/N): ").upper()
    if choice != "Y":
        print("Game Ended ")
        play_game = False

