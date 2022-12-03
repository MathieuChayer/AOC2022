import string

inputs = open('day3.txt')

inputs = inputs.read().split("\n")

objects = string.ascii_letters

sum_of_priorities = 0


for i in range(len(inputs)):

    n_objects = len(inputs[i])

    first_compartment = inputs[i][0:n_objects//2]
    second_compartment = inputs[i][n_objects//2::]

    for type in objects:
        if bool(type in first_compartment) & bool(type in second_compartment):
            priority = objects.index(type)+1
            sum_of_priorities += priority
            break

print(sum_of_priorities)