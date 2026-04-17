from character import Character
from functions import *
import random

class Player(Character):
    def __init__(self, name):
        super().__init__(name)
        self.inventory = []

    def check_stat(self):
        print(f"{self.name:<6} | Hp : {self.hp:<3} |")

    def take_turn(self):
        print(f"1.slash attack  (atk : {self.atk})\n")
        print("'I' to open Inventory")

    def open_inv(self):
        print("\n--- INVENTORY ---")
        if not self.inventory:
            print("Inventory is empty.")
        
        for i, item in enumerate(self.inventory): ##
            print(f"{i + 1}. {item.name}")
        underline()
        choice = input("Use item? (B to go back): ").upper()

        if choice == "B":
            return True
            
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(self.inventory):
                item = self.inventory.pop(idx)
                item.use(self)
            else:
                print("Invalid choice.")
                return True
        else:
            print("Invalid.")
            return True

    def add_item(self, item):
        self.inventory.append(item)

class Warrior(Player):
    pass

class Mage(Player):
    def __init__(self, name):
        self.base_mp = 10
        super().__init__(name)
        self.base_hp = 70
        self.base_atk = 10

        self.reset_stat()
    
    def reset_stat(self):
        super().reset_stat()
        self.mp = self.base_mp

    def check_stat(self):
        print(f"{self.name:<6} | Hp : {self.hp:<3} | Mp : {self.mp:<3}")

    def take_turn(self):
        print(f"1.basic attack  (atk : {self.atk})\n"
               "2.charge        (mp + 20)\n"
               "3.cast fireball (mp cost: 25)(35 damage)\n"
               "'I' to open Inventory")
        
    def charge(self):
        self.mp += 20
        print("+ 20 mp ")
        pause()

    def cast_fireball(self):
        if self.mp < 25:
            print("Not enough Mp!")
            pause()
            return None
        
        print(f"Mp : {self.mp} - 25")
        self.mp -= 25
        print("fireball casted!")
        pause()
        return 35


class Item():
    def __init__(self, name, effect, value):
        self.name = name
        self.effect = effect
        self.value = value

    def use(self, target):
        if self.effect == "heal":
            target.hp += self.value
            print(f"{target.name} : healed {self.value} hp!")
        
        elif self.effect == "buff":
            target.atk += self.value
            print(f"{target.name} : atk + {self.value}!")

def add_item_set1(target):
    target.add_item(heal_potion)
    target.add_item(strength_potion)
    pause()
    print(f"+ 1 {heal_potion.name}")
    pause()
    print(f"+ 1 {strength_potion.name}")
    pause()

def add_random_item(target):
    ran_item = random.choice(item_list)
    target.add_item(ran_item)
    pause()
    print(f"+ 1 {ran_item.name}")

heal_potion = Item("heal potion", "heal", 30)
strength_potion = Item("strength potion", "buff", 10)

item_list = [heal_potion, strength_potion]
