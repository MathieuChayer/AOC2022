import string

inputs = open('day3.txt')

inputs = inputs.read().split("\n")

objects = string.ascii_letters

sum_of_priorities = 0

i = 0
while i+3 <= len(inputs):

    first_elf = inputs[i]
    second_elf = inputs[i+1]
    third_elf = inputs[i+2]

    for type in objects:
        if bool(type in first_elf) & bool(type in second_elf) & bool(type in third_elf):
            priority = objects.index(type)+1
            sum_of_priorities += priority

    i += 3 # Next group of 3 elves

print(sum_of_priorities)