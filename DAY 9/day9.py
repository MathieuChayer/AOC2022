import numpy as np
from collections import defaultdict

inputs = open('day9.txt')
inputs = inputs.read().strip().split("\n")

nuts = defaultdict()

N_nuts = 10

for i in range(N_nuts):
    nuts[i] = [(0,0)]

for i in range(len(inputs)):

    move = inputs[i].split()
    move[1] = int(move[1])
    delta_x = 0
    delta_y = 0

    if move[0] == "U":
        delta_y = 1
    elif move[0] == "D":
        delta_y = -1
    elif move[0] == "R":
        delta_x = 1
    elif move[0] == "L":
        delta_x = -1

    for k in range(1,move[1]+1):

        nuts[0].append((nuts[0][-1][0]+delta_x,nuts[0][-1][1]+delta_y))

        for j in range(1,N_nuts):

            x_gap = nuts[j-1][-1][0]-nuts[j][-1][0]
            y_gap = nuts[j-1][-1][1]-nuts[j][-1][1]
            xy_gap = [x_gap,y_gap]

            idx_max_gap = np.argmax(np.abs(xy_gap))
            move_T = [0,0]

            if np.sum(np.abs(xy_gap)) == 4:
                move_T[idx_max_gap] = xy_gap[idx_max_gap]//2
                move_T[not(idx_max_gap)] = xy_gap[not(idx_max_gap)]//2
                nuts[j].append((nuts[j][-1][0]+move_T[0],nuts[j][-1][1]+move_T[1]))

            if np.sum(np.abs(xy_gap)) == 3:
                move_T[idx_max_gap] = xy_gap[idx_max_gap]//2
                move_T[not(idx_max_gap)] = xy_gap[not(idx_max_gap)]
                nuts[j].append((nuts[j][-1][0]+move_T[0],nuts[j][-1][1]+move_T[1]))


            elif np.sum(np.abs(xy_gap))==2 & np.max(np.abs(xy_gap))>1:
                move_T[idx_max_gap] = xy_gap[idx_max_gap]//2
                nuts[j].append((nuts[j][-1][0]+move_T[0],nuts[j][-1][1]+move_T[1]))

            else:
                nuts[j].append((nuts[j][-1][0], nuts[j][-1][1]))
# Different positions
print("Number of different positions occupied at least once by T : ",len(set(nuts[N_nuts-1])))





