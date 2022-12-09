import numpy as np
import matplotlib.pyplot as plt

def check_visibility(line):

    visibility_line = np.zeros_like(line)

    for count, ele in enumerate(line):

        # Set visible perimeter
        if count == 0 or count == len(line):
            visibility_line[count] = True

        # Check the inside
        else:
            if any([all(j < ele for j in line[:count]),
                    any([all(j < ele for j in line[::-1][:(len(line) - count - 1)]), 0])]):
                visibility_line[count] = True

    return visibility_line


inputs = open('day8_demo.txt')
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

for count, line in enumerate(map):
    horizontal_visibility[count,:] = check_visibility(line)

for count, line in enumerate(np.transpose(map)):
    vertical_visibility[:,count] = np.transpose(check_visibility(line))

visibility_map = np.logical_or(horizontal_visibility,vertical_visibility)

print(np.sum(visibility_map))

fig, (ax1, ax2) = plt.subplots(1,2)
ax1.set_title('Trees map')
im1 = ax1.imshow(map, interpolation='none', cmap="Greens")
ax2.set_title('Visibility map')
im2 = ax2.imshow(visibility_map, interpolation='none', cmap="gray")
plt.show()