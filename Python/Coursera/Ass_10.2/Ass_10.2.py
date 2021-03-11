#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

#program starts from here
#opening file
fhandle = open("mbox-short.txt")

#main body
time=[]
lst=[]
hour = { }
for line in fhandle:
    line = line.strip()
    if 'From ' in line:
        line = line.rstrip()
        line = line.split()
        string = line[5]
        string = string[0:2]
        lst.append(string)
print(lst)
for our in lst:
    hour[our] = hour.get(our, 0) + 1
for k,v in hour.items():
    newtp=(k,v)
    time.append(newtp)
time = sorted(time)

#final print
for k,v in time:
    print(k,v)
