n=int(input())
d=[input().split() for _ in range(n)]

phonebook = {k: v for k,v in d}

while True:
    try:
        name = input()
        if name in phonebook:
            print('%s=%s' % (name, phonebook[name]))
        else:
            print('Not found')
    except:
        break