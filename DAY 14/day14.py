import math
import numpy as np
from matplotlib import pyplot as plt

def sandblock():
    global Z
    global x
    global y
    global sand_source
    new_sand = sand_source
    stopped = False

    while not stopped and new_sand[1] < len(y)-2:
        # Move down
        if not Z[np.where(y == new_sand[1])[0]+1, np.where(x == new_sand[0])[0]]:
            new_sand = (new_sand[0],new_sand[1] + 1)

        # Move down diag left
        elif not Z[np.where(y == new_sand[1])[0]+1, np.where(x == new_sand[0])[0]-1]:
            new_sand = (new_sand[0]-1, new_sand[1] + 1)

        # Move down diag right
        elif not Z[np.where(y == new_sand[1])[0]+1, np.where(x == new_sand[0])[0]+1]:
            new_sand = (new_sand[0] + 1, new_sand[1] + 1)

        else:
            stopped=1

    Z[np.where(y == new_sand[1]), np.where(x == new_sand[0])] = 1



inputs = open('day14.txt')
inputs = inputs.read().strip().split("\n")

structures = []
max_x = 0
min_x = math.inf
max_y = 0
min_y = math.inf

sand_source = (500,0)

for lines in inputs:

    # Coordinates of structure nodes
    nodes = lines.split(" -> ")
    nodes = [eval("("+j+")") for j in nodes]
    structures.append(nodes)

    # Find world borders
    for node in nodes+[sand_source]:
        if node[0] < min_x:
            min_x = node[0]
        if node[1] < min_y:
            min_y = node[1]
        if node[0] > max_x:
            max_x = node[0]
        if node[1] > max_y:
            max_y = node[1]


# Make rock lines
Rocks = set()

for structure in structures:
    last_node = structure[0]
    for node in structure:
        rock_x_range = np.arange(np.sort([last_node[0],node[0]])[0],np.sort([last_node[0],node[0]])[1]+1)
        rock_y_range = np.arange(np.sort([last_node[1],node[1]])[0],np.sort([last_node[1],node[1]])[1]+1)
        for x_rock_coord in rock_x_range:
            for y_rock_cord in rock_y_range:
                Rocks.add((x_rock_coord,y_rock_cord))
        last_node = node

# Create World Map
x = np.arange(min_x-1,max_x+2,1,dtype=int)
y = np.arange(min_y-1,max_y+2,1,dtype=int)

X,Y = np.meshgrid(y,x,indexing="ij")

point = [(500,0)]

Z = np.zeros_like(X)

for i in x:
    for j in y:
        if (i,j) in Rocks:
            Z[np.where(y==j),np.where(x==i)]=1


count_blocks = 0
while not any(Z[-1,:]):
    sandblock()
    count_blocks+=1

print("Blocks before void :", count_blocks-1)

plt.imshow(Z,cmap="gray")
plt.axis("off")
plt.show()