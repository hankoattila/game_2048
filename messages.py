def name_prompt():
    username = input("\x1B[1m\nYour name:\x1B[0m ")
    return username


def welcome_message(username):
    print((len("Your name: " + username)) * "-")
    print("\nWelcome, \x1B[1m{}!\x1B[0m\n".format(username))
    return username
    

def set_controls():
    print("\x1B[1m\nPlease set the controls of movement:\x1B[0m")
    up = input("\x1B[1mMove up: \x1B[0m")
    down = input("\x1B[1mMove down: \x1B[0m")
    left = input("\x1B[1mMove left: \x1B[0m")
    right = input("\x1B[1mMove right: \x1B[0m")
    return up, down, left, right


def defined_controls(controls):
    print("\x1B[1m\nControls:\x1B[0m")
    print("Up: [{}] | Down: [{}] | Left: [{}] | Right: [{}]".format(controls[0], controls[1], controls[2], controls[3]))
    print("Press [q] to exit.\n")


def current_player(username):
    username = print("\x1B[1m\nPlayer:\x1B[0m {} |".format(username), end=" ")
    return username

def title():
    print("                      ___   ___  _  _   ___  ")
    print("                     |__ \ / _ \| || | / _ \ ")
    print("                        ) | | | | || || (_) |")
    print("                       / /| | | |__   _> _ < ")
    print("                      / /_| |_| |  | || (_) |")
    print("                     |____|\___/   |_| \___/ ")
    print("                                      by Atti & Alex")
