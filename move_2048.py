import new_random_2048


def no_move(myArray, last_Myarray):
    if last_Myarray != myArray:
        new_random_2048.new_random(myArray)


def move_up(myArray):
    x = 0
    for y in range(4):
        if myArray[x][y] != 0 or myArray[x + 1][y] != 0 or myArray[x + 2][y] != 0 or myArray[x + 3][y] != 0:
            for k in range(4):
                if myArray[x][y] == 0:
                    myArray[x][y] = myArray[x + 1][y]
                    myArray[x + 1][y] = myArray[x + 2][y]
                    myArray[x + 2][y] = myArray[x + 3][y]
                    myArray[x + 3][y] = 0

                if myArray[x + 1][y] == 0:
                    myArray[x + 1][y] = myArray[x + 2][y]
                    myArray[x + 2][y] = myArray[x + 3][y]
                    myArray[x + 3][y] = 0

                if myArray[x + 2][y] == 0:
                    myArray[x + 2][y] = myArray[x + 3][y]
                    myArray[x + 3][y] = 0


def up_addition(myArray):
    x = 0
    count = 0
    for y in range(4):
        if myArray[x][y] == myArray[x + 1][y]:
            count = count + myArray[x][y] * 2
            myArray[x][y] = myArray[x][y] + myArray[x][y]
            myArray[x + 1][y] = myArray[x + 2][y]
            myArray[x + 2][y] = myArray[x + 3][y]
            myArray[x + 3][y] = 0

        if myArray[x + 1][y] == myArray[x + 2][y]:
            count = count + myArray[x + 1][y] * 2
            myArray[x + 1][y] = myArray[x + 1][y] + myArray[x + 1][y]
            myArray[x + 2][y] = myArray[x + 3][y]
            myArray[x + 3][y] = 0

        if myArray[x + 2][y] == myArray[x + 3][y]:
            count = count + myArray[x + 2][y] * 2
            myArray[x + 2][y] = myArray[x + 2][y] + myArray[x + 2][y]
            myArray[x + 3][y] = 0
    return count


def down_move(myArray):
    x = 0
    for y in range(4):
        if myArray[x][y] != 0 or myArray[x + 1][y] != 0 or myArray[x + 2][y] != 0 or myArray[x + 3][y] != 0:
            for k in range(4):
                if myArray[x + 3][y] == 0:
                    myArray[x + 3][y] = myArray[x + 2][y]
                    myArray[x + 2][y] = myArray[x + 1][y]
                    myArray[x + 1][y] = myArray[x][y]
                    myArray[x][y] = 0

                if myArray[x + 2][y] == 0:
                    myArray[x + 2][y] = myArray[x + 1][y]
                    myArray[x + 1][y] = myArray[x][y]
                    myArray[x][y] = 0

                if myArray[x + 1][y] == 0:
                    myArray[x + 1][y] = myArray[x][y]
                    myArray[x][y] = 0


def down_addition(myArray):
    x = 0
    for y in range(4):
        if myArray[x + 3][y] == myArray[x + 2][y]:
            myArray[x + 3][y] = myArray[x + 3][y] + myArray[x + 3][y]
            myArray[x + 2][y] = myArray[x + 1][y]
            myArray[x + 1][y] = myArray[x][y]
            myArray[x][y] = 0

        if myArray[x + 2][y] == myArray[x + 3][y]:
            myArray[x + 2][y] = myArray[x + 2][y] + myArray[x + 1][y]
            myArray[x + 1][y] = myArray[x][y]
            myArray[x][y] = 0

        if myArray[x + 1][y] == myArray[x + 2][y]:
            myArray[x + 1][y] = myArray[x + 1][y] + myArray[x + 1][y]
            myArray[x][y] = 0


def left_move(myArray):
    y = 0
    for x in range(4):
        if myArray[x][y] != 0 or myArray[x][y + 1] != 0 or myArray[x][y + 2] != 0 or myArray[x][y + 3] != 0:
            for k in range(4):
                if myArray[x][y] == 0:
                    myArray[x][y] = myArray[x][y + 1]
                    myArray[x][y + 1] = myArray[x][y + 2]
                    myArray[x][y + 2] = myArray[x][y + 3]
                    myArray[x][y + 3] = 0

                if myArray[x][y + 1] == 0:
                    myArray[x][y + 1] = myArray[x][y + 2]
                    myArray[x][y + 2] = myArray[x][y + 3]
                    myArray[x][y + 3] = 0

                if myArray[x][y + 2] == 0:
                    myArray[x][y + 2] = myArray[x][y + 3]
                    myArray[x][y + 3] = 0


def left_addition(myArray):
    y = 0
    for x in range(4):
        if myArray[x][y] == myArray[x][y + 1]:
            myArray[x][y] = myArray[x][y] + myArray[x][y]
            myArray[x][y + 1] = myArray[x][y + 2]
            myArray[x][y + 2] = myArray[x][y + 3]
            myArray[x][y + 3] = 0

        if myArray[x][y + 1] == myArray[x][y + 2]:
            myArray[x][y + 1] = myArray[x][y + 2] + myArray[x][y + 1]
            myArray[x][y + 2] = myArray[x][y + 3]
            myArray[x][y + 3] = 0

        if myArray[x][y + 2] == myArray[x][y + 3]:
            myArray[x][y + 2] = myArray[x][y + 3] + myArray[x][y + 2]
            myArray[x][y + 3] = 0


def right_move(myArray):

    y = 0
    for x in range(4):
        if myArray[x][y] != 0 or myArray[x][y + 1] != 0 or myArray[x][y + 2] != 0 or myArray[x][y + 3] != 0:
            for k in range(4):
                if myArray[x][y + 3] == 0:
                    myArray[x][y + 3] = myArray[x][y + 2]
                    myArray[x][y + 2] = myArray[x][y + 1]
                    myArray[x][y + 1] = myArray[x][y]
                    myArray[x][y] = 0

                if myArray[x][y + 2] == 0:
                    myArray[x][y + 2] = myArray[x][y + 1]
                    myArray[x][y + 1] = myArray[x][y]
                    myArray[x][y] = 0

                if myArray[x][y + 1] == 0:
                    myArray[x][y + 1] = myArray[x][y]
                    myArray[x][y] = 0


def right_addition(myArray):
    y = 0
    for x in range(4):
        if myArray[x][y + 3] == myArray[x][y + 2]:
            myArray[x][y + 3] = myArray[x][y + 3] + myArray[x][y + 2]
            myArray[x][y + 2] = myArray[x][y + 1]
            myArray[x][y + 1] = myArray[x][y]
            myArray[x][y] = 0

        if myArray[x][y + 2] == myArray[x][y + 1]:
            myArray[x][y + 2] = myArray[x][y + 2] + myArray[x][y + 1]
            myArray[x][y + 1] = myArray[x][y]
            myArray[x][y] = 0

        if myArray[x][y + 1] == myArray[x][y]:
            myArray[x][y + 1] = myArray[x][y + 1] + myArray[x][y]
            myArray[x][y] = 0
