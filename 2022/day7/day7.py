import os
directory = os.getcwd() + "/input.txt"

with open(directory, "r") as file:
    inputLines = file.readlines()
        
total = 0
for line in inputLines:
    words = line.split()
    print(words)
    if words[0].isdigit():
        if int(words[0]) < 100000:
            print()
            total += int(words[0])


print(total)
