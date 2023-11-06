#!/usr/bin/python3

def multiple_returns(sentence):
    # sent_len = len(sentence)

    if not sentence:
        fisrt_char = None
    else:
        first_char = sentence[0]

    return (len(sentence), first_char)
