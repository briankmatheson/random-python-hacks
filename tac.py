#!/usr/bin/env python

from sys import stdin

def why_am_i_doing_brians_homework(string):
    char = list(string)
    rev_char = list()
    for i in range(0, len(char)):
        rev_char.insert(0, char[i])
    return ''.join(rev_char)

line = stdin.readline()
print why_am_i_doing_brians_homework(line)

