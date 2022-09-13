def fun():
    #Creating list
    num = int(input('Enter the no. of students to be added in the tuple:'))
    i = 1
    lst = []
    while i <= num:
        y = input('Enter the name of students:')
        lst.append(y)
        i = i + 1
    #Converting list to tuple
    tup = tuple(lst)
    #Checking for entered name
    name = input('Enter a name of student to check his/her presence:')
    x = tup.count(name)
    if x == 0:
        print('Entered name does not exists in tuple')
    else:
        print('Entered name does exists in tuple')
#Calling function
fun()
