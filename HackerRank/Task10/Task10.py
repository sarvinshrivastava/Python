# Write a program to print the second lowest grade of N students in class. If some student have same
# marks then print the names in shorted manner.

# program starts from here
# takeing input
num = int(input())
lst_class = [ ]
for i in range(num):
    name = str(input())
    marks = float(input())
    lst_class.append([name,marks])

#finding minimum
vlst=[ ]
for i in lst_class:
    vlst.append(i[1])
    vlst.sort(reverse=True)
newlst = [ ]
min =min(vlst)
l=len(vlst)
for j in range(l):
    if min==vlst[j]:
        vlst[j]=1000.0
#print('Min:',min)

vlst.sort()
#print('Sorted:', vlst)
#print('lstclass:', lst_class)
for i,j in lst_class:
    if j==vlst[0]:
        newlst.append(i)
#print(newlst)
for i in newlst:
    newlst.sort()
for i in newlst:
    print(i)
