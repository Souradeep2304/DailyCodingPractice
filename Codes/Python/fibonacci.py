def fibo(a):
    b=0
    c=1
    for i in range(0,a):
        print(str(b)+" ")
        d=b+c
        b=c
        c=d


f=int(input("Enter the number of terms:"))

fibo(f)
        
    
