"""TicTacToe"""

BOARD = {1: ' ',  2: ' ',  3: ' ',
         4: ' ',  5: ' ',  6: ' ',
         7: ' ',  8: ' ',  9: ' '}


def render():
    """Returns a str describing the board in current state"""
    return f''' {BOARD[1]} | {BOARD[2]} | {BOARD[3]}
---+---+---
 {BOARD[4]} | {BOARD[5]} | {BOARD[6]} 
---+---+---
 {BOARD[7]} | {BOARD[8]} | {BOARD[9]} '''


def get_action(player):
    """Prompts user for number 1-9"""
    while True:
        try:
            action = int(
                input(f"{player}'s turn, choose a number between 1-9: "))
        except ValueError:
            print("Invalid input, please enter a number between 1-9.")
            continue

        if action < 1 or action > 9:
            print("Invalid input, please enter a number between 1-9.")
            continue

        if BOARD[action] != ' ':
            print("This space is already taken. Please choose another.")
            continue

        return action


def victory_message(player):
    """Prints updated board and victory message for winner"""
    print(render())
    return f"{player} wins!"


def check_win(player):
    """Checks victory conditions"""
    win_conditions = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7]
    ]

    return any(
        BOARD[condition[0]]
        == BOARD[condition[1]]
        == BOARD[condition[2]]
        == player
        for condition in win_conditions
    )


def play_t3():
    """Main function"""
    #progress = {"wins": 0, "losses": 0, "ties": 0}
    player = 'X'
    game_round = 0
    game_over = False

    while not game_over:
        print(render())

        action = get_action(player)
        BOARD[action] = player

        game_round += 1

        if game_round >= 4 and check_win(player):
            print(victory_message(player))
            game_over = True
            #progress["wins"] += 1
            break

        if game_round == 9:
            print("It's a tie!")
            game_over = True
            break

        player = 'O' if player == 'X' else 'X'

    restart = input("Do you want to play again? (y/n): ")
    if restart.lower() == 'y':
        for key in BOARD.keys():
            BOARD[key] = ' '
        play_t3()

if __name__ == '__main__':
    play_t3()
