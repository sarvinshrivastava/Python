#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    if(year <= 1917 and year >= 1700):
        if(year % 4 == 0):
            y = "12.09." + str(year)
        else:
            y = "13.09." + str(year)
    elif(year >= 1919 and year <= 2700):
        if(year % 4 == 0 and year % 100 != 0):
            y = "12.09." + str(year)
        elif(year == 2000 or year == 2400):
            y = "12.09." + str(year)
        else:
            y = "13.09." + str(year)
    else:
        y = "26.09." + str(year)
    return y


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
