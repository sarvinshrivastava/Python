def octal_num(n):
    i = 0
    d1 = 0
    d2 = 0
    while(n > 0):
        d2 = (d2 * 10) + n % 8
        i = i + 1
        n = n // 8
    i = i - 1
    while(i >= 0):
        d1 = (d1 * 10) + d2 % 10
        i = i - 1
        d2 = d2 // 10
    return  d1

def hexa_num(n):
    j = 0
    d1 = [ ]
    d2 = ""
    while(n > 0):
        d = n % 16
        if(d > 9):
            if(d == 10):
                d1.append("A")
            elif(d == 11):
                d1.append("B")
            elif(d == 12):
                d1.append("C")
            elif(d == 13):
                d1.append("D")
            elif(d == 14):
                d1.append("E")
            elif(d == 15):
                d1.append("F")
            else:
                pass
        else:
            if(d == 0):
                d1.append("0")
            elif(d == 1):
                d1.append("1")
            elif(d == 2):
                d1.append("2")
            elif(d == 3):
                d1.append("3")
            elif(d == 4):
                d1.append("4")
            elif(d == 5):
                d1.append("5")
            elif(d == 6):
                d1.append("6")
            elif(d == 7):
                d1.append("7")
            elif(d == 8):
                d1.append("8")
            elif(d == 9):
                d1.append("9")
        j = j + 1
        n = n // 16
    j = j - 1
    while(j >= 0):
        d2 = d2 + d1[j]
        j = j - 1
    return  d2

def binary_num(n):
    k = 0
    d1 = 0
    d2 = 0
    while(n > 0):
        d2 = (d2 * 10) + n % 2
        k = k + 1
        n = n // 2
    #i = i
    while(k >= 0):
        d1 = (d1 * 10) + d2 % 10
        k = k - 1
        d2 = d2 // 10
    return  d1 // 10

def print_formatted(number):
    # your code goes here
    i = 2
    print(1, "\t", 1, "\t", 1, "\t", 1)
    while(i <= number):
        o = octal_num(i)
        h = hexa_num(i)
        b = binary_num(i)
        print(i, "\t", o, "\t", h, "\t", b)
        i = i + 1

n = int(input())
print_formatted(n)
