def count_substring(string, sub_string):
    i = 0
    len_str = len(string)
    len_sub = len(sub_string)
    j = 0
    count = 0
    f = 1
    for i in range(len_str):
        #print('i=',i)
        for j in range(len_sub):
            #print('string=',string[i], 'sub=',sub_string[j])
            if sub_string[j] is string[i]:
                i = i + 1
                f = 0
                #print('i=',i,'len_str=',len_str)
                #print('j=',j)
                if j == int(len_sub-1):
                    #print('n=',n)
                    count = count + 1
                    break
                if i==len_str:
                    break
            else:
            #print (j)
                if f == 0:
                    break
                else:
                    continue
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
