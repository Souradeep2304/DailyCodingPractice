from itertools import groupby as gr

s=input()

for (k,g) in gr(s):
    print("("+str(len(list(g)))+", "+str(k)+")",end =" ")