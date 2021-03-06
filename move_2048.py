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
            my_array[x][y] = my_array[x][y] + my_array[x][y]
            my_array[x + 1][y] = my_array[x + 2][y]
            my_array[x + 2][y] = my_array[x + 3][y]
            my_array[x + 3][y] = 0
            count = count + my_array[x][y]

        if my_array[x + 1][y] == my_array[x + 2][y]:
            my_array[x + 1][y] = my_array[x + 1][y] + my_array[x + 1][y]
            my_array[x + 2][y] = my_array[x + 3][y]
            my_array[x + 3][y] = 0
            count = count + my_array[x + 1][y]

        if my_array[x + 2][y] == my_array[x + 3][y]:
            my_array[x + 2][y] = my_array[x + 2][y] + my_array[x + 2][y]
            my_array[x + 3][y] = 0
            count = count + my_array[x + 2][y]
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
            my_array[x + 3][y] = my_array[x + 3][y] + my_array[x + 3][y]
            my_array[x + 2][y] = my_array[x + 1][y]
            my_array[x + 1][y] = my_array[x][y]
            my_array[x][y] = 0
            count = count + my_array[x + 3][y]

        if my_array[x + 2][y] == my_array[x + 3][y]:
            my_array[x + 2][y] = my_array[x + 2][y] + my_array[x + 1][y]
            my_array[x + 1][y] = my_array[x][y]
            my_array[x][y] = 0
            count = count + my_array[x + 2][y]

        if my_array[x + 1][y] == my_array[x + 2][y]:
            my_array[x + 1][y] = my_array[x + 1][y] + my_array[x + 1][y]
            my_array[x][y] = 0
            count = count + my_array[x + 1][y]

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
            my_array[x][y] = my_array[x][y] + my_array[x][y]
            my_array[x][y + 1] = my_array[x][y + 2]
            my_array[x][y + 2] = my_array[x][y + 3]
            my_array[x][y + 3] = 0
            count = count + my_array[x][y]

        if my_array[x][y + 1] == my_array[x][y + 2]:
            my_array[x][y + 1] = my_array[x][y + 2] + my_array[x][y + 1]
            my_array[x][y + 2] = my_array[x][y + 3]
            my_array[x][y + 3] = 0
            count = count + my_array[x][y + 1]

        if my_array[x][y + 2] == my_array[x][y + 3]:
            my_array[x][y + 2] = my_array[x][y + 3] + my_array[x][y + 2]
            my_array[x][y + 3] = 0
            count = count + my_array[x][y + 2]
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
            my_array[x][y + 3] = my_array[x][y + 3] + my_array[x][y + 2]
            my_array[x][y + 2] = my_array[x][y + 1]
            my_array[x][y + 1] = my_array[x][y]
            my_array[x][y] = 0
            count = count + my_array[x][y + 3]

        if my_array[x][y + 2] == my_array[x][y + 1]:
            my_array[x][y + 2] = my_array[x][y + 2] + my_array[x][y + 1]
            my_array[x][y + 1] = my_array[x][y]
            my_array[x][y] = 0
            count = count + my_array[x][y + 2]

        if my_array[x][y + 1] == my_array[x][y]:
            my_array[x][y + 1] = my_array[x][y + 1] + my_array[x][y]
            my_array[x][y] = 0
            count = count + my_array[x][y + 1]

    return count


def full_map(check_the_free_place_of_the_table):
    move_up(check_the_free_place_of_the_table)
    up_addition(check_the_free_place_of_the_table)
    down_move(check_the_free_place_of_the_table)
    down_addition(check_the_free_place_of_the_table)
    left_move(check_the_free_place_of_the_table)
    left_addition(check_the_free_place_of_the_table)
    right_move(check_the_free_place_of_the_table)
    right_addition(check_the_free_place_of_the_table)
    left_move(check_the_free_place_of_the_table)
    left_addition(check_the_free_place_of_the_table)
    left_move(check_the_free_place_of_the_table)
    left_addition(check_the_free_place_of_the_table)
    move_up(check_the_free_place_of_the_table)
    up_addition(check_the_free_place_of_the_table)
    down_move(check_the_free_place_of_the_table)
    down_addition(check_the_free_place_of_the_table)
    move_up(check_the_free_place_of_the_table)
    up_addition(check_the_free_place_of_the_table)
    down_move(check_the_free_place_of_the_table)
    down_addition(check_the_free_place_of_the_table)
    left_move(check_the_free_place_of_the_table)
    left_addition(check_the_free_place_of_the_table)
    right_move(check_the_free_place_of_the_table)
    right_addition(check_the_free_place_of_the_table)
    left_move(check_the_free_place_of_the_table)
    left_addition(check_the_free_place_of_the_table)
    left_move(check_the_free_place_of_the_table)
    left_addition(check_the_free_place_of_the_table)
    move_up(check_the_free_place_of_the_table)
    up_addition(check_the_free_place_of_the_table)
    down_move(check_the_free_place_of_the_table)
    down_addition(check_the_free_place_of_the_table)
