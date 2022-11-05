def solve(s):
        s = s.capitalize()
        i = 1
        print(len(s))
        while i < int(len(s)):
                if(s[i] == " "):
                        s = s[ : i] + s[i] + s[i + 1].upper() + s[i + 2 : ]
                else:
                    pass
                i = i + 1

        return s

s = input()
result = solve(s)
print(result)
