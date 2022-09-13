print("Program to create a binary file with roll number, name and marks then input a roll number and update the marks")
import pickle
studentdata = {}

studentcount = int(input("Enter no. of student"))
file = open("stud.dat", 'ab')
for i in range(studentcount):
    studentdata["Roll no"] = int(input("Enter the role no."))
    studentdata["Name"] = input("Enter student name")
    studentdata["Marks"] = float(input("Enter marks"))
    pickle.dump(studentdata, file)
    studentdata = {}
file.close()
