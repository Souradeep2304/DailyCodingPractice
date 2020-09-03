#Write your code here
class Calculator():
    def power(self,a,b):
        if(a<0):
            raise ValueError("n and p should be non-negative")
        elif(b<0):
            raise ValueError("n and p should be non-negative")
        else:
            return(pow(a,b))




myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   