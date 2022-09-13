fobject = open("testfile.txt", "w")
sentence = input("Enter the contexrt to be writen in the file: ")
fobject.write(sentence)
fobject.colse()

print("Now reading the contents of the file: ")
fobject = open("testfile.txt", "r")
for str in fobject:
    print(str)
fobject.close()
