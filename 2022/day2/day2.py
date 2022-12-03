import os
directory = os.getcwd() + "\day2\input.txt"

A = 1
B = 2
C = 3

total = 0

X = 0
Y = 3
Z = 6

with open(directory, "r") as file:
    list = file.readlines()

for line in list:
    one, two = line.split(" ")
    score = 0

    if one == "A" and two.strip() == "X": #lose draw win
        score = X + C
        total += score
        
    elif one == "A" and two.strip() == "Y":
        score = Y + A
        total += score
    elif one == "A" and two.strip() == "Z":
        score = Z + B
        total += score

    elif one == "B" and two.strip() == "X":
        score = X + A
        total += score
    elif one == "B" and two.strip() == "Y":
        score = Y + B
        total += score
    elif one == "B" and two.strip() == "Z":
        score = Z + C
        total += score

    elif one == "C" and two.strip() =="X":
        score = X + B
        total += score
    elif one == "C" and two.strip() == "Y":
        score = Y + C
        total += score
    elif one == "C" and two.strip() == "Z":
        score = Z + A
        total += score

print(total)
