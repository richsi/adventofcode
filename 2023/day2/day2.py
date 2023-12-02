import os

directory = os.getcwd() + "/input.txt"
with open(directory, "r") as file:
    lines = file.readlines()

cubes = {"red": 12, "green": 13, "blue":14}
total = 0
valid = True
for line in lines:
    split_line = line.split(":")
    game_num = split_line[0].split(" ")[1]
    game_instances = split_line[1].split(";")
    for game in game_instances:
        game = game.strip().split(", ")
        for color in game:
            instance = color.split(" ")
            valid = False if int(instance[0]) > cubes[instance[1]] else True
            if not valid:
                break
        if not valid:
            break
    if valid:
        print("computing total")
        total += int(game_num)

