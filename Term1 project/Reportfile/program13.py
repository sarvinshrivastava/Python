print("Program to check if the number is a prime or composite")
num = int(input("Enter a number"))
for i in range(2,num):
    if (num % i) == 0:
        print("No. is composite number")
    else:
        print("No. is prime number")
