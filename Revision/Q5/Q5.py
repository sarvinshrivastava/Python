#def starts
def fun(num):
    rem = num % 7
    if rem == 0:
        print(num, 'is divisible by 7')
    else:
        print(num, 'is not divisible by 7')
#def ends

#Taking input and calling function
num = int(input('Please enter any number'))
fun(num)
