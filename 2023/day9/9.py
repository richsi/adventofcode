data = [line.strip().split(" ") for line in open("input.txt", "r").read().split("\n")]

def helper(d, total):
    total += d[-1]
    if all(i == 0 for i in d):  return total 
    hist = [d[i] - d[i-1] for i in range(1, len(d))] #generating new list
    return helper(hist, total)                        #recursive call

res = 0
for d in data:                                 # iterate through each list in data
    d = [eval(i) for i in d]
    res += helper(d, 0)                   # call the helper function on each list to obtain the result

print(res)