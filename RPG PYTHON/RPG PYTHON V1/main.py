import random
from stat import *
from player import *
from enemy import *
from functions import *

print("* RPG GAME *")
ask_name = input("Name: ").capitalize()
print("--- Choose a Class ---")
while True:
    try:
        ask_class = int(input("1. Warrior\n2. Mage\n (1/2): "))
        if ask_class == 1:
            player1 = Warrior(ask_name)
            print("You are a warrior!")
            break

        elif ask_class == 2:
            player1 = Mage(ask_name)
            print("You are a mage!")
            break

        else:
            print("Invalid choice.")

    except ValueError:
        print("Invalid.")


goblin = Goblin()
orc = Orc()
enemy_list = [goblin, orc]

add_item_set1(player1)

while True:
    enemy = random.choice(enemy_list)

    enemy.reset_stat()

    print(f"** {enemy.name} is in your way! **")
    pause()
    round = 0

    while True:

        print(f"---- ROUND {round +1} ----")
        print()
        player1.check_stat()
        underline()
        enemy.check_stat()
        pause()

        while True:
            print(f"\n{player1.name}'s turn.")
            player1.take_turn()
            underline()
            player_choice = input("What to do : ").upper()

            if player_choice == "1":
                enemy.damage_taken(player1.attack())
                break
            elif player_choice == "2" and isinstance(player1, Mage): ##
                player1.charge()
                break
            elif player_choice == "3" and isinstance(player1, Mage):
                damage = player1.cast_fireball()
                if damage == None:
                    continue
                enemy.damage_taken(damage)
                break
            elif player_choice == "I":
                check_back = player1.open_inv()
                if not check_back:
                    break
            else:
                print("Invalid.")

        if enemy.hp <= 0:
            round_end()
            print("***  You Win!!  ***")
            print(f"{enemy.name} drop...")
            add_random_item(player1)
            add_random_item(player1)
            break

        else:
            print(f"\n{enemy.name}'s turn.")
            pause()
            enemy_action = enemy.take_turn()
            if enemy_action != 0:
                player1.damage_taken(enemy_action)

        round_end()

        if player1.hp <= 0:
            print("***  You Died!  ***")
            break

        round += 1

        