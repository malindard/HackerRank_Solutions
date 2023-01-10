'''
Link: https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
Difficulty: Easy
Max score: 10
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    for i in s.split():
        s = s.replace(i, i.capitalize())
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

# replace() : replaces a specified phrase with another specified phrase.
# syntax : string.replace(oldvalue, newvalue, count)
# count : Optional. A number specifying how many occurrences of the old value you want to replace. Default is all occurrences

# split() : splits a string into a list.
# syntax : string.split(separator, maxsplit)
# https://www.w3schools.com/python/ref_string_split.asp
