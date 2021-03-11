def fun(str):
    x = str.count(' ')
    if x == 0:
        pass
    else:
        print(str.title())

str = input('Enter a string: \n')
fun(str)
