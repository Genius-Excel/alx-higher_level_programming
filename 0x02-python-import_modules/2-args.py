#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_count = len(sys.argv)

    arg_list = list(sys.argv)

    if arg_count == 1:
        print("0 arguments.")

    if arg_count == 2:
        print("{} argument:\n{}: {}".format(1, 1, arg_list[1]))

    if arg_count > 2:
        print("{} arguments:".format(arg_count - 1))  # excluding filename

        for arg in range(1, arg_count):

            print("{}: {}".format(arg, arg_list[arg]))
