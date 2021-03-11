# Program to print out the first name and last name of a person in given sentence.

# Programstarts from here
line = input()
line = line.split(' ')
first_name = line[1]
last_name = line[2]
last_name = last_name.split('!')
print(first_name)
print(last_name[0])
