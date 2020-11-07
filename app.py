import time
import random


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a monster is somewhere around here, "
                "and has captured the princess in the nearby virtual village.")
    print_pause("In front of you is a cave.")
    print_pause("To your right is a dark forrest.")
    print_pause("To the left is an abandoned castle.")


def cave(items):
    print_pause("You picked the cave!")
    print_pause("You enter the cave...")
    if "sword" in items:
        print_pause("In your hand is a wooden sword, "
                    "you can advance to the dark forrest.")
    else:
        print_pause("Here is your sword!")
        items.append("sword")
        print_pause("Continue your adventure!")
        move_player(items)


def forrest(items):
    print_pause("You picked the forrest!")
    print_pause("You enter the forrest...")
    if "shield" in items:
        print_pause("You have a sword and shield.  "
                    "It's time to save the princess!")
    else:
        print_pause("Do you have the sword?")
        if "sword" in items:
            print_pause("You have the sword.  "
                        "Now you have a shield to protect yourself!")
            items.append("shield")
        else:
            print_pause("Go to the cave or you will "
                        "never have a chance against the monster.")
    print_pause("You must go back to the fields to choose again.")
    move_player(items)


def castle(items):
    print_pause("You picked the castle!")
    print_pause("You enter the castle...Are you ready "
                "to fight the monster?")
    if "shield" in items:
        print_pause("You use your shield to fight the monster, "
                    "but do you have a sword.")
        print_pause("But do you have a sword?")
        if "sword" in items:
            print_pause("You have the sword and the shield.  "
                        "You are ready to fight!  You have 3 life pellets "
                        "The monster has 3 life pellets "
                        "Who will win?")
            fight()
        else:
            print_pause("Where is your sword? "
                        "Go to the cave to be prepared to fight the monster!")
            move_player(items)
    else:
        print_pause("How will you defend yourself "
                    "against the monster without a shield? ")
        print_pause("You head back to the forrest.")
        move_player(items)


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

    print_pause("That's not a valid choice.  Please try again.")
    move_player(items)


def game_over():
    print_pause("Would you like to play again?")
    choice = input("1. Yes\n"
                   "2. No\n")
    if choice == "1":
        play_game()
    quit()


def fight():
    player_points = 3
    monster_points = 3
    print_pause("It is you versus the monster!")
    print_pause("Here are the rules. Sword beats the monsters bite.  "
                "Shield beats the monster's fist. "
                "Bite beats the player's shield  "
                "The same rules apply in reverse to the monster. "
                "He will attack at random. Each choice will determine "
                "if you or the monster loses a life pellet.")

    rounds = 6

    while rounds > 0:

        mc = random.choice(["fist", "bite"])
        pc = input("1.  sword\n"
                   "2.  shield\n")

        if mc == "fist" and pc == "1":
            player_points -= 1
            rounds -= 1
            print_pause("The monster fist lowered your points.")

        elif mc == "fist" and pc == "2":
            monster_points -= 1
            rounds -= 1
            print_pause("Your shield lowered the monster's points by one!")

        elif mc == "bite" and pc == "1":
            monster_points -= 1
            rounds -= 1
            print_pause("Your sword lowers the monster's points by one!")

        elif mc == "bite" and pc == "2":
            player_points -= 1
            rounds -= 1
            print_pause("The monster's bite lowered you by one point!")

    if player_points <= 0 or monster_points <= 0:
        if player_points > monster_points:
            print_pause("You won!")
            game_over()
        else:
            print_pause("You lost!")
            game_over()


def play_game():
    items = []
    intro()
    move_player(items)


play_game()
