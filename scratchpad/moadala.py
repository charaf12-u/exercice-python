#import math
a=float(input("doner a"))
b=float(input("doner b"))
c=float(input("doner c"))

if(a!=0):
    if(b!=0):
        if(c!=0):
            delta = b * b - 4 * a * c
            if(delta<0):
                print("pas solution")
            elif(delta==0):
                x=-b/(2*a)
                print("solution =",x)
            else:
                x1 = (-b - math.sqrt(delta)) / (2 * a)
                print("1 racine =", x1)
                x2 = (-b + math.sqrt(delta)) / (2 * a)
                print("2 racine =", x2)
        else:
            x1=0
            print("1 racine =", x1)
            x2=-b/a
            print("2 racine =", x2)
    else:
        x = 0
        print("racine =", x)
else:
    if(b!=0):
        if(c!=0):
            x=-c/b
            print("la solution =",x)
        else:
            x = 0
            print("racine =", x)
    else:
        if(c==0):
            print("racine X= R")
        else:
            print("pas de solution")

