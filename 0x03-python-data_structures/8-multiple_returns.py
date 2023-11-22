#!/usr/bin/python3
def multiple_returns(sentence):
    ln = len(sentence)
    if (ln == 0):
        tup = 0, None
    else:
        tup = len(sentence), sentence[0]
    return (tup)
