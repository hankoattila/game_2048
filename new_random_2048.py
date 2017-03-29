import random


def new_random(myArray):
        z = [0, 1, 2, 3]
        x = random.choice(z)
        y = random.choice(z)
        while myArray[x][y] != 0:
            x = random.choice(z)
            y = random.choice(z)
            myArray[x][y]
        myArray[x][y] = 2
