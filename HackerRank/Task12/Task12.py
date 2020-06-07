#Consider a list (list = []). You can perform the following commands:
#1.insert i e: Insert integer e at position i.
#2.print: Print the list.
#3.remove e: Delete the first occurrence of integer e.
#4.append e: Insert integer e at the end of the list.
#5.sort: Sort the list.
#6.pop: Pop the last element from the list.
#7.reverse: Reverse the list.
#Initialize your list and read in the value of followed by lines of commands where each command will be of
#the types listed above. Iterate through each command in order and perform the corresponding operation
#on your list.

# program starts from here
num = int(input())
list = []
q = 0
for i in range(num):
    temp_lst = []
    elm = input()
    temp_lst = elm.split()
    n = len(temp_lst)
    # Insert Section
    if temp_lst[0] == 'insert':
        q = int(temp_lst[1])
        num = int(temp_lst[2])
        list.insert(q, num)
    # Print Section
    elif temp_lst[0] == 'print':
        print(list)
    # Remove Section
    elif temp_lst[0] == 'remove':
        no = int(temp_lst[1])
        list.remove(no)
    # Append Section
    elif temp_lst[0] == 'append':
        s = int(temp_lst[1])
        list.append(s)
    # Sort Section
    elif temp_lst[0] == 'sort':
        list.sort()
    # Pop Section
    elif temp_lst[0] == 'pop':
        list.pop()
    # Reverse Section
    elif temp_lst[0] == 'reverse':
        list.reverse()
