import numpy as np

inputs = open('day10.txt')
inputs = inputs.read().strip().split("\n")

def display(screen):
    cols = 40
    lines = 6

    reshaped = np.reshape(screen,(6,40))

    for j in range(lines):
        line = ""
        for i in range(cols):
            if reshaped[j,i]:
                line+="#"
            else:
                line+="."
        print(line)


def find_register_value(cycle):

    global register_operation
    global register_value

    idx = 0
    count = 0

    while count < cycle:
        count = np.sum(cycle_count[:idx])

        if count < cycle :
            idx += 1

    register_value = 1 + np.sum(register_operation[:idx-1])
    return register_value

cycle_count = []
register_operation = []

screen = np.zeros(240)


for i in range(len(inputs)):

    line = inputs[i].split()

    if line[0] == "addx":
        cycle_count.append(2)
        register_operation.append(int(line[1]))

    elif line[0] == "noop":
        cycle_count.append(1)
        register_operation.append(0)

cycles = np.arange(20,220+1,40)
strengths = [i*find_register_value(i) for i in cycles]

print("Question 1 - Sum of strengths in desired cycles : ", np.sum(strengths))

for j in range(1,len(screen)+1):
    x = find_register_value(j)
    sprite = [x-1, x, x+1]

    if (j-1)%40 in sprite:
        screen[j-1] = "1"


print("\nQuestion 2\n")
display(screen) #EZFPRAKL