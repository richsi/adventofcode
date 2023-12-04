lines = []
winning = []
hand = []
with open("input.txt", "r") as file:
    while line:= file.readline():
        lines.append(line.strip("Card ").strip())

for line in lines:
    winning.append(line.split("|")[0].strip().split(" "))
    hand.append(line.split("|")[1].strip().split(" "))


actual = 0
for x in range(len(hand)):
    first = True
    total = 0
    for y in range(len(hand[x])):
        if hand[x][y] == "":
            continue
        if hand[x][y] in winning[x]:
            if first:
                total += 1
                first = False
                continue
            total *= 2
    actual += total

print(actual)