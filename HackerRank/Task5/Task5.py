#Read an integer N. For all non-negative integers i < n, print i^2 .

#problem starts from here
#taking input
N = input()
N = int(N)

#main part
i = 0
while i < N:
    print(i*i)
    i=i+1
