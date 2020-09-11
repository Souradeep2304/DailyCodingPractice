import math  



def isprime(p):
    if p == 2:
        return "Prime"
    elif p == 1 or (p & 1) == 0:
        return "Not prime"
    sq=math.ceil(math.sqrt(p))
    for k in range(2,sq+1):
        if(p%k == 0):
            return("Not prime")
    return("Prime")


n=int(input())
x=[]

for i in range(0,n):
    x.append(int(input()))
    s=isprime(x[i])
    print(s)