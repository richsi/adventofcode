import re

with open("input.txt", "r") as file:
    list = [entry.rstrip() for entry in file.readlines()]


columns = [['N','D','M','Q','B','P','Z'], ['C','L','Z','Q','M','D','H','V'], ['Q','H','R','D','V','F','Z','G'],
            ['H','G','D','F','N'],['N','F','Q'], ['D','Q','V','Z','F','B','T'], ['Q','M','T','Z','D','V','S','H'],
            ['M','G','F','P','N','Q'],  ['B','W','R','M']]

for i in range(10):
    list.pop(0)

#PART 1
line_list = []
for line in list:
    line_list = [int(s) for s in line.split() if s.isdigit()]

    for num in range(line_list[0]):
        ele = columns[line_list[1]-1].pop()
        columns[line_list[2]-1].append(ele)




#PART 2
line_list = []
temp = []
for line in list:
    line_list = [int(s) for s in line.split() if s.isdigit()]

    if line_list[0] == 1:
        print("1")
        ele = columns[line_list[1]-1].pop()
        columns[line_list[2]-1].append(ele)
    else:
        for num in range(line_list[0]):
            ele = columns[line_list[1]-1].pop()
            temp.append(ele)

        for item in reversed(temp):
            columns[line_list[2]-1].append(item)
        temp.clear()




crate_order = ''
for crate in columns:
    crate_order += crate[-1]

print(crate_order)