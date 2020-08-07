from collections import OrderedDict
n=int(input())
d=OrderedDict()
for i in range(0,n):
    item,x,quantity=input().rpartition(' ')
    d[item] = d.get(item, 0) + int(quantity)
for key, value in d.items():
    print(key, value)
