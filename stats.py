#!/usr/bin/env python
import random

def score():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    die3 = random.randint(1,6)
    die4 = random.randint(1,6)
    dielist = [die1, die2, die3, die4]
    dielist = sorted(dielist, reverse=True)
    top, middle, bottom, discarded = dielist
    sum = top+middle+bottom
    return sum

def yow():
    lines = [ "Get a mount!",
              "Random DND message!",
              "I will kill you in the face!" ]
    index = random.randint(0, len(lines)-1)
    return lines[index]

for i in range(6):
    this_score = score()
    if this_score == 18:
        print("Score {} :  {} {}".format(i+1, this_score, yow()))
    else:
        print "Score", i+1, ": ", this_score
