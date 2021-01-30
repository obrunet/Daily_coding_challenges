import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

# game loop
while True:
    highest_mountain, idx = 0, 0
    for i in range(8):
        current_mountain = int(input())
        if highest_mountain < current_mountain:
            highest_mountain, idx = current_mountain, i
    print(str(idx))



## other COPIED solution

import sys
import math
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# game loop
while True:
    hiMoI = 0
    hiMo = 0
    for i in range(8):
        # represents the height of one mountain, from 9 to 0.
        mountain_h = int(input())  
        if hiMo < mountain_h: hiMo = mountain_h; hiMoI = i
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    # The number of the mountain to fire on.
    print(hiMoI)
