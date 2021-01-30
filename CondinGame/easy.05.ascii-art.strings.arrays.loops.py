import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
text = input()

rows=[]
for i in range(h):
    row = input()
    rows.append(list(row))

#print(t,l,h, file=sys.stderr)

for i in range(h):
    for t in text:
        if 64 < ord(t.upper()) < 91:
            num = (ord(t.upper())-65)*l
            for j in range(num, num+l):
                print (rows[i][j], end="")
        else:
            for j in range(26*l, 27*l):
                print (rows[i][j], end="")
    print("")