import numpy

def arrays(arr):
    a=numpy.array(arr,float)
    res=a[::-1]
    return res

arr = input().strip().split(' ')
result = arrays(arr)
print(result)