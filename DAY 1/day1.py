import numpy as np

inputs = open('input.txt')
inputs = inputs.read().strip().split("\n\n")

inputs_sums = []

for input in inputs:
    input_values = input.split("\n")
    input_sum = np.sum(np.asarray(input.split("\n"), dtype=int))
    inputs_sums.append(input_sum)

print("Maximum calories by one elf :",np.max(inputs_sums))

sorted_sums = np.flip(np.sort(inputs_sums))
print("Nb of calories carried by the 3 elves with the most :",np.sum(sorted_sums[0:3]))
