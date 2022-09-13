#7.1 Write a program that prompts for a file name, then opens that file and reads through the file,
#and print the contents of the file in upper case. Use the file word.txt to produce the output below.

#program Starts from bellow
file_name = input("Enter file name: ")
file_handle = open(file_name)
for line in file_handle:
    line = line.rstrip()
    line = line.upper()
    print(line)
