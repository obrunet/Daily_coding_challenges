#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(clouds):
    shortest_path = []
    for idx, cloud in enumerate(clouds):
        if idx == 0:
            shortest_path.append(idx)
            current_pos = 0
        else:
            if cloud == 0:
                if idx == len(clouds)-1 or (idx - current_pos) == 2:
                    shortest_path.append(idx)
                    current_pos = idx
                elif clouds[idx+1] == 1:
                    shortest_path.append(idx)
                    current_pos = idx

    return len(shortest_path)-1 



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    fptr.write(str(result) + '\n')
    fptr.close()
