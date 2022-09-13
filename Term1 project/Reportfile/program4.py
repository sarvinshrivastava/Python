print("Program to create a binary file with name and roll number then Search for a given roll number and display the name, if not found display appropriate message.")
import pickle
import sys
dict = {}
def writinfile():
    file = open("stud2.dat",'ab')
    no = int(input("Enter no of students:"))
    for i in range(no):
        print("Enter details of student", i + 1)
        dict["roll"] = int(input("Enter roll number:"))
        dict["name"] = input("Enter the name:")
        pickle.dump(dict, file)
file.close()
