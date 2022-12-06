from collections import Counter
with open("input.txt", "r") as file:
    input = file.read()

marker_count = 13

for i in range(len(input)):
    check_str = input[i:i+14]
    marker_count += 1

    if len(set(check_str)) == len(check_str):
        print("found " + check_str + " " + str(i))
        break


print(marker_count)
    




    

