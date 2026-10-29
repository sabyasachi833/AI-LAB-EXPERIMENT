
# Tic-Tac-Toe Game
import sys


# Create an empty board
def create_board():
    return [" "] * 9


# Display the board
def display_board(board):
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


# Check whether a player has won
def check_winner(board, player):
    winning_positions = [
        (0, 1, 2),  # Row 1
        (3, 4, 5),  # Row 2
        (6, 7, 8),  # Row 3
        (0, 3, 6),  # Column 1
        (1, 4, 7),  # Column 2
        (2, 5, 8),  # Column 3
        (0, 4, 8),  # Diagonal 1
        (2, 4, 6)   # Diagonal 2
    ]

    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


# Play the game
def play_game(preset_moves=None):
    board = create_board()
    current_player = "X"
    move_index = 0

    print("Tic-Tac-Toe Board Positions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")

    for turn in range(9):
        display_board(board)
        print(f"Player {current_player}'s turn")

        while True:
            if preset_moves is not None:
                if move_index >= len(preset_moves):
                    print("End of simulated moves.")
                    return

                position = preset_moves[move_index]
                move_index += 1
                print(f"Enter position (1-9): {position}")

            else:
                try:
                    position = int(input("Enter position (1-9): "))
                except (ValueError, EOFError):
                    print("Invalid input or EOF. Exiting game.")
                    return

            if position < 1 or position > 9:
                print("Please enter a number between 1 and 9.")

            elif board[position - 1] != " ":
                print("Position already occupied. Choose another.")

            else:
                break

        board[position - 1] = current_player

        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            return

        current_player = "O" if current_player == "X" else "X"

    display_board(board)
    print("Game Draw!")


# Main Program
if __name__ == "__main__":
    # Demonstration mode
    if "--demo" in sys.argv or not sys.stdin.isatty():
        print("=== Sample Demonstration Match ===")

        # Player X: 1, 4, 7
        # Player O: 2, 5
        sample_moves = [1, 2, 4, 5, 7]

        play_game(preset_moves=sample_moves)

    else:
        play_game()
