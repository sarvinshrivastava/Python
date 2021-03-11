#taking input
i=0
string = input()
sub_string = input()

#main part
string = string.strip()
sub_string = sub_string.strip()
#print(string, sub_string)
len_str = len(string)
len_sub = len(sub_string)
print(len_str, len_sub)
j = 0
n = 0
f = 1
for i in range(len_str):
    print('i=',i)
    for j in range(len_sub):
        print('string=',string[i], 'sub=',sub_string[j])
        if sub_string[j] is string[i]:
            i = i + 1
            f = 0
            print('i=',i,'len_str=',len_str)
            print('j=',j)
            if j == int(len_sub-1):
                print('n=',n)
                n = n + 1
                break
            if i==len_str:
                break

        else:
            #print (j)
            if f == 0:
                break

            else:
                continue

print(n)
