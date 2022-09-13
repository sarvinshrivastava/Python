print("Program to identify a no is armstrong")
num = int(input("Enter a no."))
sum = 0
temp = num
i = 0
while i < len(str(num)):
    dig = num % 10
    num=num-dig
    num = num/10
    sum += dig ** 3
    i=i+1
if temp == sum:
    print("No. is armstrong")
else:
    print("No. is not armstrong")
