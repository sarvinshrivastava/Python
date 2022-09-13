print("Program to read a text file and display the number of vowels/consonants/uppercase/lowercase characters in the file")
file = open("trial.txt")
content = file.read()
vowels = 0
consonents = 0
lowercase = 0
uppercase = 0
for ch in content:
    if(ch.islower()):
        lowercase += 1
    elif(ch.isupper()):
        uppercase += 1
    ch = ch.lower()
    if(ch in ['a', 'e', 'i', 'o', 'u']):
        vowels += 1
    elif(ch not in ['a', 'e', 'i', 'o', 'u']):
        consonants += 1
file.close()
print("No. of vowels are:", vowels)
print("No. of consonants are:", consonants)
print("No. of lowercase letters are:", lowercase)
print("No. of uppercase letters are:", uppercase)
