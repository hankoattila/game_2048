import os


#  Function which makes the whole game beatiful by adding colors.
def color(character):
    start = "\x1B["
    end = "\x1B[" + "0m"
    if character == "0":
        the_color = start + "0;30;8m" + character + end
    elif character == '2':
        the_color = start + "0;31;1m" + character + end
    elif character == '4':
        the_color = start + "0;32;1m" + character + end
    elif character == '8':
        the_color = start + "0;33;1m" + character + end
    elif character == '16':
        the_color = start + "0;34;1m" + character + end
    elif character == '32':
        the_color = start + "0;35;1m" + character + end
    elif character == '64':
        the_color = start + "0;36;1m" + character + end
    elif character == '128':
        the_color = start + "0;91;1m" + character + end
    elif character == '256':
        the_color = start + "0;92;1m" + character + end
    elif character == '512':
        the_color = start + "0;93;1m" + character + end
    elif character == '1024':
        the_color = start + "0;94;1m" + character + end
    elif character == '2048':
        the_color = start + "0;95;1m" + character + end
    elif character == '4096':
        the_color = start + "0;96;1m" + character + end
    else:
        the_color = start + "5;30;1m" + character + end
    return the_color


#  Colored skeleton elements of the grid system.
def skeleton():
    top = color("┏━━━━━━┳━━━━━━┳━━━━━━┳━━━━━━┓")
    center = color("┣━━━━━━╋━━━━━━╋━━━━━━╋━━━━━━┫")
    bot = color("┗━━━━━━┻━━━━━━┻━━━━━━┻━━━━━━┛")
    left = color("┃ ")
    mid = color(" ┃ ")
    right = color(" ┃")

    return top, center, bot, left, mid, right


#  Calculates the required number of spaces before values.
def sp(x, y, my_array):
    num_len = len(str(my_array[x][y]))
    space = (4 - num_len)
    return space


#  The main game renderer mechanism.
def mapp(my_array):
    os.system('clear')
    grid = skeleton()

    #  This dictionary stores the amount of spaces calculated.
    spaces = {"00": color(" " * sp(0, 0, my_array)),
              "01": color(" " * sp(0, 1, my_array)),
              "02": color(" " * sp(0, 2, my_array)),
              "03": color(" " * sp(0, 3, my_array)),

              "10": color(" " * sp(1, 0, my_array)),
              "11": color(" " * sp(1, 1, my_array)),
              "12": color(" " * sp(1, 2, my_array)),
              "13": color(" " * sp(1, 3, my_array)),

              "20": color(" " * sp(2, 0, my_array)),
              "21": color(" " * sp(2, 1, my_array)),
              "22": color(" " * sp(2, 2, my_array)),
              "23": color(" " * sp(2, 3, my_array)),

              "30": color(" " * sp(3, 0, my_array)),
              "31": color(" " * sp(3, 1, my_array)),
              "32": color(" " * sp(3, 2, my_array)),
              "33": color(" " * sp(3, 3, my_array))}

    #  This dictionary stores the values and makes them have color.
    values = {"00": color(str(my_array[0][0])),
              "01": color(str(my_array[0][1])),
              "02": color(str(my_array[0][2])),
              "03": color(str(my_array[0][3])),

              "10": color(str(my_array[1][0])),
              "11": color(str(my_array[1][1])),
              "12": color(str(my_array[1][2])),
              "13": color(str(my_array[1][3])),

              "20": color(str(my_array[2][0])),
              "21": color(str(my_array[2][1])),
              "22": color(str(my_array[2][2])),
              "23": color(str(my_array[2][3])),

              "30": color(str(my_array[3][0])),
              "31": color(str(my_array[3][1])),
              "32": color(str(my_array[3][2])),
              "33": color(str(my_array[3][3]))}

    #  Header of the grid
    print(grid[0])

    #  1st row of the grid
    print(grid[3] + spaces["00"] + values["00"] +
          grid[4] + spaces["01"] + values["01"] +
          grid[4] + spaces["02"] + values["02"] +
          grid[4] + spaces["03"] + values["03"] +
          grid[5])

    #  Separator
    print(grid[1])

    #  2nd row of the grid
    print(grid[3] + spaces["10"] + values["10"] +
          grid[4] + spaces["11"] + values["11"] +
          grid[4] + spaces["12"] + values["12"] +
          grid[4] + spaces["13"] + values["13"] +
          grid[5])

    #  Separator
    print(grid[1])

    #  3rd row of the grid
    print(grid[3] + spaces["20"] + values["20"] +
          grid[4] + spaces["21"] + values["21"] +
          grid[4] + spaces["22"] + values["22"] +
          grid[4] + spaces["23"] + values["23"] +
          grid[5])

    #  Separator
    print(grid[1])

    #  4th row of the grid
    print(grid[3] + spaces["30"] + values["30"] +
          grid[4] + spaces["31"] + values["31"] +
          grid[4] + spaces["32"] + values["32"] +
          grid[4] + spaces["33"] + values["33"] +
          grid[5])

    #  Footer of the grid
    print(grid[2])