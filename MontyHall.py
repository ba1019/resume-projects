import numpy as np
from random import randint
import matplotlib.pyplot as plt

# Simulation 1 displays the probability in the form of graph when the player can only choose once 
class Simulation1:
    def __init__(self):
        attempts = -1
        while(attempts < 1):
            attempts = GetIntegerInput("How many attempts? ")
        self.attempts = attempts
        self.meanScores = []
        self.count = []

    def Simulate(self):
        for i in range(1, self.attempts):
            scores = []

            for _ in range(1, i):
                scores.append(self.TakeTurn())

            self.meanScores.append(np.mean(scores))
            self.count.append(i)

        self.DisplayResults()

    def TakeTurn(self):
        
        actual = randint(0, 2)
        guess = randint(0, 2)

        
        if actual == guess:
            return 1
        else:
            return 0

    def DisplayResults(self):
        
        plt.plot(self.count, self.meanScores)
        plt.show()


def GetIntegerInput(message):
    while True:
        try:
            print("")
            chance = int(input(message))
        except ValueError:
            print("Enter an integer:")
            continue
        else:
            return chance

# Simulation 2 displays the probability in the form of a graph when the player chooses twice 
class Simulation2(Simulation1):
    def TakeTurn(self):
        
        actual = randint(0, 2)
        guess = randint(0, 2)

        
        newGuesses = [0, 1, 2]
        newGuesses.remove(guess)

        
        if newGuesses[0] == actual:
            del newGuesses[1]
        elif newGuesses[1] == actual:
            del newGuesses[0]
        else:
            del newGuesses[randint(0, len(newGuesses)) - 1]

        
        guess = newGuesses[0]

        if actual == guess:
            return 1
        else:
            return 0


#Mennu options Display and Loops
def Menu():
    print("")
    print("*******Monty Hall Problem********")
    print("(1) Play with only one chance")
    print("(2) Play with 2 chances")
    print("(3) Exit")
   

    
    menuOptions = [1, 2, 3]

    chance = -1
    while(chance not in menuOptions):
        chance = GetIntegerInput("Enter option: ")

    if chance == 1:
        simulation = Simulation1()
    elif chance == 2:
        simulation = Simulation2()
    elif chance == 3:
        exit()

   
    simulation.Simulate()

    Menu()


if __name__ == "__main__":
    Menu()

# As graphs show the option to choose twice is a statstically better probablity than the first one of choosing once