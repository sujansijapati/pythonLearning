
import random

def play_game():
    options = ["r", "p", "s"]
    computer_choice = random.choice(options)
    user_choice = input("Enter your choice (r, p, s): ").lower()

    if user_choice not in options:
        print("Invalid choice. Please try again.")
        return play_game()

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("Draw")
    elif (user_choice == "r" and computer_choice == "s") or \
         (user_choice == "p" and computer_choice == "r") or \
         (user_choice == "s" and computer_choice == "p"):
        print("You win!")
    else:
        print("Computer wins!")

play_game()