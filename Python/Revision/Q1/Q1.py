#Taking input
x = int(input('Please enter the time taken by A to complete the task.'))
y = int(input('Please enter the time taken by B to complete the task.'))
z = int(input('Please enter the time taken by C to complete the task.'))

#Solving
p = x*y*z
q = x*y + y*z + z*x
Time_by_all = p/q

#Printing
print('Time taken by all to complete the same task  is:',int(Time_by_all))
