import os


def color(caracter):
    start = "\x1B["
    end = "\x1B[" + "0m"
    if caracter == "0":
        the_color = start + "5;37;47m" + caracter + end
    elif caracter == '2':
        the_color = start + "5;30;41m" + caracter + end
    elif caracter == '4':
        the_color = start + "5;30;42m" + caracter + end
    elif caracter == '8':
        the_color = start + "5;30;43m" + caracter + end
    elif caracter == '16':
        the_color = start + "5;30;44m" + caracter + end
    elif caracter == '32':
        the_color = start + "5;30;45m" + caracter + end
    elif caracter == '64':
        the_color = start + "5;30;46m" + caracter + end
    elif caracter == '128':
        the_color = start + "0;30;41m" + caracter + end
    elif caracter == '256':
        the_color = start + "0;30;42m" + caracter + end
    elif caracter == '512':
        the_color = start + "0;30;43m" + caracter + end
    elif caracter == '1024':
        the_color = start + "0;30;44m" + caracter + end
    elif caracter == '2048':
        the_color = start + "0;30;45m" + caracter + end
    elif caracter == '4096':
        the_color = start + "0;30;46m" + caracter + end
    elif caracter == '16':
        the_color = start + "0;30;47m" + caracter + end
    else:
        the_color = start + "5;30;47m" + caracter + end
    return the_color


def mapp(my_array):
    os.system('clear')
    print(color("┏━━━━━━┳━━━━━━┳━━━━━━┳━━━━━━┓"))
    print(color("┃ ") + color(" " * szam(0, 0, my_array)) + color(str(my_array[0][0])) + color(" ┃ ") + color(" " * szam(0, 1, my_array) + color(str(my_array[0][1]))) + color(
        " ┃ ") + color(" " * szam(0, 2, my_array)) + color(str(my_array[0][2])) + color(" ┃ ") + color(" " * szam(0, 3, my_array)) + color(str(my_array[0][3])) + color(" ┃"))
    print(color("┣━━━━━━╋━━━━━━╋━━━━━━╋━━━━━━┫"))
    print(color("┃ ") + color(" " * szam(1, 0, my_array) + color(str(my_array[1][0]))) + color(" ┃ ") + color(" " * szam(1, 1, my_array)) + color(str(my_array[1][1])) + color(
        " ┃ ") + color(" " * szam(1, 2, my_array)) + color(str(my_array[1][2])) + color(" ┃ ") + color(" " * szam(1, 3, my_array)) + color(str(my_array[1][3])) + color(" ┃"))
    print(color("┣━━━━━━╋━━━━━━╋━━━━━━╋━━━━━━┫"))
    print(color("┃ ") + color(" " * szam(2, 0, my_array) + color(str(my_array[2][0]))) + color(" ┃ ") + color(" " * szam(2, 1, my_array)) + color(str(my_array[2][1])) + color(
        " ┃ ") + color(" " * szam(2, 2, my_array)) + color(str(my_array[2][2])) + color(" ┃ ") + color(" " * szam(2, 3, my_array)) + color(str(my_array[2][3])) + color(" ┃"))
    print(color("┣━━━━━━╋━━━━━━╋━━━━━━╋━━━━━━┫"))
    print(color("┃ ") + color(" " * szam(3, 0, my_array) + color(str(my_array[3][0]))) + color(" ┃ ") + color(" " * szam(3, 1, my_array)) + color(str(my_array[3][1])) + color(
        " ┃ ") + color(" " * szam(3, 2, my_array)) + color(str(my_array[3][2])) + color(" ┃ ") + color(" " * szam(3, 3, my_array)) + color(str(my_array[3][3])) + color(" ┃"))
    print(color("┗━━━━━━┻━━━━━━┻━━━━━━┻━━━━━━┛"))


def szam(x, y, my_array):
    szorzas = (4 - len(str(my_array[x][y])))
    return szorzas
