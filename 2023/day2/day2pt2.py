import os

directory = os.getcwd() + "/input.txt"
with open(directory, "r") as file:
    lines = file.readlines()

cubes = {"red": 12, "green": 13, "blue":14}
total = 0

for line in lines:
    minCubes = {"red": 0, "green": 0, "blue": 0}
    split_line = line.split(":")
    game_num = split_line[0].split(" ")[1]
    game_instances = split_line[1].split(";")
    for game in game_instances:
        game = game.strip().split(", ")
        for color in game:
            instance = color.split(" ")
            minCubes[instance[1]] = int(instance[0]) if int(instance[0]) > minCubes[instance[1]] else minCubes[instance[1]]
    total += (minCubes["red"] * minCubes["green"] * minCubes["blue"])    


print(minCubes)
print(total)
