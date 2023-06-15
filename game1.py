import random

class Mario:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.max_life = level * 100
        self.current_life = self.max_life


    def attack(self, enemy):
        hurt = random.randint(10, 30) * self.level
        enemy.receive_hurt(hurt)

    def receive_hurt(self, hurt):
        self.current_life -= hurt
        if self.current_life <= 0:
            self.current_life = 0
            print(f"{self.name} has been defeated!")

    def __str__(self):
        return f"{self.name} (Level: {self.level})"