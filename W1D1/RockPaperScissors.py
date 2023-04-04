# using Python, write a Rock - Paper - Scissors program that accepts the user's input, and make sure that input is either 'r', 'p', or 's'.
# Ask for a second user's input and make sure that input is also only 'r', 'p', or 's.'
# Complete the program to output the results of a rock, paper, scissors game. 

import random

# function to get user input


def get_user_choice():
    user_choice = input(
        "Enter 'r' for rock, 'p' for paper, or 's' for scissors: ")
    while user_choice not in ['r', 'p', 's']:
        print("Invalid input. Please try again.")
        user_choice = input(
            "Enter 'r' for rock, 'p' for paper, or 's' for scissors: ")
    return user_choice

# function to determine winner


def get_winner(player1, player2):
    if player1 == player2:
        return None
    elif (
        player1 == 'r'
        and player2 == 's'
        or player1 == 'p'
        and player2 == 'r'
        or player1 == 's'
        and player2 == 'p'
    ):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

# main function to run the game


def play_game():
    print("Let's play Rock-Paper-Scissors!")
    player1 = get_user_choice()
    player2 = random.choice(['r', 'p', 's'])
    print("Player 2 chose", player2)
    if result := get_winner(player1, player2):
        print(result)
    else:
        print("It's a tie!")


# call the main function to start the game
play_game()
