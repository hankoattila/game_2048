import new_random_2048


def no_move(my_array, last_my_array):
    if last_my_array != my_array:
        new_random_2048.new_random(my_array)


def move_up(my_array):
    x = 0
    for y in range(4):
        if my_array[x][y] != 0 or my_array[x + 1][y] != 0 or my_array[x + 2][y] != 0 or my_array[x + 3][y] != 0:
            for k in range(4):
                if my_array[x][y] == 0:
                    my_array[x][y] = my_array[x + 1][y]
                    my_array[x + 1][y] = my_array[x + 2][y]
                    my_array[x + 2][y] = my_array[x + 3][y]
                    my_array[x + 3][y] = 0

                if my_array[x + 1][y] == 0:
                    my_array[x + 1][y] = my_array[x + 2][y]
                    my_array[x + 2][y] = my_array[x + 3][y]
                    my_array[x + 3][y] = 0

                if my_array[x + 2][y] == 0:
                    my_array[x + 2][y] = my_array[x + 3][y]
                    my_array[x + 3][y] = 0


def up_addition(my_array):
    x = 0
    count = 0
    for y in range(4):
        if my_array[x][y] == my_array[x + 1][y]:
            count = count + my_array[x][y] * 2
            my_array[x][y] = my_array[x][y] + my_array[x][y]
            my_array[x + 1][y] = my_array[x + 2][y]
            my_array[x + 2][y] = my_array[x + 3][y]
            my_array[x + 3][y] = 0

        if my_array[x + 1][y] == my_array[x + 2][y]:
            count = count + my_array[x + 1][y] * 2
            my_array[x + 1][y] = my_array[x + 1][y] + my_array[x + 1][y]
            my_array[x + 2][y] = my_array[x + 3][y]
            my_array[x + 3][y] = 0

        if my_array[x + 2][y] == my_array[x + 3][y]:
            count = count + my_array[x + 2][y] * 2
            my_array[x + 2][y] = my_array[x + 2][y] + my_array[x + 2][y]
            my_array[x + 3][y] = 0
    return count


def down_move(my_array):
    x = 0
    for y in range(4):
        if my_array[x][y] != 0 or my_array[x + 1][y] != 0 or my_array[x + 2][y] != 0 or my_array[x + 3][y] != 0:
            for k in range(4):
                if my_array[x + 3][y] == 0:
                    my_array[x + 3][y] = my_array[x + 2][y]
                    my_array[x + 2][y] = my_array[x + 1][y]
                    my_array[x + 1][y] = my_array[x][y]
                    my_array[x][y] = 0

                if my_array[x + 2][y] == 0:
                    my_array[x + 2][y] = my_array[x + 1][y]
                    my_array[x + 1][y] = my_array[x][y]
                    my_array[x][y] = 0

                if my_array[x + 1][y] == 0:
                    my_array[x + 1][y] = my_array[x][y]
                    my_array[x][y] = 0


def down_addition(my_array):
    x = 0
    count = 0
    for y in range(4):
        if my_array[x + 3][y] == my_array[x + 2][y]:
            count = count + my_array[x + 3][y] * 2
            my_array[x + 3][y] = my_array[x + 3][y] + my_array[x + 3][y]
            my_array[x + 2][y] = my_array[x + 1][y]
            my_array[x + 1][y] = my_array[x][y]
            my_array[x][y] = 0

        if my_array[x + 2][y] == my_array[x + 3][y]:
            count = count + my_array[x + 2][y] * 2
            my_array[x + 2][y] = my_array[x + 2][y] + my_array[x + 1][y]
            my_array[x + 1][y] = my_array[x][y]
            my_array[x][y] = 0

        if my_array[x + 1][y] == my_array[x + 2][y]:
            count = count + my_array[x + 1][y] * 2
            my_array[x + 1][y] = my_array[x + 1][y] + my_array[x + 1][y]
            my_array[x][y] = 0
    return count


