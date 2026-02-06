from functions import pause

class Character:
    def __init__(self, name):
        self.name = name

        self.base_hp = 100
        self.base_atk = 15

        self.reset_stat()
    
    def reset_stat(self):
        self.hp = self.base_hp
        self.atk = self.base_atk


    def attack(self):
        print(f"{self.name} use slash attack!")
        pause()
        return self.atk
    
    def damage_taken(self, damage_taken):
        print(f"{self.name:<6} | take {damage_taken} damage!")
        self.hp -= damage_taken
        print(f"{self.name:<6} | Hp : {self.hp}")
        pause()
