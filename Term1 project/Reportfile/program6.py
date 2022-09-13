print("Program to write a random number generator that generates random numbers between 1 and 6 (simulates a dice).")
import random
while True:
    num = random.randint(1,6)
    print("You got:",num)
    ch = input("Roll again? (Y/N)")
    if ch in 'Nn':
        break
