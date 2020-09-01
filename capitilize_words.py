#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    result = ""
    list_string =list(map(str,s.split()))
    for item in range(len(list_string)):
        
        if (list_string[item][0]>=0 and list_string[item][0]<=9) :
            if item == len(list_string)-1:
                    result += list_string[item].capitalize()+"" 
            else:
                    result += list_string[item].capitalize()+ " "
        else:
            result += list_string[item].capitalize()+ " "
            
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
