#Read two integers and print two lines. The first line should contain integer division, a //b .
#The second line should contain float division, a / b.
#You don't need to perform any rounding or formatting operations.

#program starts form here
#takeing input
a = input()
a = int(a)
b = input()
b = int(b)

#main part
print(a // b)
a = float(a)
b = float(b)
print(a / b)
