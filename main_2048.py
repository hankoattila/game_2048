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
    count = 0
    messages.title()
    user = messages.welcome_message(messages.name_prompt())
    my_array = menu_2048.start_game()
    if my_array[0].count(2) > 1 or my_array[1].count(2) > 1 or my_array[2].count(2) > 1 or my_array[3].count(2) > 1:
        count = int(file_handler_2048.heigh_score_import("score_of_the_saved_game.csv"))
    controls = messages.set_controls()
    high_score = int(file_handler_2048.heigh_score_import("high_score.csv"))

    while True:
        design_2048.mapp(my_array)
        messages.current_player(user)
        print("\x1B[1mScore:\x1B[0m " + str(count) + " |", end=" ")
        print("\x1B[1mHigh Score:\x1B[0m " + str(high_score))

        messages.defined_controls(controls)

        check_the_free_place_of_the_table = copy.deepcopy(my_array)
        move_2048.full_map(check_the_free_place_of_the_table)
        if my_array == check_the_free_place_of_the_table:
            design_2048.mapp(my_array)
            if count > high_score:
                file_handler_2048.heigh_score_export(count, "high_score.csv")
            break

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
            menu_2048.menu_exit(my_array, high_score, count)
    os.system("clear")
    design_2048.mapp(my_array)
    print("-=Game Over=-")


if __name__ == "__main__":
    main()