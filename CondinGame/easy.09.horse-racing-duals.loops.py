import sys
import math



pi,nb = [], int(input())
for i in range(nb):
    pi.append(int(input()))
pi.sort()

min_delta = 100000
for i in range(nb-1):
    if min_delta==0:
        break 
    if min_delta > abs(pi[i] - pi[i+1]):
        min_delta = abs(pi[i] - pi[i+1])
print(min_delta)