import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
current_x, current_y = initial_tx, initial_ty

while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    if light_y > current_y and current_y < 18:
        direction = "S"
        current_y += 1
    elif light_y < current_y and current_y >= 0:        
        direction = "N"   
        current_y -= 1

    if light_x > initial_tx and current_x < 40:
        direction += "E"
        current_x += 1
    elif light_x < current_x and current_x >= 0:
        direction += "W"
        current_x -= 1
        
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(direction)
    
    # learned: don't forget to increase counter when needed
    # questions: Why does board start in upper left corner?