import random
import os
import copy
import move_2048
import design_2048
import menu_2048
import new_random_2048
import messages
import file_handler_2048


def main():
    my_array = menu_2048.start_game()

    messages.welcome_message(messages.name_prompt())
    controls = messages.set_controls()

    count = 0
    while True:
        design_2048.mapp(my_array)
        messages.defined_controls(controls)
        move = input("Command: ")

        if move == controls[0]:
            last_my_array = copy.deepcopy(my_array)
            move_2048.move_up(my_array)
            count = count + move_2048.up_addition(my_array)
            move_2048.no_move(my_array, last_my_array)
            design_2048.mapp(my_array)

        if move == controls[1]:
            last_my_array = copy.deepcopy(my_array)
            move_2048.down_move(my_array)
            move_2048.down_addition(my_array)
            move_2048.no_move(my_array, last_my_array)
            design_2048.mapp(my_array)

        if move == controls[2]:
            last_my_array = copy.deepcopy(my_array)
            move_2048.left_move(my_array)
            move_2048.left_addition(my_array)
            move_2048.no_move(my_array, last_my_array)
            design_2048.mapp(my_array)

        if move == controls[3]:
            last_my_array = copy.deepcopy(my_array)
            move_2048.right_move(my_array)
            move_2048.right_addition(my_array)
            move_2048.no_move(my_array, last_my_array)
            design_2048.mapp(my_array)
        if move == 'q':
            os.system('clear')
            input_exit = input("Would you like to save your game? (y/N) ")
            if input_exit == 'y' or input_exit == "Y":
                print("Your game is saved!")
                exit()
            else:
                exit()


main()
