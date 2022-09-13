#7.2 Write a program that prompts for a file name, then opens that file and reads through the file,
#looking for lines of the form:
#"X-DSPAM-Confidence:"
#Count these lines and extract the floating point values from each of the lines and compute the average
#of those values and produce an output as shown below. Do not use the sum() function or a variable 
#named sum in your solution.

#program starts from here
#opening file
fname = input("Enter file name: ")
fhandle = open(fname)

#loop starts
sum = 0
count = 0
for line in fhandle:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:") :
        count = count + 1
        find_num = line.find('0')
        fvalue = float(line[find_num+1:])
        sum = sum + fvalue

#satisfying end
ave = sum / count
print("Average spam confidence:",ave)
