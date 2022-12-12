from collections import defaultdict

inputs = open('day7.txt')
inputs = inputs.read().strip().split("\n")

MAX = 100000

system_tree = defaultdict(lambda: 0)

list_path = ["/"]
path = "//"

size = 0

for line in inputs:

    if line[0:4] == "$ cd":
        if ".." in line:
            list_path.pop()
        elif "/" not in line:
            list_path.append(line[5:])

    elif line[0].isdigit():

        if list_path == ["/"]:
            path = "/".join(list_path)+"/"
        else :
            path = "/".join(list_path)

        file_info = line.split(" ")
        file_size = int(file_info[0])

        #Add to current path and parent paths
        for i in range(len(list_path)):
            if i == 0 :
                path = "//"
            else:
                path = "/".join(list_path[0:i+1])

            system_tree[path] += file_size

sum_sub_max = 0
Disk_space = 70000000
Used_space = system_tree["//"]
Needed_space = 30000000 - (Disk_space-Used_space)
deleted_dir = ""

gap = Disk_space

for k,v in system_tree.items():
    if v <= MAX:
        sum_sub_max += v

    if v>= Needed_space and (v-Needed_space) < gap:
        gap = v-Needed_space
        deleted_dir = k

print("Sum of sizes of dirs under 100 000 :", sum_sub_max)
print("Directory to be deleted :",deleted_dir," of size",system_tree[deleted_dir])