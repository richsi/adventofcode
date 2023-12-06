lines = []
with open("input.txt", "r") as file:
    while line := file.readline():
        lines.append(line.strip())

#['Time:        44     89     96     91', 'Distance:   277   1136   1890   1768']
times = "".join([t for t in lines[0].split("Time: ")[1].split(" ") if t])
distances = "".join([d for d in lines[1].split("Distance: ")[1].split(" ") if d])

print(times, distances)

wins = 0
for time in range(int(times)): 
    remaining_time = int(times) - time - 1 
    distance = remaining_time * (time + 1) 
    print(distance)
    if distance > int(distances):
        wins += 1
print(wins)
