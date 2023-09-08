def display_board(board):
    """Displays the current state of the board."""
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")

def play_game():
    """Plays the game of Tic Tac Toe."""
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    player = "X"
    game_over = False
    
    while not game_over:
        display_board(board)
        position = int(input(f"Player {player}, choose a position (1-9): ")) - 1
        
        if board[position] == " ":
            board[position] = player
        else:
            print("That position is already taken. Choose another.")
            continue
        
        if check_win(board, player):
            display_board(board)
            print(f"Player {player} wins!")
            game_over = True
        elif check_tie(board):
            display_board(board)
            print("Tie game.")
            game_over = True
        else:
            player = "O" if player == "X" else "X"
    
    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() == "y":
        play_game()

def check_win(board, player):
    """Checks if the player has won the game."""
    return (board[0] == board[1] == board[2] == player or
            board[3] == board[4] == board[5] == player or
            board[6] == board[7] == board[8] == player or
            board[0] == board[3] == board[6] == player or
            board[1] == board[4] == board[7] == player or
            board[2] == board[5] == board[8] == player or
            board[0] == board[4] == board[8] == player or
            board[2] == board[4] == board[6] == player)

def check_tie(board):
    """Checks if the game is a tie."""
    return " " not in board

play_game()
