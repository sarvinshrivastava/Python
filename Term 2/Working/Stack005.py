n = [12, 13, 34, 56, 21, 79, 98, 22, 35, 38]
i = 0
m = [ ]
for i in range(len(n)):
    if n[i]%2 == 0:
        m.append(n[i])
    else:
        pass
j = 0
for j in range(len(m)):
    ele = m.pop()
    print(ele)
