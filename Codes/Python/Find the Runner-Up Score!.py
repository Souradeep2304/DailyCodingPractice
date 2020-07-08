if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(0, len(arr)):    
        for j in range(i+1, len(arr)):    
            if(arr[i] < arr[j]):    
                temp = arr[i];    
                arr[i] = arr[j];    
                arr[j] = temp; 

    for i in range(0,n-1):
        if(i==n):
            print(arr[i])
            break
        if(arr[i]>arr[i+1]):
            print(arr[i+1])
            break
