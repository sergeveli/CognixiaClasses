# expand this Rock, Paper, Scissors game. Prompt the user to ask them if they want to play again. 
# Repeat the game until the user decides to quit. Keep track of the wins for Players 1 and 2 and the Draws. 
# Give the option to play a game to best of 5.

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
        return "draw"
    elif (
        player1 == 'r'
        and player2 == 's'
        or player1 == 'p'
        and player2 == 'r'
        or player1 == 's'
        and player2 == 'p'
    ):
        return "Player 1 wins"
    else:
        return "Player 2 wins"

# main function to run the game


def play_game():
    print("Let's play Rock-Paper-Scissors!")
    player1_wins = 0
    player2_wins = 0
    draws = 0
    rounds_played = 0
    best_of_five = False
    if input("Would you like to play a best of 5 game? (y/n): ").lower() == 'y':
        best_of_five = True
        print("Best of 5 game selected.")
    # loop to play rounds until one player has won 3 rounds (in a regular game) or a best of 5 game is completed
    while not best_of_five or (player1_wins < 3 and player2_wins < 3):
        print(f"Round {rounds_played+1}")
        player1 = get_user_choice()
        # randomly select Player 2's choice
        player2 = random.choice(['r', 'p', 's'])
        print(f"Player 2 chose {player2}")
        # determine the winner of the round
        result = get_winner(player1, player2)
        if result == "draw":
            print("It's a draw!")
            draws += 1
        elif result == "Player 1 wins":
            print("Player 1 wins!")
            player1_wins += 1
        else:
            print("Player 2 wins!")
            player2_wins += 1
        rounds_played += 1
        print(
            f"Current score: Player 1 - {player1_wins}, Player 2 - {player2_wins}, Draws - {draws}\n")
        # if playing a best of 5 game and one player has won 3 rounds
        if best_of_five and (player1_wins == 3 or player2_wins == 3):
            if player1_wins > player2_wins:
                print("Player 1 wins the best of 5 game!")
            else:
                print("Player 2 wins the best of 5 game!")


# main loop to run the game
while True:
    play_game()  # call the play_game function
    play_again = input("Would you like to play again? (y/n): ")
    if play_again.lower() != 'y':  # if the user doesn't want to play again, exit the loop
        break
