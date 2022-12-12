import numpy as np

class Monkey:

  def __init__(self, name, items, operation, test, if_true, if_false):
    self.name = name
    self.items = items
    self.operation = operation
    self.test = test
    self.if_true = if_true
    self.if_false = if_false
    self.inspections = 0

  def inspect_and_throw(self):
      worry_lvl = eval(self.operation.replace("old",str(self.items[0])))
      worry_lvl = int(np.floor(worry_lvl/3))

      if worry_lvl%self.test == 0:
          destination_monkey = self.if_true
      else:
          destination_monkey = self.if_false

      return worry_lvl, destination_monkey


# Read inputs
inputs = open('day11_demo.txt')
inputs = inputs.read().strip().split("\n")

# Parse input and make monkeys
Monkeys = []
for i in range(len(inputs)):
    if "Monkey" in inputs[i]:
        name = int(inputs[i].split()[1][0])
        items = [int(j) for j in inputs[i+1][18:].split(", ")]
        operation = inputs[i+2].split("= ")[1]
        test = int(inputs[i+3].split("by")[1])
        if_true = int(inputs[i+4].split("monkey")[1])
        if_false = int(inputs[i+5].split("monkey")[1])
        Monkeys.append(Monkey(name, items, operation, test, if_true, if_false))

# Compute rounds
round = 1
while round <= 20:
    for i in range(len(Monkeys)):
        while Monkeys[i].items != []:
            worry_lvl, destination_monkey = Monkeys[i].inspect_and_throw()
            Monkeys[destination_monkey].items.append(worry_lvl)
            Monkeys[i].items.pop(0)
            Monkeys[i].inspections+=1

    round+=1

# Print answers
inspections = []
for i in range(len(Monkeys)):
    inspections.append(Monkeys[i].inspections)

print("Monkey Business after 20 rounds : ", sorted(inspections,reverse=True)[0]*sorted(inspections,reverse=True)[1])