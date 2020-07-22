#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    for x in s[:].split():
        s=s.replace(x,x.capitlize())
    return(s)

if __name__ == '__main__':
    

    s = input()

    result = solve(s)

    print(result)
