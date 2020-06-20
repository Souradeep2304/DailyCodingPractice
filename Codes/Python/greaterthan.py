def greater(a,b):
    for number in b:
        if number>a :
            print(number)
            
k=[1,7,5,9,8,3,6,45,78,15,1,0]
p=int(input("Enter the number, greater numbers will be displayed: "))
greater(p,k)
