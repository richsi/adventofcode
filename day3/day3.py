
import os

directory = os.getcwd() + "\day3\input.txt"

with open(directory, "r") as file:
    list = file.readlines()

# lenth = len(list)
# print(lenth)

lowercase = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16,
                "q":17, "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}

uppercase = {"A":27, "B":28, "C":29, "D":30, "E":31, "F":32, "G":33, "H":34, "I":35, "J":36, "K":37, "L":38, "M":39, "N":40, "O":41, "P":42,
                "Q":43, "R":44, "S":45, "T":46, "U":47, "V":48, "W":49, "X":50, "Y":51, "Z":52}

total = 0
priority_list = []
temp_list = []
count = 0

#PART 1
# for line in list:
#     length = int(len(line) / 2)
#     # print(length)
#     one = line[:length]
#     two = line[length:]

#     for i in range(len(one)):
#         if (one[i] in two):
#             print(one[i])
#             priority_list.append(one[i])
#             break

# PART 2
for line in list:
    temp_list.append(line.strip())
    count += 1
    if (count == 3):
        #print(newele + " " + temp_list[0] + " " + temp_list[1] + " " + temp_list[2])
        newele = temp_list[0]
        for i in range(len(newele)):
            if (newele[i] in temp_list[1]) and (newele[i] in temp_list[2] and newele[i] in temp_list[0]):
                priority_list.append(newele[i])
                break

        temp_list.clear()
        count = 0


#GETTING THE SUM 
for item in priority_list:
    #print(item)
    if item in lowercase.keys():
        total += lowercase.get(item)

    elif item in uppercase.keys():
        total += uppercase.get(item)


print(total)
