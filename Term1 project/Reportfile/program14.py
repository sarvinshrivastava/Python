print("Program to find the smallest and largest number from the user entered list")
lst = []
num = int(input('Enter the length of list'))
for i in range(num):
    element = int(input('Enter number '))
    lst.append(element)
print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))
