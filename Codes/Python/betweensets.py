#!/bin/python3
 
import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def gcd(a, b):
    while a % b != 0:
        a, b = b, (a % b)
    return b

def lcm(a,b):
    return a * b // gcd(a, b)

def getTotalX(a, b):
    # Write your code here
    mingcd=b[0]
    maxlcm=a[0]
    for i in range(m):
        if(i+1)==m:
             break
        mingcd=gcd(mingcd,b[i+1])
        
    for i in range(n):
        if(i+1)==n:
             break
        maxlcm=lcm(maxlcm,a[i+1])
        
    count = 0
    for i in range(maxlcm, mingcd+1, maxlcm):
        if mingcd % i==0:
            count=count+1
 
    return count
        
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
