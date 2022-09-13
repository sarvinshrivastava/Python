num = int(input('Enter the no. of number to be added in a string:'))
i = 1
lst = []
while i <= num:
    y = int(input('Enter the no:'))
    lst.append(y)
    i = i + 1
list.sort()
x = len(lst)
rem = x % 2
if rem == 0:
    med = (x/2 + (x+1)/2)/2
else:
    med = (x+1)/2
print('Median of the list is:', med)
