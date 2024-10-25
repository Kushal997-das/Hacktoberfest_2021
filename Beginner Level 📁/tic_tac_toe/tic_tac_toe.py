def print_board(board):
    """Display the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Check for a winner in the game."""
    # Check rows, columns and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def is_board_full(board):
    """Check if the board is full."""
    for row in board:
        if ' ' in row:
            return False
    return True

def play_game():
    """Main function to play Tic-Tac-Toe."""
    print("Welcome to Tic-Tac-Toe!")
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter the row (0-2): "))
        col = int(input(f"Player {current_player}, enter the column (0-2): "))

        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != ' ':
            print("Invalid move. Please try again.")
            continue

        board[row][col] = current_player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_game()
