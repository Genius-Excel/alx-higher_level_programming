#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for item_a in matrix:
        for item_b in item_a:
            print("{}".format(item_b), end=' ')
        print()
