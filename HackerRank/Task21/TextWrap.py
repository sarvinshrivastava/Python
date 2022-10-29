import textwrap

def wrap(string, max_width):
    i = 1
    f = 0
    l = len(string)
    while(i <= l):
        if(i % max_width == 0 and i != len(string)):
            if f == 0:
                string = string[ : i] + "\n" + string[i : ]
                f = 1
            else:
                string = string[ : i + f] + '\n' + string[i + f :]
                f = f + 1
            l = len(string)
        i = i + 1
    return string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
