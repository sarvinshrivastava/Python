#defining function
def fun(lst1, plst, nlst, x, count):
    while count <= x:
        a = lst1.pop()
        count = count + 1
        if a < 0:
            nlst.append(a)
        else:
            plst.append(a)
    print('List with positive no:', plst)
    print('List with negetive no:', nlst)


#formimg lst1
num = int(input('Enter the no. of number to be added in a string:'))
i = 1
lst1 = []
while i <= num:
    y = int(input('Enter the no:'))
    lst1.append(y)
    i = i + 1

#Taking input
lst2 = []; plst = []; nlst = []
lst2 = lst1; x = len(lst1); count = 1

print('Original list:', lst2)

#calling function
fun(lst1, plst, nlst, x, count)
