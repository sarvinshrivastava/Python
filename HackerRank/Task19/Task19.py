def count_substring(string, sub_string):
    flag = 0
    i = 0
    j = 0
    count = 0
    while i < len(string) - 1:
        #print(i)
        if(string[i] ==  sub_string[0]):
                while j < len(sub_string):
                        if(i + j < len(string)):
                            if string[i+j] == sub_string[j]:
                                j = j + 1
                            else:
                                flag = 1
                                break
                        else:
                            break
                        #print(i, j)
                        if j == len(sub_string):
                                count = count + 1
                                j = 0
                                break
        i = i + 1
    return count

if __name__ == '__main__':
        string = input().strip()
        sub_string = input().strip()
        count = count_substring(string, sub_string)
        print(count)
