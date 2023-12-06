with open("input.txt", "r") as file:
    times = "".join([t for t in file.readline().split("Time: ")[1].split(" ") if t])
    distances = "".join([d for d in file.readline().split("Distance: ")[1].split(" ") if d])

wins = 0
for time in range(int(times)): 
    distance = int(times) - time - 1  * (time + 1) 
    if distance > int(distances):
        wins += 1
print(wins)
