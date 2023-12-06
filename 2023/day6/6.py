with open("input.txt", "r") as file:
    times = [t for t in file.readline().strip().split("Time: ")[1].split(" ") if t]
    distances = [d for d in file.readline().strip().split("Distance: ")[1].split(" ") if d]

res = []
for time in range(len(times)):
    wins = 0
    for t in range(int(times[time])):
        remaining_time = int(times[time]) - t - 1 #6
        if remaining_time * (t+1)  > int(distances[time]):
            wins += 1
    res.append(wins)

print(res[0] * res[1] * res[2] * res[3])


