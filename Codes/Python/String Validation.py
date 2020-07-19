if __name__ == '__main__':
    s = input()
    flag=False
    for i in range(0,len(s)):
        if(s[i].isalnum()==True):
            flag=True
            break
    print(flag)
    flag=False
    for i in range(0,len(s)):
        if(s[i].isalpha()==True):
            flag=True
            break
    print(flag)
    flag=False
    for i in range(0,len(s)):
        if(s[i].isdigit()==True):
            flag=True
            break
    print(flag)
    flag=False
    for i in range(0,len(s)):
        if(s[i].islower()==True):
            flag=True
            break
    print(flag)
    flag=False
    for i in range(0,len(s)):
        if(s[i].isupper()==True):
            flag=True
            break
    print(flag)
