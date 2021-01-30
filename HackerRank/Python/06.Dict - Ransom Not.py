import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mag_dict, note_dict = {}, {}
    
    for m in magazine:
        if m.lower() not in mag_dict:
            mag_dict[m.lower()] = 0
        else:
            mag_dict[m.lower()] += 1

    for n in note:
        if n.lower() not in note_dict:
            note_dict[n.lower()] = 0
        else:
            note_dict[n.lower()] += 1
    
    answer = 'Yes'
    for n in note:
        if n not in mag_dict or mag_dict[n] < note_dict[n]:
            answer = 'No'
            break
    print(answer)


if __name__ == '__main__':
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    checkMagazine(magazine, note)
