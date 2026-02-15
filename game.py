import random

def show_board(board):
    print(f"\n{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]} \n")

def player_move(board):
    while True:
        move = input("Enter position from 1 to 9: ")
        if not move.isdigit():
            print("Invalid position. Please choose between 1 and 9.")
            continue
        move  = int(move) - 1
        if move <0 or move>8:
            print("Position does not exist.")
        elif board[move] != " ":
            print("Position already taken.")
        else:
            board[move] = "X"
            break

def computer_move(board):
    print("Computer's turn...")
    available = []
    for i in range(9):
        if board[i] == " ":     
            available.append(i)
    move = random.choice(available)
    board[move] = "O"
    
def win_check(board,player):
    if board[0] == player and board[1] == player and board[2] == player:
        return True
    if board[3] == player and board[4] == player and board[5] == player:
        return True
    if board[6] == player and board[7] == player and board[8] == player:
        return True
    
    if board[0] == player and board[3] == player and board[6] == player:
        return True
    if board[1] == player and board[4] == player and board[7] == player:
        return True
    if board[2] == player and board[5] == player and board[8] == player:
        return True
    
    if board[0] == player and board[4] == player and board[8] == player:
        return True
    if board[2] == player and board[4] == player and board[6] == player:
        return True

    return False

def check_draw(board):
    for i in range(9):
        if board[i] == " ":
            return False
    return True

def play_game():
    board = [" "] * 9
    show_board(["1","2","3","4","5","6","7","8","9"])
    print("--------------------------------------")
    print("     Welcome to Tic Tac Toe Game!")
    print("--------------------------------------")
    while True:
        show_board(board)

        player_move(board)
        if win_check(board,"X"):
            show_board(board)
            print("Congrats! You Win.")
            break

        if check_draw(board):
            show_board(board)
            print("Its a draw.")
            break

        computer_move(board)
        if win_check(board,"O"):
            show_board(board)
            print("Computer Win.")
            break

while True:
    play_game()
    again = input("Play again? (y/n): ")
    if again.lower() != "y":
        print("Thanks for playing.")
        break

# Best regards! - Muhammad Ali | Department of Software Engineering 
