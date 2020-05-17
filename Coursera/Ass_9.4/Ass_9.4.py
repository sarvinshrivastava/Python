#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear
#in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the
#most prolific committer.

#program starts from here
#opening file
fhandle = open('mbox-short.txt')

#main body
email_id = dict()
lst=list()
for line in fhandle:
    line = line.rstrip()
    if 'From ' in line:
        line = line.split()
        lst.append(line[1])
for word in lst:
    email_id[word] = email_id.get(word, 0) + 1

bigword=None
bigcount=None
for word, count in email_id.items():
    if bigcount is None or count> bigcount:
        bigcount=count
        bigword=word

#final printing
print(bigword, bigcount)
