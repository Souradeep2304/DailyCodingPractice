if __name__ == '__main__':
    N = int(input())
    l=[]
    for _ in range(N):
        inp=input().split()
        a=inp[0]
        b=inp[1:]
        if a!="print":
            a+="("+ ",".join(b) +")"
            eval("l."+a)
        else:
            print(l)
