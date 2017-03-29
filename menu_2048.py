import file_handler_2048
import os
import random


def start_game():
    print("1) Start new game!")
    print("2) Continue the last saved game!")
    load_game_or_not = input("What would you liket to do?\nAnsware: ")
    if load_game_or_not == "2":
        my_array = file_handler_2048.import_list()
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


def menu_exit(my_array):
    os.system('clear')
    input_exit = input("Would you like to save your game? (y/N) ")
    if input_exit == 'y' or input_exit == "Y":
        print("Your game is saved!")
        file_handler_2048.export_list(my_array)
        exit()
    else:
        exit()
