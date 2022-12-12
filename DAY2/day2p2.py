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
}

winning_rules = {
    "ROCK":"SCISSORS",
    "PAPER":"ROCK",
    "SCISSORS":"PAPER"
}

letter_outcomes = {
    "X":"LOSE",
    "Y":"DRAW",
    "Z":"WIN",
}

inputs = inputs.read().split()
opponent_moves = inputs[0::2]
outcomes = inputs[1::2]

my_score = 0
my_moves = []

for i in range(len(outcomes)):

    my_possible_moves = ["ROCK","PAPER","SCISSORS"]

    if letter_outcomes[outcomes[i]]=="LOSE":
        my_move = winning_rules[letter_shapes[opponent_moves[i]]]

    elif letter_outcomes[outcomes[i]]=="DRAW":
        my_move = letter_shapes[opponent_moves[i]]
        my_score += 3

    elif letter_outcomes[outcomes[i]]=="WIN":
        my_possible_moves.remove(winning_rules[letter_shapes[opponent_moves[i]]])
        my_possible_moves.remove(letter_shapes[opponent_moves[i]])
        my_move = my_possible_moves[0]
        my_score += 6

    my_moves.append(my_move)
    my_score += shape_values[str(my_move)]

print(my_score)