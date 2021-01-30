#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    current_valley, alt = False, 0
    nb_valley = 0

    for i in s:
        if i == 'D':
            alt -= 1
        else:
            alt += 1 # i == 'U'
    
        if alt < 0:
            current_valley = True
        elif alt == 0 and current_valley:
            nb_valley += 1
            current_valley = False

    return nb_valley


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    fptr.write(str(result) + '\n')
    fptr.close()