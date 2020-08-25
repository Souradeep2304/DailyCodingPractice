#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
res=arr[::-1]
for i in range(0,len(res)):
    print(res[i],end=" ")