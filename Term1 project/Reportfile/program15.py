print("Program to swap the element of list at even position with odd position")
lst = []
num = int(input('Enter the length of list'))
for i in range(num):
    element = int(input('Enter number '))
    lst.append(element)
s = len(lst)
if s % 2 != 0:
    s = s - 1
for i in range(0,s,2):
    lst[i], lst[i+1] = lst[i+1], lst[i]
print("List after swapping :", lst)
