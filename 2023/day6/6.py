lines = []
with open("input.txt", "r") as file:
    while line := file.readline():
        lines.append(line.strip())

times = [t for t in lines[0].split("Time: ")[1].split(" ") if t]
distances = [d for d in lines[1].split("Distance: ")[1].split(" ") if d]

res = 1
for time in range(len(times)):
    wins = 0
    current_time = int(times[time]) #7
    for t in range(current_time):
        remaining_time = current_time - t - 1 #6
        distance = remaining_time * (t+1) 
        if distance > int(distances[time]):
            wins += 1
    res *= wins

print(res)


