# Program starts from here
string = input()
temp_var = input()
temp_var = temp_var.split(' ')
counter = int(temp_var[0])
character = str(temp_var[1])
temp_list = list(string)
temp_list[counter] = character
string = ''.join(temp_list)
print(string)
