import numpy as np
import math
from matplotlib import pyplot as plt

inputs = open('day15.txt')
inputs = inputs.read().strip().split("\n")

data = []
sensors = set()
beacons = set()


# Parse input
for line in inputs :

    line = line.split(":")

    sensor = []
    sensor.append(int(line[0][10:].split(", ")[0][2:]))
    sensor.append(int(line[0][10:].split(", ")[1][2:]))

    beacon = []
    beacon.append(int(line[1][22:].split(", ")[0][2:]))
    beacon.append(int(line[1][22:].split(", ")[1][2:]))

    coverage = np.abs(sensor[0]-beacon[0])+np.abs(sensor[1]-beacon[1])

    data.append(tuple(sensor+beacon+[coverage]))

# Convert to structured array and sort
data = np.array(data, dtype=np.dtype([('sx', int), ('sy', int),('bx', int),('by', int), ('D', int)]))

# Sort array by x coordinate of sensors
data = np.sort(data,order="sx")

def scan_row(Y):
    global data

    row_coverage = 0
    uncovered_spots = []

    # Only consider sensors which cover the row of interest
    concerned_sensors = data[data["D"] - np.abs(Y - data["sy"]) > 0]

    for i in range(1,len(concerned_sensors)):

         # Compute coverage overlap
         r1 = (concerned_sensors[i-1]["D"]-np.abs(Y-concerned_sensors[i-1]["sy"]))
         r2 = (concerned_sensors[i]["D"]-np.abs(Y-concerned_sensors[i]["sy"]))
         gap = (concerned_sensors[i]["sx"] - concerned_sensors[i-1]["sx"])
         overlap = r1+r2-gap

         if overlap >= 0:
             row_coverage += gap+1

         else :
             row_coverage += gap + overlap + 2
             # À modifier
             uncovered_spots.append([concerned_sensors[i-1]["sx"]+r1+1,Y])

         #Left limit
         if i == 1:
             if r2 > r1 + gap:
                 row_coverage += r2-gap
                 x_min = concerned_sensors[i-1]["sx"] - (r2-gap)
             else:
                 row_coverage += r1
                 x_min = concerned_sensors[i-1]["sx"] - r1

         # Right limit
         if i == len(concerned_sensors)-1:
             if r1 > r2 + gap:
                 row_coverage += r1-gap
                 x_max = concerned_sensors[i]["sx"] + (r1-gap)
             else:
                 row_coverage += r2
                 x_max = concerned_sensors[i]["sx"] + r2

    # Substract points counted in double
    row_coverage -= len(concerned_sensors)-2

    beacons_in_row = len(np.unique(data[["bx","by"]][data["by"]==Y]))
    sensors_in_row = len(data[["sx","sy"]][data["sy"]==Y])

    row_coverage -= beacons_in_row + sensors_in_row

    x_range = x_max - x_min - beacons_in_row - sensors_in_row + 1
    return row_coverage,x_range

# Part 1 :
Y = 2000000
row_coverage, x_range = scan_row(Y)
print("Part 1 : ")
print("In row Y =",Y,",",row_coverage,"spots cannot contain beacons. \n")

# print("Part 2 : ")
# r_min = 0
# r_max = 4000000
# for Y in range(r_min,r_max):
#     row_coverage, x_range = scan_row(Y)



