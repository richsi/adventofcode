import os

directory = os.getcwd() + "/input.txt"

with open(directory, "r") as file:
    lines = file.readlines()

# PART 1
result = []
for line in lines:
    eachline = []
    for i in line:
        if i.isdigit():
            eachline.append(i)
    result.append(eachline)

finalresult = [] 
totalsum = 0
for item in result:
    total = str(item[0]) + str(item[len(item)-1])
    totalsum += int(total)

# PART2

numDict = {"one" : 1, "two": 2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
result = []
finalresult = [] 
totalsum = 0

for line in lines:
    lineNums = []
    for i in range(len(line)):
        numChar = ""
        if line[i].isdigit():
            lineNums.append(line[i])
            continue
        numChar += line[i]
        for j in range(i+1, len(line)):
            numChar += line[j]
            if numChar in numDict:
                lineNums.append(numDict[numChar])
                break
    result.append(lineNums)

for item in result:
    total = str(item[0]) + str(item[len(item)-1])
    totalsum += int(total)

print(totalsum)