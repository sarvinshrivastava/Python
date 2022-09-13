def test(num):
    rem = num % 7
    if rem == 0:
        return(print("Divisible"))
    else:
        return(print("Not Divisible"))
num = int(input('Enter any no:'))
test(num)
