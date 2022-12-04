import os


directory = os.getcwd() + "\input.txt"


with open(directory, "r") as file:
    list = [entry.strip() for entry in file.readlines()]

counter = 0

#PART1
for line in list:
    halfone, halftwo = line.split(",")

    one, two = halfone.split("-")
    three, four = halftwo.split("-")

    if int(one) <= int(three) and int(two) >= int(four):
        counter += 1
    elif int(one) >= int(three) and int(two) <= int(four):
        counter += 1

#PART2
for line in list:
    halfone, halftwo = line.split(",")

    one, two = halfone.split("-")
    three, four = halftwo.split("-")

    if int(two) >= int(three) and int(one) < int(four):
        counter += 1
    elif int(four) >= int(one) and int(two) > int(three):
        counter+= 1


print(counter)