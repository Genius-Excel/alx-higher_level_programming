#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a_pair = tuple_a + (0, 0)

    tuple_b_pair = tuple_b + (0, 0)

    tuple_sum_a = (tuple_a_pair[0] + tuple_b_pair[0])

    tuple_sum_b = (tuple_a_pair[1] + tuple_b_pair[1])

    tuple_result = (tuple_sum_a, tuple_sum_b)

    return (tuple_result)
