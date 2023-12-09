import functools
import math

with open("input.txt", "r") as f:
    instructions = f.readline().strip("\n")
    f.readline()
    D = {}
    starting_nodes = []
    while line := f.readline().strip("\n"):
        start, dests = line.split("=")[0].strip(), line.split("=")[1].strip("() ").split(", ")
        D[start] = {"L": dests[0], "R": dests[1]}
        if start[-1] == "A":
            starting_nodes.append(start)

combined_steps = []
for node in starting_nodes:
    steps = 0
    while True:
        for inst in instructions:
            steps += 1
            print(D[node][inst], inst)
            node = D[node][inst]
            if node[-1] == "Z":
                break
        if node[-1] == "Z":
            combined_steps.append(steps)
            break

print(functools.reduce(lambda x,y: (x*y) // math.gcd(x, y), combined_steps))