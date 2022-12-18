import numpy as np
import math
from matplotlib import pyplot as plt

inputs = open('day15.txt')
row_of_interest = 2000000;
inputs = inputs.read().strip().split("\n")

row_coverage = set()
sensors = []
beacons = []
coverages = []

# Parse input
for line in inputs :

    line = line.split(":")

    sensor = []
    sensor.append(int(line[0][10:].split(", ")[0][2:]))
    sensor.append(int(line[0][10:].split(", ")[1][2:]))
    sensors.append(sensor)

    beacon = []
    beacon.append(int(line[1][22:].split(", ")[0][2:]))
    beacon.append(int(line[1][22:].split(", ")[1][2:]))
    beacons.append(beacon)

    coverage = np.abs(sensor[0]-beacon[0])+np.abs(sensor[1]-beacon[1])
    coverages.append(coverage)

# Check coverage of line of interest for each sensor
for i in range(len(sensors)):

    y_dist = np.abs(row_of_interest-sensors[i][1])
    if y_dist <= coverages[i]:
        xrange = np.abs(y_dist - coverages[i])
        row_coverage.update(set(np.arange(sensors[i][0]-xrange,sensors[i][0]+xrange+1)))

# Substract intersection with Beacons and Sensors
for sensor in sensors:
    if sensor[1] == row_of_interest:
        row_coverage.discard(sensor[0])

for beacon in beacons:
    if beacon[1] == row_of_interest:
        row_coverage.discard(beacon[0])

print(len(row_coverage))