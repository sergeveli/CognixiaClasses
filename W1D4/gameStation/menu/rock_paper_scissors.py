"""Module for playing Rock, Paper, Scissors"""
import random

options = ["rock", "paper", "scissors"]
"""Define the game options"""

def prompt_input(prompt):
    """Define a function to prompt the user for input"""
    return input(prompt).strip()

def play_game():
    """Define a function to play the game""" 
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
    return progress
