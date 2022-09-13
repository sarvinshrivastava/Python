list = [ ]
res = 'y'
while res == "y":
    ele = int(input('Enter any random no.'))
    c = ele % 2
    if c == 0:
        pass
    else:
        list.append(ele)
    res = input('Do you whant to continue? y/n')
print(list)
i = 0
m = 0
max = 0
sum = 0
for i in range(len(list)):
    lel = list.pop()
    sum = sum + lel
    #print(lel)
    if m < lel:
        max = lel
        m = lel
    else:
        m = lel
print(max)
print(sum/i)
