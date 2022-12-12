import numpy as np
import copy

# Simulate operation of CrateMover9000
def CrateMover9000(move):
    global stacks9000

    for n in range(move[0]):
        stacks9000[move[2]].insert(0,stacks9000[move[1]][0])
        stacks9000[move[1]].pop(0)

# Simulate operation of CrateMover9001
def CrateMover9001(move):
    global stacks9001

    stacks9001[move[2]] = stacks9001[move[1]][0:move[0]]+stacks9001[move[2]]

    for i in range(move[0]):
        stacks9001[move[1]].pop(0)

# MAIN CODE
inputs = open('day5.txt')
inputs = inputs.read().strip().split("\n\n")

# Parse the moves
moves = inputs[1].replace("move ","")
moves = moves.replace("to ","")
moves = moves.replace("from ","")
moves = moves.split("\n")

# Parse the stacks
stacks = inputs[0].split("\n")

# Find number of columns
N_stacks = len(stacks[-1].split())
# Each stacks is 3 chars + 1 space between stacks
stack_indexes = np.arange(1, 4*N_stacks+1, 4, dtype=int)

# Storing the data in a dict of keys 1...n stacks.
# Values in dict are a list of the elements in the stack.
# first in the list is top of the stack
dict_stacks = {}

for i in range(1,N_stacks+1):
    dict_stacks[i] = []

for n in range(len(stacks)-1):
    line = [stacks[n][i] for i in stack_indexes]

    for k in range(N_stacks):
        if line[k] != " ":
            dict_stacks[k+1].append(line[k])

# Create copy for both machines
stacks9000 = copy.deepcopy(dict_stacks)
stacks9001 = copy.deepcopy(dict_stacks)

# Execute the moves
for move in moves:
    move = move.split()
    move = [int(x) for x in move]
    CrateMover9000(move)
    CrateMover9001(move)

# Compose and print answers
answer9000 = ""
answer9001 = ""

for i in range(1,N_stacks+1):
    answer9000 += stacks9000[i][0]
    answer9001 += stacks9001[i][0]

print("Top of stacks with CrateMover9000 :",answer9000)
print("Top of stacks with CrateMover9001 :",answer9001)