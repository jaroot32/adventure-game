import time

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)

def intro():
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a monster is somewhere around here, and has been terrifying the nearby virtual village.")
    print_pause("In front of you is a cave.")
    print_pause("To your right is a dark forrest.")
    print_pause("To the left is an abandoned castle.")
    print_pause("In your hand is a wooden sword.")


def move_player(items):
    print_pause("Please enter the number for "
    "the direction you would like to go:")
    direction = input("1.  The cave\n"
                    "2.  The forrest\n"
                    "3.  The castle\n")
    if direction == "1":
        cave(items)
    elif direction == "2":
        forrest(items)
    elif direction == "3":
        castle(items)                        

def play_game():
    items = []
    intro()
    move_player(items)

play_game()