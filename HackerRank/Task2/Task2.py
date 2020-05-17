#Given an integer, perform the following conditional actions:
#If is odd, print Weird
#If is even and in the inclusive range of 2 to 5 print Not Weird.
#If is even and in the inclusive range of 6 to 20 print Weird.
#If is even and greater than 20  print Not Weird.
#Input 3

#program starts from here
#takeing Input
num = input("Enter a number")
num = int(num)

#main part
rem = num % 2
if rem == 0:
    if num <= 5:
        print("Not Weird")
    elif num <= 20:
        print("Weird")
    elif 20 < num:
        print("Not Weird")
else:
    print("Weird")
