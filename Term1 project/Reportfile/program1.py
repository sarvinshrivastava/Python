print("Program to read a text file line by line and display each word separated by a '#'.")
f = open("trial.txt")
item = []
for line in f:
    words = line.split()
    for i in words:
        item.append(i)
print('#'.join(item))
