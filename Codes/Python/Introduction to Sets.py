def average(array):
    s=set(array)
    p=0
    count=0
    for i in s:
        p=p+int(i)
        count=count+1
    return p/count
    

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
