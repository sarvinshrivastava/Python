#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
        i = 0
        if(s[8] == "P"): #if for p starts
            a = int(s[0]) + 1
            b = int(s[1]) + 2
            print(a, b)
            if(a != 2 or b != 4): #if for not 12 starts
                    print("yup still here")
                    print("a = ", a, "b = ", b)
                    if (b > 9): #if for b greater than 9 starts
                        b = b % 10
                        a = a + 1
                        print("a = ", a, "b = ", b)
                        if(a == 1):
                            a = 49
                        elif(a == 2):
                            a = 50
                        else:
                            pass
                        if(b == 0):
                            b = 48
                        elif(b == 1):
                            b = 49
                        elif(b == 2):
                            b = 50
                        elif(b == 3):
                            b = 51
                        elif(b == 4):
                            b = 52
                        elif(b == 5):
                            b = 53
                        elif(b == 6):
                            b = 54
                        elif(b == 7):
                            b = 55
                        elif(b == 8):
                            b = 56
                        elif(b == 9):
                            b = 57
                        else:
                            pass
                        string = chr(a) + chr(b) + s[2 : 8]
                    else: #else for b greater than 9 starts
                        if(a == 1):
                            a = 49
                        elif(a == 2):
                            a = 50
                        else:
                            pass
                        if(b == 0):
                            b = 48
                        elif(b == 1):
                            b = 49
                        elif(b == 2):
                            b = 50
                        elif(b == 3):
                            b = 51
                        elif(b == 4):
                            b = 52
                        elif(b == 5):
                            b = 53
                        elif(b == 6):
                            b = 54
                        elif(b == 7):
                            b = 55
                        elif(b == 8):
                            b = 56
                        elif(b == 9):
                            b = 57
                        else:
                            pass
                        string = chr(a) + chr(b) + s[2 : 8]
            else: #else for not 12 starts
                string = s[ : 8]

        else: #else for P
            a = int(s[0])
            b = int(s[1])
            if(a == 1 and b == 2):
                string = chr(48) + chr(48) + s[2 : 8]
            else:
                string = s[ : 8]

        print(string)


s = input()
timeConversion(s)
