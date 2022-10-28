if __name__ == '__main__':
        s = input()
        i = 0
        f1 = 0
        f2 = 0
        f3 = 0
        f4 = 0
        f5 = 0
        while(i < len(s)):
                a1 = s[i].isalnum()
                a2 = s[i].isalpha()
                a3 = s[i].isdigit()
                a4 = s[i].islower()
                a5 = s[i].isupper()
                if(a1 := 'True'):
                        f1 = 1
                if(a2 := 'True'):
                        f2 = 1
                if(a3 := 'True'):
                        f3 = 1
                if(a4 := 'True'):
                        f4 = 1
                if(a5 := 'True'):
                        f5 = 1
                i = i + 1

        if(f1 == 1):
                print('TRUE')
        if(f2 == 1):
                print('TRUE')
        if(f3 == 1):
                print('TRUE')
        if(f4 == 1):
                print('TRUE')
        if(f5 == 1):
                print('TRUE')
