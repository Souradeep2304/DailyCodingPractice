# for _ in range(int(input())):
#     A=list()
#     B=list()
#     n, k = map(int, input().split())
#     for i in range (1,n+1):
#         for j in range(i+1,n+1):
#             A.append(i&j)
#     m=0
#     A.sort()
#     for l in range(0,len(A)):
#         if(A[l]<k):
#             m=A[l]
#         else:
#             break
#     print(m)

T = int(input().strip())
for _ in range(T):
    n , k = map(int , input().split())
    print(k-1 if ((k-1) | k) <= n else k-2)