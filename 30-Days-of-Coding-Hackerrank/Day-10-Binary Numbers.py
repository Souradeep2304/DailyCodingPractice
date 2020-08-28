#!/bin/python3

import math
import os
import random
import re
import sys

    

def func(num):
    return num[2:]

if __name__ == '__main__':
    n = int(input())
    
    a = max(func(bin(n)).split('0')).count('1')
    print(a)