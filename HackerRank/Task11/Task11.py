#Problem: You have a record of N students. Each record contains the student's name, and their percent
#marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer N
#followed by the names and marks for N students. You are required to save the record in a dictionary
#data type. The user then enters a student's name. Output the average percentage marks obtained by that
#student, correct to two decimal places.

#Program starts from here
#Takeing input
num = int(input())
new_lst=[]
lst_name = [ ]
lst_maths = [ ]
lst_physics = [ ]
lst_chemistry = [ ]
for i in range(num):
    elm = input()
    new_lst=elm.split()
    lst_name.append(new_lst[0])
    lst_maths.append(new_lst[1])
    lst_physics.append(new_lst[2])
    lst_chemistry.append(new_lst[3])

#Finding the name and taking out percentage
name = str(input())
num = int(len(lst_name))
for i in range(num):
    if name == lst_name[i]:
        maths = float(lst_maths[i])
        physics = float(lst_physics[i])
        chemistry = float(lst_chemistry[i])
        s = maths + physics + chemistry
        per = s / 3
        print(per)
