#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    arg_count = len(sys.argv)

    arg_list = list(sys.argv)

    operators = {"+": add, "-": sub, "/": div, "*": mul}

    if arg_count < 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")

        exit(1)

    a = int(arg_list[1])

    b = int(arg_list[3])

    user_operator = str(arg_list[2])

    if user_operator not in operators.keys():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if user_operator in operators.keys():
        for sign, func in operators.items():
            if user_operator == sign:
                print("{} {} {} = {}".format(a, sign, b, func(a, b)))
