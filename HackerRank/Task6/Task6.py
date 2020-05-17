#Criatria:-
#The year can be evenly divided by 4, is a leap year.
#The year can be evenly divided by 100, it is NOT a leap year.
#The year is also evenly divisible by 400. Then it is a leap year.
#Task:- You are given the year, and you have to write a function to check if the year is leap or not.

#program starts from here
#main part
def is_leap(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False
print(is_leap(int(input())))
