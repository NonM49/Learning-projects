
import random

options = ("rock", "paper", "scissors")
is_running = True
win = 0
lose = 0


while is_running:

    player = None
    computer = random.choice(options)

    while player not in options:
    
        player = input(f"Choose {options}: ").lower()
            
    print("-------------------")
    print(f"You choose      :{player}")
    print(f"Computer choose :{computer}")
    print("-------------------")

    if player == computer:
                print("It's a tie!")
    elif player == options[0] and computer == options[2]:
                print("You win!")
                win += 1
    elif player == options[1] and computer == options[0]:
                print("You win!")
                win += 1
    elif player == options[2] and computer == options[1]:
                print("You win!")
                win += 1
    else:
                print("You loose!")
                lose += 1
    
    play_again = input("Play again? (y/n): ").lower()
    if  play_again != "y":
        break
 
print("--------------------")
print(f"Thanks for playing!\nYou Win {win}, and lost {lose} times.")