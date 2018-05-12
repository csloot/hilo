import random


def main():
    print_header()
    game_loop()


def print_header():
    """

    Writes the introduction of the game to the screen.

    """
    print("Welcome to the HI - LO game")


def print_exit():
    """

    Writes the exit message of the game to the screen.

    :param: null
    :return: null
    """
    print("Thanks for playing, until next time.")


def game_loop():
    number = random.randint(0, 100)

    while True:
        chosen_number = int(input('Guess a number between 0 & 100:'))
        if chosen_number == number:
            print("Got it: The number is {}".format(number))
            print_exit()
            break
        elif chosen_number < number:
            print("Too low!")
        elif chosen_number > number:
            print("Too high!")


if __name__ == '__main__':
    main()
