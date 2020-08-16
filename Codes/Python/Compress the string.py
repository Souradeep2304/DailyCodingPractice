from itertools import groupby as gr

s="1222311"


for (k,g) in gr(s):
    print("("+str(len(list(g)))+", "+str(k)+")",end =" ")