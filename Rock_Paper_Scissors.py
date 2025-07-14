import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid input! Please choose rock, paper, or scissors.")

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("Welcome to the Rock-Paper-Scissors Game!")

    while True:
        print(f"\n--- Round {round_number} ---")
        
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)

        if winner == "tie":
            print("Result: It's a tie!")
        elif winner == "user":
            print("Result: You win this round!")
            user_score += 1
        else:
            print("Result: Computer wins this round!")
            computer_score += 1

        print(f"Score → You: {user_score} | Computer: {computer_score}")


        while True:
            play_again = input("Do you want to play another round? (yes/no): ").lower()
            if play_again in ["yes", "y"]:
                round_number += 1
                break  
            elif play_again in ["no", "n"]:
                print("\nThanks for playing! ")
                print(f"Final Score → You: {user_score} | Computer: {computer_score}")
                return 
            else:
                print("Invalid input. Please type 'yes' or 'no'.")

play_game()
