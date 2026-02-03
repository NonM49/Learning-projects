
board = [" "] * 9
def current_board():
    print("", board[0], "|", board[1], "|", board[2], "\n"
      " --+---+--\n",
      board[3], "|", board[4], "|", board[5], "\n"
      " --+---+--\n",
      board[6], "|", board[7], "|", board[8], "\n")
    
def ex_board():
    print("1 | 2 | 3\n"
          "--+---+--\n"
          "4 | 5 | 6\n"
          "--+---+--\n"
          "7 | 8 | 9\n")

print("* TIC TAC TOE *")
print("How to play? :")
print("Choose a position")
ex_board()
while True:
    try:
        ask_start = int(input("Who to start player 1 or 2 (1/2): "))
        if ask_start not in (1,2):
            print("Enter a number 1 or 2.")
        elif ask_start == 1:
            first_player = "Player 1"
            second_player = "Player 2"
            break
        else:
            first_player = "Player 2"
            second_player = "Player 1"
            break
    except ValueError:
        print("Enter a number 1 or 2.")
        continue
round = 0

while True:
    if round % 2 == 0:
        current_player = first_player
        current_xo = "X"
    else:
        current_player = second_player
        current_xo = "O"

    current_board()    
    print(f"{current_player}'s turn ({current_xo})")
    try:
        player_choose = int(input("Enter a number (1-9): ")) -1
        if player_choose not in range(9):
            print("\n* Enter a number between 1 - 9!")
            continue
        elif board[player_choose] != " ":
            print("\n* Cant choose here!")
            continue
        else:
            board[player_choose] = current_xo
    except ValueError:
        print("\n* Enter a number (1-9)!")
        continue

    if (board[0] == board[1] == board[2] != " " or 
        board[3] == board[4] == board[5] != " " or 
        board[6] == board[7] == board[8] != " " or 
        board[0] == board[3] == board[6] != " " or
        board[1] == board[4] == board[7] != " " or
        board[2] == board[5] == board[8] != " " or
        board[0] == board[4] == board[8] != " " or
        board[2] == board[4] == board[6] != " "):
        current_board()
        print(f"* {current_player} Win! *")
        break


    round += 1

    if round >= 9:
        current_board()
        print("\n* Tie! *")
        break
    






