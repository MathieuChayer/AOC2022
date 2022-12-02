inputs = open('day2.txt')

shape_values = {
    "ROCK": 1,
    "PAPER": 2,
    "SCISSORS": 3,
}

letter_shapes = {
    "A":"ROCK",
    "B":"PAPER",
    "C":"SCISSORS",
    "X": "ROCK",
    "Y": "PAPER",
    "Z": "SCISSORS",
}

winning_rules = {
    "ROCK":"SCISSORS",
    "PAPER":"ROCK",
    "SCISSORS":"PAPER"
}

inputs = inputs.read().split()
opponent_moves = inputs[0::2]
my_moves = inputs[1::2]

my_score = 0;

for i in range(len(my_moves)):
    my_score += shape_values[letter_shapes[my_moves[i]]]

    if winning_rules[letter_shapes[my_moves[i]]] == letter_shapes[opponent_moves[i]]:
        my_score += 6

    elif letter_shapes[my_moves[i]] == letter_shapes[opponent_moves[i]]:
        my_score += 3

print(my_score)
