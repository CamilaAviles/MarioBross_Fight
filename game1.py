import random

class Mario: # mario class is created
    def __init__(self, name, level):
        self.name = name # each character has name
        self.level = level # each character has a level
        self.max_life = level * 100 # each character has max life
        self.current_life = self.max_life # each character has current life 


    def attack(self, enemy): # enemy to be attacked
        hurt = random.randint(10, 30) * self.level # The amount of damage inflicted on the enemy is calculated by multiplying a random number between 10 and 30 by the current character level.
        enemy.receive_hurt(hurt) # enemy will receive the damage

    def receive_hurt(self, hurt):
        self.current_life -= hurt # The damage is reduced from the character's current life. 
        if self.current_life <= 0: # If the character's current life is equal to or less than zero
            self.current_life = 0 # it is set to zero 
            print(f"{self.name} has been defeated!") # to indicate that the character has been defeated. 

    def __str__(self): # a string object representation is returned
        return f"{self.name} (Level: {self.level})" # a string is returned which contains the name and level of the current character in the form "name (Level: level)".


class Fight: # fight class is created
    def __init__(self, marios): # marios object is assigned
        self.marios = marios

    def start_Fight(self):
        print("Fight starts!")
        while len(self.marios) > 1: # two variables are assigned, mario 1, mario2, where in each iteration two characters are chosen randomly
            mario1 = random.choice(self.marios)
            mario2 = random.choice(self.marios)
            if mario1 != mario2: # if mario1 is different from mario2, then:
                print(f"{mario1} vs {mario2}")
                while mario1.current_life > 0 and mario2.current_life > 0: # as long as both mario1 and mario2 have current life greater than zero:
                    mario1.attack(mario2) # mario1 attacks mario2 in each iteration with the attack function
                    if mario2.current_life > 0: # but if mario2 is still alive...
                        mario2.attack(mario1) # now it is him who attacks mario1
                if mario1.current_life > 0: # it is verified which of the two marios has current life to know who has been the winner 
                    print(f"{mario1} wins the fight against {mario2}!")
                    self.marios.remove(mario2) # The losing character is removed from the marios list using the remove method.
                else:
                    print(f"{mario2} wins the fight against {mario1}!")
                    self.marios.remove(mario1) # The losing character is removed from the marios list using the remove method.
        print(f"{self.marios[0]} is the winner!!!!") # the last character on the list is shown, who will be the winner. 


# Create Mario instances
marios = [] # a list with marios is created, where the characters with their name and level are added using an append.
marios.append(Mario("Mario", 10))
marios.append(Mario("Luigi", 8))
marios.append(Mario("Bowser", 12))
marios.append(Mario("Princess Peach", 7))
marios.append(Mario("Yoshi", 9))      


# Create a Fight instance and start the fight
Fight = Fight(marios) # fight between marios
Fight.start_Fight() # the fight between the characters is started and printed 
