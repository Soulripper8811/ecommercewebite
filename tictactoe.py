def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}\n")

def check_winner(board, player):
    # Winning combinations: rows, columns, and diagonals
    winning_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    # Check if any combo matches the current player's marks
    return any(all(board[i] == player for i in combo) for combo in winning_combos)

def is_draw(board):
    # A draw occurs when no empty spaces remain and no winner
    return " " not in board

def tic_tac_toe():
    board = [" "] * 9  # Initialize an empty 3x3 board
    current_player = "X"

    while True:
        print_board(board)

        # Get and validate user input
        try:
            move = int(input(f"Player {current_player}, enter a position (1-9): ")) - 1
        except ValueError:
            print("Please enter a valid number between 1 and 9.")
            continue

        # Check if the move is within range and the cell is empty
        if move < 0 or move >= 9 or board[move] != " ":
            print("Invalid move! The cell is either occupied or out of range. Try again.")
            continue

        # Make the move
        board[move] = current_player

        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a draw
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
