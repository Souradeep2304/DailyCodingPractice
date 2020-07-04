#!/bin/python3

import math
import os
import random
import re
import sys
import operator

"""

# implementation works for small inputs
if __name__ == '__main__':
    s = input()
    l=len(set(s)) #no of unique characters
    i=0
    c=0 #count
    items=dict()
    last=False

    for j in range(0,l): 
        while(True):
            if(i==len(s)-1):
                last=True
                if(s[i-1]==s[i]):
                    items[s[i]]=c+1
                    break
                else:
                    items[s[i]]=1
                    break
            elif(s[i]==s[i+1]):
                c=c+1
                i=i+1
            else:
                break
        if(last==True):
            break
        items[s[i]]=c+1
        i=i+1
        c=0
    
    #res = all(list(items.values())[0] == x for x in items.values())
    res = False
    if(res==True):
        p=0 # to print first 3 most common characters
        for k in sorted(items):
            print(k+" "+str(items[k]))
            p=p+1
            if(p>=3):
                break


    if(res == False):
        final=dict(sorted(items.items(), key=operator.itemgetter(1),reverse=True))
        p=0 # to print first 3 most common characters
        for k in final:
            print(k+" "+str(final[k]))
            p=p+1
            if(p>=3):
                break
"""


from collections import Counter, OrderedDict



class OrderedCounter(Counter, OrderedDict):
    pass

if __name__ == '__main__':
    s = input()
    [print(*c) for c in OrderedCounter(sorted(s)).most_common(3)]


        
    

