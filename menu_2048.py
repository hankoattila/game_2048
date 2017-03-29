import file_handler_2048


def start_game():
    load_game_or_not = input("Would you like to load you game? (y/N: ")
    if load_game_or_not == "y" or load_game_or_not == "Y":
        my_array = file_handler_2048.list_import()
    else:
        my_array = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        random_position_list = [0, 1, 2, 3]
        first_column = random.choice(random_position_list)
        first_row = random.choice(random_position_list)
        my_array[first_column][first_row] = 2
    return my_array


def load_game():
    pass


def options():
    pass


def menu_exit():
    pass
