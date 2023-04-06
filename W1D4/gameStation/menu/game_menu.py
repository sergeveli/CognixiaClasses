"""Module providingFunction printing python version."""

import os
import json
import rock_paper_scissors
import tic_tac_toe

# Define the path for the log file
LOG_FILE = "game_progress.json"

# Load the game progress from the log file
if os.path.exists(LOG_FILE):
    with open(LOG_FILE, "r", encoding="UTF-8") as log_file:
        game_progress = json.load(log_file)
else:
    game_progress = {}

# Define the menu options
menu_options = {
    "1": "Rock Paper Scissors",
    "2": "Tic Tac Toe",
    "3": "Exit"
}

# Define a function to display the menu


def display_menu():
    """Define a function to display the menu"""
    print("Welcome to the game menu!")
    print("Please select a game to play:")
    for key, value in menu_options.items():
        print(f"{key}. {value}")

# Define a function to prompt the user for input


def prompt_input(prompt):
    return input(prompt).strip()

# Define a function to save the game progress to the log file


def save_progress(game_name, progress):
    game_progress[game_name] = progress
    with open(LOG_FILE, "w", encoding="UTF-8") as log_file2:
        json.dump(game_progress, log_file2)

# Define the main function


def main():
    while True:
        display_menu()
        choice = prompt_input("Enter your choice: ")
        if choice == "1":
            print("Starting Rock Paper Scissors...")
            progress = rock_paper_scissors.play_game()
            save_progress("rock_paper_scissors", progress)
        elif choice == "2":
            print("Starting Tic Tac Toe...")
            progress = tic_tac_toe.play_game()
            save_progress("tic_tac_toe", progress)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
