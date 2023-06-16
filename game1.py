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


class Fight:
    def __init__(self, marios):
        self.marios = marios

    def start_Fight(self):
        print("Fight starts!")
        while len(self.marios) > 1:
            mario1 = random.choice(self.marios)
            mario2 = random.choice(self.marios)
            if mario1 != mario2:
                print(f"{mario1} vs {mario2}")
                while mario1.current_life > 0 and mario2.current_life > 0:
                    mario1.attack(mario2)
                    if mario2.current_life > 0:
                        mario2.attack(mario1)
                if mario1.current_life > 0:
                    print(f"{mario1} wins the fight against {mario2}!")
                    self.marios.remove(mario2)
                else:
                    print(f"{mario2} wins the fight against {mario1}!")
                    self.marios.remove(mario1)
        print(f"{self.marios[0]} is the winner!!!!")


# Create Mario instances
marios = []
marios.append(Mario("Mario", 10))
marios.append(Mario("Luigi", 8))
marios.append(Mario("Bowser", 12))
marios.append(Mario("Princess Peach", 7))
marios.append(Mario("Yoshi", 9))      


# Create a Fight instance and start the fight
Fight = Fight(marios)
Fight.start_Fight()
