#!/usr/bin/python3

def multiple_returns(sentence):
    sent_len = len(sentence)

    fisrt_char = None

    if not sentence:
        pass
    else:
        first_char = sentence[0]

    return (sent_len, first_char)
