#program to create a claculator
a = int(input("Enter no. 1:"))
b = int(input("Enter no. 2:"))
c = str(input("Enter opperation:"))
if c == '+':
    print(a+b)
elif c == '-':
    print(a-b)
elif c == '*':
    print(a*b)
elif c == '/':
    print(a/b)
elif c == '//':
    print(a//b)
elif c == '%':
    print(a%b)
else:
    print("Enter correct opperation")
