result = 0
numlist = [10, 20, 30]
numlist.append(40)
for i in range(4):
    result = result + numlist.pop()
avg = result / i
print(result)
print(avg)
