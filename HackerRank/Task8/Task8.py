#You have to print a list of all possible coordinates given by (i,j,k )on a 3D grid where the sum of i + j+ k != N.
#Here:-
#0 <= i <= X
#0 <= j <= Y
#0 <= k <= Z

#program starts from Here
#takeing input
X = int(input())
Y = int(input())
Z = int(input())
N = int(input())
lst=[]

#Main Part
i=j=k=0
while i<=X:
    while j<=Y:
        while k<=Z:
            s=i+j+k
            if s!=N:
                lst.append([i,j,k])
            k=k+1
        j=j+1
        k=0
    i=i+1
    j=0
    k=0

#final part
print(lst)
