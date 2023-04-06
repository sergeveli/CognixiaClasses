import random

# Define the game options
options = ["X", "O"]

# Define a function to prompt the user for input


def prompt_input(prompt):
    return input(prompt).strip()

# Define a function to display the board


def display_board(board):
    print("     |     |")
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}")
    print("_____|_____|_____")
    print("     |     |")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}")
    print("_____|_____|_____")
    print("     |     |")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}")
    print("     |     |")

# Define a function to check if the game is over


def check_game_over(board):
    # Check rows
    for i in range(0, 9, 3):
        if board[i : i + 3] in [["X", "X", "X"], ["O", "O", "O"]]:
            return True
    return next(
        (
            True
            for i in range(3)
            if board[i::3] in [["X", "X", "X"], ["O", "O", "O"]]
        ),
        True
        if board[0] == board[4] == board[8] or board[2] == board[4] == board[6]
        else " " not in board,
    )

# Define a function to play the game


def play_game():
    # Load the game progress from the log file
    progress = {"wins": 0, "losses": 0, "ties": 0}
    # Play the game until the user decides to quit
    while True:
        # Display the current game progress
        print(
            f"Wins: {progress['wins']}, Losses: {progress['losses']}, Ties: {progress['ties']}")
        # Initialize the board
        board = [" "] * 9
        # Choose a random option for the computer
        computer_option = random.choice(options)
        # Prompt the user for input
        user_option = prompt_input("Choose X or O (or q to quit): ")
        if user_option.lower() == "q":
            break
        # Determine the user's option and the computer's option
        if user_option.upper() == "X":
            user_option = "X"
            computer_option = "O"
        else:
            user_option = "O"
            computer_option = "X"
        # Display the board
        display_board(board)
        # Play the game until it is over
        while not check_game_over(board):
            # Prompt the user for input
            user_move = prompt_input(
                "Enter the number of an empty space to make a move (or q to quit): ")
            if user_move.lower() == "q":
                break
            user_move = int(user_move) - 1
            # Make the user's move
            if board[user_move] == " ":
                board[user_move] = user_option
            else:
                print("That space is already taken!")
                continue
            # Check if the game is over
            if check_game_over(board):
                break
            # Make the computer's move
            computer_move = random.choice(
                [i for i, x in enumerate(board) if x == " "])
            board[computer_move] = computer_option
            # Display the board
            display_board(board)
        # Determine the outcome of the game
        if check_game_over(board) and " " not in board:
            print("Tie!")
            progress["ties"] += 1
        elif user_option == board[4] and check_game_over(board):
            print("You win!")
            progress["wins"] += 1
        elif computer_option == board[4] and check_game_over(board):
            print("Computer wins!")
            progress["losses"] += 1
        else:
            print("Invalid game state!")
    # Return the game progress
    return progress
