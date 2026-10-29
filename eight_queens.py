
N = 8

# Initialize the chessboard
board = [["." for _ in range(N)] for _ in range(N)]


# Function to check if placing a Queen is safe
def is_safe(row, col):
    """
    Check if placing a Queen at board[row][col] is safe.
    1. Same column above
    2. Upper-left diagonal
    3. Upper-right diagonal
    """

    # Check column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < N:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


# Function to solve the N-Queens problem
def solve_queens(row):
    """
    Backtracking solver for N-Queens problem.
    """

    if row == N:
        return True

    for col in range(N):
        if is_safe(row, col):
            board[row][col] = "Q"

            if solve_queens(row + 1):
                return True

            # Backtrack
            board[row][col] = "."

    return False


# Main Program
if __name__ == "__main__":
    print(f"Solving {N}-Queens Problem using Backtracking...")
    print()

    if solve_queens(0):
        print(f"Solution for {N}-Queens Problem:")
        print("-" * (N * 2 + 1))

        for row in board:
            print(" " + " ".join(row))

        print("-" * (N * 2 + 1))
    else:
        print("No solution exists")
