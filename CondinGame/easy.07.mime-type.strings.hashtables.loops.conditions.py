import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

association_table = {}

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    association_table[ext.lower()] = mt 

for i in range(q):
    fname = input()  # One file name per line.
    fsplitted = fname.split('.')
    if len(fsplitted) <= 1:
        print("UNKNOWN")
    else:
        try:
            print(association_table[farr[-1].lower()])
        except:
            print("UNKNOWN")
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)



"""

dictionary = {}
n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    dictionary[ext.lower()] = mt    
for i in range(q):
    fname = input()  # One file name per line.
    farr = fname.split('.')
    if len(farr)>1:
        try:
            print(dictionary[farr[-1].lower()])
        except KeyError:
            print("UNKNOWN")
        except IndexError:
            print("UNKNOWN")
    else:
        print("UNKNOWN")
# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
"""