

def user_pick_rule(current_list, num_list, current_num):
    while True:
        ran = input("How many time you like to enter? (1 - 3) : ")
        if not ran.isdigit():
            print("Invalid")
            continue

        ran = int(ran)

        if 1 <= ran <= 3 :
            current_list += num_list[current_num : current_num + ran]
            current_num += ran
            return current_num
        else:
            print("Invalid, Enter a number between 1 and 3")
            continue

def player_turn(turns, player_start, player_second):
    if turns %2 == 0:
        current = player_start
    else:
        current = player_second
    return current

def decor_text():
    print("*************************************")

player_start = ""
player_second = ""
player_current = ""

while True:
    decor_text()
    print("DON'T COUNT NUMBER 21 GAME")
    decor_text()
    player1_name = input("Player1 name : ")
    player2_name = input("Player2 name : ")
    decor_text()
    
    ask_start = int(input(f"Who to start? \n""Player 1 or 2 (1/2): "))
    decor_text()

    if ask_start == 1:
        player_start = player1_name
        player_second = player2_name
    elif ask_start == 2:
        player_start = player2_name
        player_second = player1_name
    else:
        print("Invalid")

    num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    current_list = []
    current_num = 0
    turns = 0

    while True:

        player_current = player_turn(turns, player_start, player_second)
        print(f"\n{player_current}'s turn!")
        turns += 1
        current_num = user_pick_rule(current_list, num_list, current_num)
        decor_text()
        print(current_list)

        if current_num >= 21:
            decor_text()
            print(f"\n{player_current} counted 21!")
            winner = player_turn(turns, player_start, player_second)
            print(f"{winner} is the winner!!\n")
            decor_text()
            current_list.clear()
            break

    while True:
        play_again = input("Play again? (y/n) : ").lower()
        if play_again == "y":
            print("Play again ....")
            break
        elif play_again == "n":
            quit()
        else:
            print("Invalid")