import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = input()
lat = input()
n = int(input())

all_defibs = []
for i in range(n):
    defib = input()
    all_defibs.append(defib)

def distance(lon_a, lon_b, lat_a, lat_b):
    """ Preprocess input: str to float conversion, then calculate & return distance"""
    lon_a = float(str(lon_a).replace(',','.'))
    lon_b = float(str(lon_b).replace(',','.'))
    lat_a = float(str(lat_a).replace(',','.'))
    lat_b = float(str(lat_b).replace(',','.'))
    x = abs(lon_b - lon_a) * math.cos((lat_a + lat_b) / 2)
    y = abs(lat_b - lat_a)
    return math.sqrt(x*x + y*y) * 6371

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
shortest_dist = 6371 # initialize to less than the radius of the earth in km. 
for d in all_defibs:
    d = d.split(';')
    dist = distance(d[4], lon, d[5], lat)
    if shortest_dist > dist:
        shortest_dist = dist
        p = d[1]
print(p)