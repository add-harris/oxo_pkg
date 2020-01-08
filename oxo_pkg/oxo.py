#!/usr/bin/python

from .utils.methods import *
from .models.models import *


def run():

    # Argument Handling

    hard_mode = False
    s_rank = False
    args_list = []
    accepted_arguments = ["--hard", "--s-hard", "--help", "--version"]

    for eachArg in sys.argv[1:]:
        if eachArg in accepted_arguments:
            args_list.append(eachArg)
        else:
            print (eachArg + " is not an accepted argument")
            print_help()

    print_functions(args_list)

    if args_list.__contains__("--s-hard"):
        hard_mode = True
        s_rank = True
        print("*** SUPER-HARD-MODE ACTIVATE ***")
    elif args_list.__contains__("--hard"):
        hard_mode = True
        print("** HARD-MODE ACTIVATE **")

    game = Grid()

    def turn():
        try:
            print(game)
            your_move = input("your move: ").lower()

            if is_input_valid(your_move):

                move_key = input_to_move_key(your_move)

                if is_move_valid(game, move_key):

                    setattr(game, move_key, Move( move_key, "X"))

                    if check_for_win_wrapper(game, "congratulations! %s's win") == True:
                        run()

                    if hard_mode:
                        cpu_move_key = computer_move_hard(game)
                    else:
                        cpu_move_key = computer_move(game)

                    setattr(game, cpu_move_key, Move(cpu_move_key, "O"))
                    print("computer makes a move: " + cpu_move_key)

                    if check_for_win_wrapper(game, "you lose! %s's win") == True:
                        run()

                    turn()
                else:
                    print("move is NOT valid - move %s is already taken" %(your_move))
                    turn()
            else:
                print("invalid input")
                turn()
        except KeyboardInterrupt:
            print(" - program exited")
            print("bye bye!")
            sys.exit()

    if s_rank:
        print("computer makes first move ...")
        cpu_move_key = computer_move_hard(game)
        setattr(game, cpu_move_key, Move(cpu_move_key, "O"))

    turn()


if __name__ == "__main__":
    run()
