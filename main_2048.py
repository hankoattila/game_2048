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

    messages.welcome_message(messages.name_prompt())
    my_array = menu_2048.start_game()
    controls = messages.set_controls()

    count = 0
    while True:
        design_2048.mapp(my_array)
        messages.defined_controls(controls)
        print("Total Number: " + str(count))

        check_the_free_place_of_the_table = copy.deepcopy(my_array)
        move_2048.full_map(check_the_free_place_of_the_table)
        if my_array == check_the_free_place_of_the_table:
            os.system('clear')
            design_2048.mapp(my_array)
            print("\nJatek Vege")

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
            count = count + move_2048.down_addition(my_array)
            move_2048.no_move(my_array, last_my_array)
            design_2048.mapp(my_array)

        if move == controls[2]:
            last_my_array = copy.deepcopy(my_array)
            move_2048.left_move(my_array)
            count = count + move_2048.left_addition(my_array)
            move_2048.no_move(my_array, last_my_array)
            design_2048.mapp(my_array)

        if move == controls[3]:
            last_my_array = copy.deepcopy(my_array)
            move_2048.right_move(my_array)
            count = count + move_2048.right_addition(my_array)
            move_2048.no_move(my_array, last_my_array)
            design_2048.mapp(my_array)
        if move == 'q':
            menu_2048.menu_exit(my_array)


main()
