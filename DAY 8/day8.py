import numpy as np
import matplotlib.pyplot as plt

def check_visibility(line):

    visibility_line = np.zeros_like(line)

    for count, ele in enumerate(line):

        # Set visible perimeter
        if count == 0 or count == len(line):
            visibility_line[count] = 1

        # Check the inside
        else:
            if any([all(j < ele for j in line[:count]),
                    any([all(j < ele for j in line[::-1][:(len(line) - count - 1)]), 0])]):
                visibility_line[count] = 1

    return visibility_line

def uni_score(value,line):
    scenic_score = 0

    if line == []:
        scenic_score = 0
    else:
        for count,ele in enumerate(line):
            if count == 0:
                scenic_score += 1
                if ele >= value:
                    break
            elif all(j < value for j in line[:count]) :
                scenic_score += 1
            if ele>=value:
                break

    return scenic_score


# Main Code
inputs = open('day8.txt')
inputs = inputs.read().strip().split("\n")

cols = len(inputs[0])
lines = len(inputs)

map = np.zeros((lines,cols))

for i in range(lines):
    map[i] = np.fromiter((int(j) for j in inputs[i]),int)

map = map.astype(int)

visibility_map = np.zeros_like(map)
horizontal_visibility = np.zeros_like(map)
vertical_visibility = np.zeros_like(map)
scenic_score = np.ones_like(map)

for count, line in enumerate(map):
    horizontal_visibility[count,:] = check_visibility(line)

for count, line in enumerate(np.transpose(map)):
    vertical_visibility[:,count] = np.transpose(check_visibility(line))

visibility_map = np.logical_or(horizontal_visibility,vertical_visibility)
visibility_map = visibility_map.astype(int)

for idx, value in np.ndenumerate(map):
    left = map[idx[0],:idx[1]][::-1]
    right = map[idx[0],idx[1]+1:]
    top = map[:idx[0],idx[1]][::-1]
    bottom = map[idx[0]+1:,idx[1]]

    score_left = uni_score(value, left)
    score_right = uni_score(value, right)
    score_top = uni_score(value, top)
    score_bottom = uni_score(value, bottom)

    scenic_score[idx] = score_left*score_right*score_top*score_bottom

# Answers
print("Number of visible trees : ",np.sum(visibility_map))
print("Maximum scenic score : ", np.max(scenic_score))

fig, (ax1, ax2, ax3) = plt.subplots(1,3)
ax1.set_title('Trees map')
im1 = ax1.imshow(map, interpolation='none', cmap="Greens")
ax2.set_title('Visibility map')
im2 = ax2.imshow(visibility_map, interpolation='none', cmap="gray")
ax3.set_title('Scenic score map')
im3 = ax3.imshow(scenic_score, interpolation='none', cmap="gray")
plt.show()