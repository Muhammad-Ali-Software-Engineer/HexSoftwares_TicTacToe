import random

# ---------- BOARD DISPLAY ----------
def show_board(board):
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

# ---------- PLAYER MOVE ----------
def player_move(board):
    while True:
        move = input("Enter position (1-9): ")

        if not move.isdigit():
            print("Invalid input. Enter number 1-9.")
            continue

        move = int(move) - 1

        if move < 0 or move > 8:
            print("Position out of range.")
        elif board[move] != " ":
            print("Position already taken.")
        else:
            board[move] = "X"
            break

# ---------- COMPUTER MOVE ----------
def computer_move(board):
    print("Computer's turn...")

    available = [] 

    for i in range(9):
        if board[i] == " ":
            available.append(i)

    move = random.choice(available)
    board[move] = "O"

# ---------- WIN CHECK ----------

    # win_conditions = [
    #     [0,1,2], [3,4,5], [6,7,8],  # rows
    #     [0,3,6], [1,4,7], [2,5,8],  # columns
    #     [0,4,8], [2,4,6]            # diagonals
    # ]

def check_win(board, player):

    # Rows
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    if board[3] == player and board[4] == player and board[5] == player:
        return True
    if board[6] == player and board[7] == player and board[8] == player:
        return True

    # Columns
    if board[0] == player and board[3] == player and board[6] == player:
        return True
    if board[1] == player and board[4] == player and board[7] == player:
        return True
    if board[2] == player and board[5] == player and board[8] == player:
        return True

    # Diagonals
    if board[0] == player and board[4] == player and board[8] == player:
        return True
    if board[2] == player and board[4] == player and board[6] == player:
        return True

    return False

# ---------- DRAW CHECK ----------
def check_draw(board):
    for i in range(9):
        if board[i] == " ":
            return False
    return True  

# ---------- MAIN GAME ----------
def play_game():
    board = [" "] * 9

    print("Welcome to Tic-Tac-Toe!")
    show_board(["1","2","3","4","5","6","7","8","9"])

    while True:
        show_board(board)

        player_move(board)
        if check_win(board, "X"):
            show_board(board)
            print("Congrats! You Win.")
            break

        if check_draw(board):
            show_board(board)
            print("It's a Draw!")
            break

        computer_move(board)
        if check_win(board, "O"):
            show_board(board)
            print("Computer Wins!")
            break


# ---------- REPLAY LOOP ----------
while True:
    play_game()

    again = input("Play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing!")
        break
