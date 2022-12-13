import numpy as np
import copy

def compare_ints(Left,Right):
    order = 0
    decision = 0

    if Left < Right:
        order = 1
        decision = 1

    elif Left > Right:
        order = 0
        decision = 1

    return order, decision


def compare_lists(Left, Right):

    n = 0
    order = 0
    decision = 0

    while n < np.min([len(Left), len(Right)]) and not decision:

        if isinstance(Left[n],int) & isinstance(Right[n],int):
            order, decision = compare_ints(Left[n], Right[n])

        elif isinstance(Left[n],list) & isinstance(Right[n],list):
            order, decision = compare_lists(Left[n], Right[n])

        else:
            order, decision = compare(Left,Right)

        n+=1

    if not decision:

        if len(Left) < len(Right):
            order = 1
            decision = 1

        elif len(Left) > len(Right):
            order = 0
            decision = 1

    return order, decision

def compare(Left_original,Right_original):
    # Assuming Identical packets do not exist

    Left = copy.deepcopy(Left_original)
    Right = copy.deepcopy(Right_original)

    # Order : 0 incorrect, 1 correct
    decision = 0
    order = 0

    k = 0
    while not decision and k < np.min([len(Left), len(Right)]):

        if type(Left[k]) != type(Right[k]):
            if isinstance(Left[k],int):
                Left[k] = [Left[k]]

            elif isinstance(Right[k],int):
                Right[k] = [Right[k]]

        if isinstance(Left[k],int) & isinstance(Right[k],int):
            order, decision = compare_ints(Left[k], Right[k])

        elif isinstance(Left[k],list) & isinstance(Right[k],list):
            order, decision = compare_lists(Left[k], Right[k])

        k+=1

    if not decision:

        if len(Left) < len(Right):
            order = 1
            decision = 1

        elif len(Left) > len(Right):
            order = 0
            decision = 1

    return order, decision

# Parsing inputs
inputs = open('day13.txt')
inputs = inputs.read().strip().split("\n")

while "" in inputs:
    inputs.remove('')

inputs = [eval(i) for i in inputs]


# Adding divider packets to the lot
inputs.append([[6]])
inputs.append([[2]])

# Sorting packets
decisions = [0]
while not all(decisions):

    decisions = []

    for i in range(len(inputs)-1):

        Left = inputs[i]
        Right = inputs[i+1]

        [order, decision] = compare(Left, Right)
        decisions.append(order)

        if order == 0:
            inputs[i] = Right
            inputs[i+1] = Left


decoder_key = (inputs.index([[6]])+1)*(inputs.index([[2]])+1)
print(decoder_key)
