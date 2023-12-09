data = [line.strip().split(" ") for line in open("input.txt", "r").read().split("\n")]

def helper(d):
    nums = [d[0]]
    while len(set(d)) > 1:    
        d = [d[i] - d[i-1] for i in range(1, len(d))]
        nums[:0] = [d[0]]

    for i in range(1, len(nums)):
        nums[i] = nums[i] - nums[i-1]
    return nums[-1]
    
res = 0
for d in data:   
    d = [eval(i) for i in d]
    res += helper(d)                  

print(res)