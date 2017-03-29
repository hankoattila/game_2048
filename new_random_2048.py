import random


def new_random(my_array):
        z = [0, 1, 2, 3]
        x = random.choice(z)
        y = random.choice(z)
        while my_array[x][y] != 0:
            x = random.choice(z)
            y = random.choice(z)
        my_array[x][y] = 2
