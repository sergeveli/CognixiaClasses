import random

# Define the game options
options = ["rock", "paper", "scissors"]

# Define a function to prompt the user for input


def prompt_input(prompt):
    return input(prompt).strip()

# Define a function to play the game


def play_game():
    # Load the game progress from the log file
    progress = {"wins": 0, "losses": 0, "ties": 0}
    # Play the game until the user decides to quit
    while True:
        # Display the current game progress
        print(
            f"Wins: {progress['wins']}, Losses: {progress['losses']}, Ties: {progress['ties']}")
        # Prompt the user for input
        user_choice = prompt_input(
            "Enter rock, paper, or scissors (or q to quit): ")
        if user_choice.lower() == "q":
            break
        # Choose a random option for the computer
        computer_choice = random.choice(options)
        # Determine the winner of the game
        if user_choice.lower() == computer_choice:
            print("Tie!")
            progress["ties"] += 1
        elif user_choice.lower() == "rock" and computer_choice == "scissors":
            print("You win!")
            progress["wins"] += 1
        elif user_choice.lower() == "paper" and computer_choice == "rock":
            print("You win!")
            progress["wins"] += 1
        elif user_choice.lower() == "scissors" and computer_choice == "paper":
            print("You win!")
            progress["wins"] += 1
        else:
            print("Computer wins!")
            progress["losses"] += 1
    # Return the game progress
    return progress
