ad, am, ay = [int(x) for x in input().split(' ')] #actual
ed, em, ey = [int(x) for x in input().split(' ')] #expected

fine=0
if (ay, am, ad) <= (ey, em, ed):
    print(0)
elif (ay, am) == (ey, em):
    print(15 * (ad - ed))
elif ay == ay:
    print(500 * (am - em))
else:
    print(10000)