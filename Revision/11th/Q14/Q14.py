def diter(a,b,c):
    D = b**2 - 4*a*c
    print(D)
    if D > 0:
        print('Determinant of the quardratic is positive')
    elif D == 0:
        print('Determinant of the quardratic is zero')
    else:
        print('Determinant of the quardratic is negative')
a = int(input('Enter the coefficient of x^2:'))
b = int(input('Enter the coefficient of x:'))
c = int(input('Enter the constant:'))
diter(a,b,c)
