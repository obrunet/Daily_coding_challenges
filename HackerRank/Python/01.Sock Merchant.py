#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    nb_pair = 0
    previous_color, current_color = -1, -1
    for i in ar:
        if i != previous_color:
            previous_color = i
            continue
        nb_pair += 1
        previous_color = -1
    return nb_pair


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()