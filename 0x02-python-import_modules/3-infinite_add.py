#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_count = len(sys.argv)

    arg_list = list(sys.argv)

    sum_result = 0

    if arg_count == 1:
        pass

    for arg in range(1, arg_count):
        arg_val = int(arg_list[arg])

        sum_result += arg_val

    print("{}".format(sum_result))
