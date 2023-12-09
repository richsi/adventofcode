import numpy as np

lines = [line.strip() for line in open("input.txt", "r").read().split("\n") if line != ""]
instruction = lines.pop(0)
lines = [line.split("=") for line in lines]

d= {}
for line in lines:
    line[0] = line[0].strip(" ")
    line[1] = line[1].strip(" () ").split(",")
    d[line[0]] = line[1]


def navigate(inst, d, start):
    if inst == "R":
        return d[start][1].strip()
    else:
        return d[start][0].strip()

count = 0
steps = 0
start = "AAA"


while True:
    print(start, count, instruction[count])
    start = navigate(instruction[count], d, start)
    steps += 1

    if start == "ZZZ":
        print(steps, start)
        break

    if count == len(instruction) -1 :
        count = 0
        continue

    count += 1

