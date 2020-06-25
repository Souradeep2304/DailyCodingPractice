def counta(s,n):
    
    count=0
    
    for i in s:
        if i=="a":
            if n==0:
                return "0"
            elif len(s)==1:
                return n

            elif n<=len(s):
                for i in k:
                    if (i=="a"):
                        count=count+1
                return count

            else:
                k=(s*(n//len(s)+ 1))[:n]
                for i in k:
                    if (i=="a"):
                        count=count+1
                return count
    
    return "0"


s="avbags"
n=253
print(str(counta(s,n)))