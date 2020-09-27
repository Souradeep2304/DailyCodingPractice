n = int(input())
s = set(map(int, input().split()))
N=int(input())
for i in range(0,N):
    l=list(map(str, input().split()))
    if(l[0]=='remove'):
        s.remove(int(l[1]))
    elif(l[0]=='discard'):
        s.discard(int(l[1]))
    else:
        s.pop()
print(sum(s))