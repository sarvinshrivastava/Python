print("This program converts octal to decimal")
octal = input("Pls enter any octal no. system number:")
n = octal
count=0
list = []
if '.' in octal:
    #octal = float(octal)
    print("Please enter a non decimal octal no.")
else:
    octal = int(octal)
    n = int(n)
    while(n > 0):
        count = count + 1
        n = n // 10
    while octal > 0:
        pass
    print(list)
