from character import Character
from functions import *
from player import Item

class Enemy(Character):
    def __init__(self, name):
        super().__init__(name)

    def check_stat(self):
        print(f"{self.name:<6} | Hp : {self.hp:<3} |")

class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin")
        self.base_hp = 50
        self.base_atk = 8

        self.reset_stat()

    def take_turn(self):
        self.attack()
        pause()
        return self.atk

    def attack(self):
        print(f"{self.name} stabs!")
        big_pause()
        return self.atk
    
class Orc(Enemy):
    def __init__(self):
        super().__init__("Orc")
        self.charge_point = 0
        self.base_hp = 100
        self.base_atk = 12

    def check_stat(self):
        print(f"{self.name:<6} | Hp : {self.hp:<3} | Charged : {self.charge_point:<1}")

    def take_turn(self):
        if self.charge_point == 0:
            self.charging()
            return 0
        elif self.charge_point >= 1:
            return self.slam_attack()

    def charging(self):
        self.charge_point += 1
        print(f"{self.name} is charging")
        big_pause()

    def slam_attack(self):
        self.charge_point -= 1
        print(f"{self.name} use slam attack!")
        pause()
        return self.atk * 2