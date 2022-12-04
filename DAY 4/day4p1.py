inputs = open('day4.txt')
inputs = inputs.read().strip().split("\n")

fully_contained = 0
overlap = 0

for i in range(len(inputs)):

    pair = inputs[i].split(",")
    first_elf_bounds = [int(x) for x in pair[0].split("-")]
    second_elf_bounds = [int(x) for x in pair[1].split("-")]

    first_elf_assignment = set(range(first_elf_bounds[0],first_elf_bounds[1]+1))
    second_elf_assignment = set(range(second_elf_bounds[0],second_elf_bounds[1]+1))

    intersection = first_elf_assignment.intersection(second_elf_assignment)

    if (len(intersection) == len(first_elf_assignment)) or (len(intersection) == len(second_elf_assignment)):
        fully_contained += 1

    if len(intersection):
        overlap += 1

print("# of fully contained assigment pairs :", fully_contained)
print("# of assigment pairs that overlap    :", overlap)