def left_move(my_array):
    y = 0
    for x in range(4):
        if my_array[x][y] != 0 or my_array[x][y + 1] != 0 or my_array[x][y + 2] != 0 or my_array[x][y + 3] != 0:
            for k in range(4):
                if my_array[x][y] == 0:
                    my_array[x][y] = my_array[x][y + 1]
                    my_array[x][y + 1] = my_array[x][y + 2]
                    my_array[x][y + 2] = my_array[x][y + 3]
                    my_array[x][y + 3] = 0

                if my_array[x][y + 1] == 0:
                    my_array[x][y + 1] = my_array[x][y + 2]
                    my_array[x][y + 2] = my_array[x][y + 3]
                    my_array[x][y + 3] = 0

                if my_array[x][y + 2] == 0:
                    my_array[x][y + 2] = my_array[x][y + 3]
                    my_array[x][y + 3] = 0


def left_addition(my_array):
    y = 0
    count = 0
    for x in range(4):
        if my_array[x][y] == my_array[x][y + 1]:
            count = count + my_array[x][y] * 2
            my_array[x][y] = my_array[x][y] + my_array[x][y]
            my_array[x][y + 1] = my_array[x][y + 2]
            my_array[x][y + 2] = my_array[x][y + 3]
            my_array[x][y + 3] = 0

        if my_array[x][y + 1] == my_array[x][y + 2]:
            count = count + my_array[x][y + 1] * 2
            my_array[x][y + 1] = my_array[x][y + 2] + my_array[x][y + 1]
            my_array[x][y + 2] = my_array[x][y + 3]
            my_array[x][y + 3] = 0

        if my_array[x][y + 2] == my_array[x][y + 3]:
            count = count + my_array[x][y + 2] * 2
            my_array[x][y + 2] = my_array[x][y + 3] + my_array[x][y + 2]
            my_array[x][y + 3] = 0
    return count


def right_move(my_array):

    y = 0
    for x in range(4):
        if my_array[x][y] != 0 or my_array[x][y + 1] != 0 or my_array[x][y + 2] != 0 or my_array[x][y + 3] != 0:
            for k in range(4):
                if my_array[x][y + 3] == 0:
                    my_array[x][y + 3] = my_array[x][y + 2]
                    my_array[x][y + 2] = my_array[x][y + 1]
                    my_array[x][y + 1] = my_array[x][y]
                    my_array[x][y] = 0

                if my_array[x][y + 2] == 0:
                    my_array[x][y + 2] = my_array[x][y + 1]
                    my_array[x][y + 1] = my_array[x][y]
                    my_array[x][y] = 0

                if my_array[x][y + 1] == 0:
                    my_array[x][y + 1] = my_array[x][y]
                    my_array[x][y] = 0


def right_addition(my_array):
    y = 0
    count = 0
    for x in range(4):
        if my_array[x][y + 3] == my_array[x][y + 2]:
            count = count + my_array[x][y + 3] * 2
            my_array[x][y + 3] = my_array[x][y + 3] + my_array[x][y + 2]
            my_array[x][y + 2] = my_array[x][y + 1]
            my_array[x][y + 1] = my_array[x][y]
            my_array[x][y] = 0

        if my_array[x][y + 2] == my_array[x][y + 1]:
            count = count + my_array[x][y + 2] * 2
            my_array[x][y + 2] = my_array[x][y + 2] + my_array[x][y + 1]
            my_array[x][y + 1] = my_array[x][y]
            my_array[x][y] = 0

        if my_array[x][y + 1] == my_array[x][y]:
            count = count + my_array[x][y + 1] * 2
            my_array[x][y + 1] = my_array[x][y + 1] + my_array[x][y]
            my_array[x][y] = 0
    return count


def full_map(full_array):
    move_up(full_array)
    up_addition(full_array)
    down_move(full_array)
    down_addition(full_array)
    left_move(full_array)
    left_addition(full_array)
    right_move(full_array)
    right_addition(full_array)
    left_move(full_array)
    left_addition(full_array)
    left_move(full_array)
    left_addition(full_array)
    move_up(full_array)
    up_addition(full_array)
    down_move(full_array)
    down_addition(full_array)
