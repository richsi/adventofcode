crates = [['A','B'], ['C','D','E'], ['F','G','H']]

list = [1,2,3,4,5,6]
list2 = [7]

temp = list[-3:]
temp.reverse()
del list[-3:]

print(temp)
print(list)

list2.extend(temp)
print(list2)