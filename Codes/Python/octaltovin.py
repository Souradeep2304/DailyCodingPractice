number=int(input())
if(number > 7):
    print("Your Warning")
else:
    number=str(number)
    dec = str(int(number, 8));
    decm = int(dec);
    print("in Binary =",bin(decm));
