#program starts from here
#takeing input
num = int(input())
max = None
elm = input()
lst_pcepants = [ ]
lst_pcepants = list(map(int, elm.split()))

#finding max
i = 0
for i in range(num):
    if max is None or max < int(lst_pcepants[i]):
        max = int(lst_pcepants[i])

#finding runnerup
runerup = None
i=0
for i in range(0,num):
    if max == int(lst_pcepants[i]):
        lst_pcepants[i] = None
i = 0
for i in range(0,num):
    if lst_pcepants[i] is None:
        continue
    if runerup is None or runerup < int(lst_pcepants[i]):
        runerup = lst_pcepants[i]

#printing
print(runerup)
