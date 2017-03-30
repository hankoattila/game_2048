def name_prompt():
    username = input("\nYour name: ")
    return username


def welcome_message(username):
    print((len("Your name: " + username)) * "-")
    print("\nWelcome, {}!\n".format(username))


def set_controls():
    print("\nPlease set the controls of movement:")
    up = input("Move up: ")
    down = input("Move down: ")
    left = input("Move left: ")
    right = input("Move right: ")
    return up, down, left, right


def defined_controls(controls):
    print("\nControls:")
    print("Up: [{}] | Down: [{}] | Left: [{}] | Right: [{}]".format(controls[0], controls[1], controls[2], controls[3]))
    print("Press [q] to exit.\n")
