#!/bin/python3

import math
import os
import random
import re
import sys


res=list()
if __name__ == '__main__':
    N = int(input())

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if(emailID.endswith("@gmail.com")):
            res.append(firstName)
res=sorted(res)
for i in range(0,len(res)):
    print(res[i])

