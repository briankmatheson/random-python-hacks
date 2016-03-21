#!/usr/bin/env python

def score():
    import random
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    die3 = random.randint(1,6)
    die4 = random.randint(1,6)
    dielist = [die1, die2, die3, die4]
    dielist = sorted(dielist, reverse=True)
    top, middle, bottom, discarded = dielist
    sum = top+middle+bottom
    return sum

for i in range(6):
    print ("Score", i+1, ": ", score())

