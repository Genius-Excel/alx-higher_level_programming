#!/usr/bin/python3
def uppercase(str):
    str_result = ""
    for c in str:
        if ord(c) in range(97, 123):
            upper_c = ord(c) - 32
            str_result += chr(upper_c)
        else:
            str_result += c

    print("{}".format(str_result))
