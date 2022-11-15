import math
import os
import random
import re
import sys

from collections import Counter

def pickingNumbers(a):
        countNums = Counter(a)
        maxnum = 0
        print(countNums, "\n")
        
        for i in range(1, 100):
             #print(countNums[i], " ", countNums[i + 1])
             maxnum = max(maxnum, countNums[i]+countNums[i+1])                      
        
        return maxnum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
