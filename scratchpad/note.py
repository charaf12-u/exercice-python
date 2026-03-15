print("donner n1")
n1=float(input())
print("donner n2")
n2=float(input())
print("donner c1")
c1=float(input())
print("donner c2")
c2=float(input())
m=(n1*c1+n2*c2)/(c1+c2)
print("la moyenne c'est",m)
if(m<10):
    print("redouble")
else:
    if(m<12):
        print("passable")
    elif(m<14):
        print("A bien")
    elif(m<16):
        print("bien")
    else:
        print("T bien")