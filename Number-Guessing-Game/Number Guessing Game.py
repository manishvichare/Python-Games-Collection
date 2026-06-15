import random
import os

SCORE_FILE = "scorecard.txt"


def save_score(name, attempts):
    with open(SCORE_FILE, "a") as file:
        file.write(f"{name},{attempts}\n")


def show_scorecard():
    if not os.path.exists(SCORE_FILE):
        print("\nNo scores recorded yet.")
        return

    scores = []

    with open(SCORE_FILE, "r") as file:
        for line in file:
            name, attempts = line.strip().split(",")
            scores.append((name, int(attempts)))

    scores.sort(key=lambda x: x[1])

    print("\n========== SCORECARD ==========")
    print("Rank\tName\tAttempts")
    print("-" * 30)

    for rank, (name, attempts) in enumerate(scores, start=1):
        print(f"{rank}\t{name}\t{attempts}")


def play_game():
    print("\n===== NUMBER GUESSING GAME =====")

    player_name = input("Enter your name: ")

    secret_number = random.randint(1, 100)
    attempts = 0

    print("\nI have selected a number between 1 and 100.")
    print("Try to guess it!\n")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            difference = abs(secret_number - guess)

            if guess < secret_number:

                if difference <= 3:
                    print(" Extremely close! Try a slightly higher number.")

                elif difference <= 10:
                    print(" Very close! Go a little higher.")

                elif difference <= 20:
                    print(" Getting closer! Increase your guess.")

                else:
                    print(" Your guess is far below the target.")

            elif guess > secret_number:

                if difference <= 3:
                    print(" Extremely close! Try a slightly lower number.")

                elif difference <= 10:
                    print(" Very close! Go a little lower.")

                elif difference <= 20:
                    print(" Getting closer! Decrease your guess.")

                else:
                    print(" Your guess is far above the target.")

            else:
                print("\n Congratulations!")
                print(f"You guessed the number in {attempts} attempts!")

                save_score(player_name, attempts)
                break

        except ValueError:
            print(" Please enter a valid number.")


def main():
    while True:
        print("\n==============================")
        print("   NUMBER GUESSING GAME")
        print("==============================")
        print("1. Play Game")
        print("2. View Scorecard")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            play_game()

        elif choice == "2":
            show_scorecard()

        elif choice == "3":
            print("\nThank you for playing!")
            break

        else:
            print(" Invalid choice. Please try again.")


if __name__ == "__main__":
    main()