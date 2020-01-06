import sys
import random

from ..models.models import *
from ..resources.data import *

from ..text import text


# Methods

def is_input_valid(input):
    if input in possible_input:
        return True
    else:
        return False

def input_to_move_key(input):
    return moves_map.get(input)

def get_available_move_keys(game):
    return_list = []
    for key in all_move_keys:
        move = getattr(game, key)
        if move.value == "-":
            return_list.append(key)
    return return_list

def is_move_valid(game, move_key):
    all_available_move_keys = get_available_move_keys(game)
    if move_key in all_available_move_keys:
        return True
    else:
        return False

def computer_move(game):
    all_available_move_keys = get_available_move_keys(game)
    random_index = random.randint(0, len(all_available_move_keys)-1)
    cpu_move_key = all_available_move_keys[random_index]
    return cpu_move_key

def check_for_win(game):
    for win_set in possible_wins:
        values = list(map(lambda position: getattr(game, position).value, win_set))
        if values.count("X") == 3 or values.count("O") == 3:
            return Win( True, values[0])
    return Win( False, "-")

def check_for_win_wrapper(game, string):
    win = check_for_win(game)
    if win.win == True:
        print (game)
        print (string %(win.value))
        return play_again()
    elif len(get_available_move_keys(game)) == 0:
        print (game)
        print ("oh ho, its a draw")
        return play_again()
    else:
        return False

def play_again():
    print ("would you like to play again?")
    replay = input(": ").lower()
    if replay in no_answers:
        print("bye bye!")
        sys.exit()
    elif replay in yes_answers:
        return True
    else:
        print ("not a valid input")
        print ("enter no or press Ctrl + C to exit")
        return play_again()

def computer_move_hard(game):

    winning_move = watch_for_win(game)
    if winning_move != None:
        print("computer: I win!!")
        return winning_move

    blocking_move = watch_for_win(game, "X")
    if blocking_move != None:
        print("computer: Not so fast!!")
        return blocking_move

    all_available_move_keys = get_available_move_keys(game)

    corner_move = play_the_corners(game, all_available_move_keys)
    if corner_move != None:
        return corner_move
    else:
        return all_available_move_keys[0]

def play_the_corners(game, move_list):
    available_conrers = list(filter(lambda move: move in move_list, corner_moves))
    if len(available_conrers) > 0:
        return available_conrers[0]
    else:
        return None

def watch_for_win(game, player = "O"):
    for win_set in possible_wins:
        moves = list(map(lambda position: getattr(game, position), win_set))
        values = list(map(lambda move: move.value, moves))
        if values.count(player) == 2 and values.count("-") == 1:
            winning_move = list(filter(lambda move: move.value == "-", moves)).pop().position
            return winning_move
    return None

# Non Functional Methods

def print_functions(args):
    if args.__contains__("--help"):
        print("showing help options")
        print_help()

    if args.__contains__("--version"):
        print_version()

    if args.__contains__("--license"):
        print_license()

    if args.__contains__("--readme"):
        print_readme()

def print_help():
    print(text.help_text)
    sys.exit()

def print_version():
    print(text.version_text)
    sys.exit()

def print_license():
    print(text.license_txt)
    sys.exit()

def print_readme():
    print(text.readme)
    sys.exit()
