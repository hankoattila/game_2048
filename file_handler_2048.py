import csv


def export_list():
    current_state = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2048, 0]]
    with open("saved_game.csv", "w") as k:
        for i in range(4):
            for x in range(4):
                k.write(str(current_state[i][x]) + ",")


def import_list():
    with open("saved_game.csv", "r") as f:
        import_old_array = f.read()

    array_of_imported_splitted_file = import_old_array.split(",")
    number_of_export_list = 0
    new_table = [[], [], [], []]
    for i in range(len(new_table)):
        for x in range(4):
            new_table[i].append(int(array_of_imported_splitted_file[number_of_export_list]))
            number_of_export_list = number_of_export_list + 1
    return new_table


import_list()