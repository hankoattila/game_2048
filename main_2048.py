import random
import os
import copy
import move_2048
import design_2048
import new_random_2048

myArray = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
random_position_list = [0, 1, 2, 3]
first_column = random.choice(random_position_list)
first_row = random.choice(random_position_list)
myArray[first_column][first_row] = 2


def main():
    myArray = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    random_position_list = [0, 1, 2, 3]
    first_column = random.choice(random_position_list)
    first_row = random.choice(random_position_list)
    myArray[first_column][first_row] = 2

    up = input("Choose a key from keyboard for move UP: ")
    right = input("Choose a key from keyboard for move RIGHT: ")
    down = input("Choose a key from keyboard for move DOWN: ")
    left = input("Choose a key from keyboard for move LEFT: ")
    count = 0
    while True:
        design_2048.mapp(myArray)
        print(design_2048.color(""))
        print(design_2048.color("Up:") + design_2048.color(up))
        print(design_2048.color("Right:") + design_2048.color(right))
        print(design_2048.color("Down:") + design_2048.color(down))
        print(design_2048.color("Left:") + design_2048.color(left))
        print(design_2048.color("Type q to exit\n"))

        move = input("Give me a direction: ")

        if move == up:
            last_Myarray = copy.deepcopy(myArray)
            move_2048.move_up(myArray)
            count = count + move_2048.up_addition(myArray)
            move_2048.no_move(myArray, last_Myarray)
            design_2048.mapp(myArray)

        if move == down:
            last_Myarray = copy.deepcopy(myArray)
            move_2048.down_move(myArray)
            move_2048.down_addition(myArray)
            move_2048.no_move(myArray, last_Myarray)
            design_2048.mapp(myArray)

        if move == left:
            last_Myarray = copy.deepcopy(myArray)
            move_2048.left_move(myArray)
            move_2048.left_addition(myArray)
            move_2048.no_move(myArray, last_Myarray)
            design_2048.mapp(myArray)

        if move == right:
            last_Myarray = copy.deepcopy(myArray)
            move_2048.right_move(myArray)
            move_2048.right_addition(myArray)
            move_2048.no_move(myArray, last_Myarray)
            design_2048.mapp(myArray)
        if move == 'q':
            os.system('clear')
            input_exit = input("Would you like to save your game? (y/N) ")
            if input_exit == 'y' or input_exit == "Y":
                print("your game is saved")

            else:
                exit()


main()
