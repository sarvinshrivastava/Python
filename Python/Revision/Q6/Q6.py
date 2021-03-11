#def starts
def fun(name, gend):
    if gend == 'm':
        print('You are: Mr.', name)
    else:
        print('You are: Ms.', name)
#def ends

#Taking input and calling function
name = input('Enter your name:')
gend = input('Enter your gender:')
fun(name, gend)
