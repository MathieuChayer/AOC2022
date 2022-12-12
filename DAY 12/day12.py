import math

import numpy as np
start = "S"
end = "E"
inputs = open('day12.txt')
inputs = inputs.read().strip().split("\n")
cols = len(inputs[0])
lines = len(inputs)

map = np.empty((lines,cols),str)
for i in range(len(inputs)):
    map[i,:] = [j for j in inputs[i]]

# Find start/stop and replace with actual heights
start_idx = np.where(map==start)
end_idx = np.where(map==end)
map[start_idx] = "a"
map[end_idx] = "z"

# Initialize visited and steps maps
visited = np.zeros_like(map,float)
steps = math.inf*np.ones_like(map,int)
steps[start_idx] = 0

while visited[end_idx]==0:

    print(np.sum(visited),"/",cols*lines)
    current_node = np.unravel_index(np.argmin(np.where(visited == 0, steps, math.inf), axis=None), steps.shape)
    visited[current_node]=1

    # Down
    if current_node[0]+1 in range(lines):
        if ord(map[current_node]) - ord(map[(current_node[0]+1,current_node[1])]) >= -1:
            new_distance = steps[current_node]+1
            if new_distance < steps[(current_node[0]+1,current_node[1])]:
                steps[(current_node[0] + 1, current_node[1])] = new_distance

    # Up
    if current_node[0]-1 in range(lines):
        if ord(map[current_node]) - ord(map[(current_node[0]-1,current_node[1])]) >= -1:
            new_distance = steps[current_node]+1
            if new_distance < steps[(current_node[0]-1,current_node[1])]:
                steps[(current_node[0]-1, current_node[1])] = new_distance

    # Left
    if current_node[1]-1 in range(cols):
        if ord(map[current_node]) - ord(map[(current_node[0],current_node[1]-1)]) >= -1:
            new_distance = steps[current_node]+1
            if new_distance < steps[(current_node[0],current_node[1]-1)]:
                steps[(current_node[0], current_node[1]-1)] = new_distance

    # Right
    if current_node[1]+1 in range(cols):
        if ord(map[current_node]) - ord(map[(current_node[0],current_node[1]+1)]) >= -1:
            new_distance = steps[current_node]+1
            if new_distance < steps[(current_node[0],current_node[1]+1)]:
                steps[(current_node[0], current_node[1]+1)] = new_distance


print("Minimum number of steps to end : ", int(steps[end_idx[0],end_idx[1]][0]))
