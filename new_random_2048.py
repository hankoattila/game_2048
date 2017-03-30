import random


def new_random(my_array):
    z = [0, 1, 2, 3]
    x = random.choice(z)
    y = random.choice(z)
    while my_array[x][y] != 0:
        x = random.choice(z)
        y = random.choice(z)
    two_or_four = random.choice(list(range(100)))
    if two_or_four > 80:
        my_array[x][y] = 4
    else:
        my_array[x][y] = 2
