#for i in range (1,11):
#    print("bonjour")



#print("donner la valeur de n")
#n=int(input())
#for i in range(1,13):
   # print(i,"*",n,"=",i*n)


#import math
#print("donner n")
#n=int(input())
#s=0
#for i in range(1,n+1):
#    s=s+i/(i+math.sqrt(2+(i*i)))
#print("s=",s)


#print("donner n")
#n=int(input())
#for i in range(1,n+1):
#    print("donnez la",i,"nomber")
 #   a=int(input())
 #   if(a>=0):
 #       print(a,"positif")
 #   else:
 #       print(a,"négatif")



#for i in range(10,1,-2):
#     print("i=",i)



#for i in range(1,11):
#    print("voici la taple de muetpde de",i)
 #   for j in range(1, 11):
 #       print(i,"*",j,"=",i*j)
 #   print("**********")



#print("donez la nomber de module")
#n=int(input())
#s=0
#m=0
#for i in range(1,n+1):
 #   print("donnez la",i,"note")
 #   note=float(input())
#
 #   print("donnez la", i, "ceuficion")
  #  c = float(input())
#    m=m+note*c
#    s=s+c
#m=m/s
#print("la moyene de modul=",m)
#if(m<10):
#    print("redouble")
#else:
#    if(m<12):
 #       print("passable")
#    elif(m<14):
#        print("A bien")
#    elif(m<16):
#        print("bien")
 #   else:
 #       print("T bien")


import math
#print("donnez n")
#n=int(input())
#s=0
#for i in range(1,n+1):
#   s=s+1/(math.cos(i*i))
#print("s=",s)



#print("donnez n")
#n=int(input())
#for i in range(1,n+1):
#    print("donner la",i,"nomber")
 #   a=int(input())
 #   if(a%2==0):
 #       print(a,"est pair")
 #   else:
 #       print(a,"est non pair")


#print("donnez le nomber de modul")
#n=int(input())
#cp=0
#for i in range(1,n+1):
#     print("donnez la note de la ",i,"modul")
#     note=float(input())
#     if(note>=10):
#         cp=cp+1
#print("le nomber de module validé",cp)



#print("donnez n")
#n=int(input())
#cp=0
#ci=0
#for i in range(1,n+1):
#    print("donnez la",i,"nomber")
#    a=int(input())
#    if(a%2==0):
#        cp=cp+1
#    if (a % 2 != 0):
#        ci=ci+1
#print("nomber de la pair=",cp)
#print("nomber de étend impaire=",ci)



#print("donnez n")
#n=int(input())
#for i in range(1,n+1):
#    if(n%i==0):
#        print(i,"diver",n)
#    else:
#        print(i,"no diver",n)


#print("donnez n")
#n=int(input())
#s=0
#for i in range(1,n+1):
#    if (n % i == 0):
#        s=s+i
#if(n==s):
#    print(n,"magic")
#else:
#    print(n,"no magic")


#for n in range(2,5000000000000000000):
#    s=0
#    for i in range(1,n):
 #       if(n%i==0):
#            s=s+i
#    if(s==n):
#        print(n,"cet magic")

#écrir python qui lire les nom de un joueur et les n but marqué
#puis affich le total but marqué et affich les nom du joueur
#marqué a >7 but et comptes les joueur marqé >3



#nj=int(input("donnez nomber de joueur"))
#s=0
#cp=0
#for i in range(1,nj+1):
#    print("donner le nom de",i,"joueur")
 #   nom=str(input())
#    print("donner le nomber but de", i, "joueur")
#    nb=int(input())
#    s=s+nb
#print("total de but =",s)
#cp=cp+nb
#if(cp>=7):
#    print("le nom",nom)


#print("1:solition AR")
#print("2:solition FR")
#print("3:sortir")
#print("votre achoix")
#choix=int(input())
#while(choix!=0):
#    if(choix==1):
#        print("السلام")
#    if(choix==2):
#        print("salam")
#    print("1:solition AR")
#    print("2:")
#    print("3:sortir")
 #   print("votre achoix")
#    choix=int(input())


#print("1:la some type")
#print("2:la diff type")
#print("3:molphicah type")
#print("4:la division type")
#print("5:sortir")
#print("votre achoix")
#choix=int(input())
#while(choix!=0):
#    if(choix==1):
#        print("donez a")
#        a=int(input())
#        print("donez b")
#        b=int(input())
#        s=a+b
#        print("s=",s)
#    if(choix==2):
#        print("donez a")
#        a = int(input())
#        print("donez b")
#        b = int(input())
#        s = a - b
#        print("s=", s)
#    if (choix == 3):
#        print("donez a")
#        a = int(input())
#        print("donez b")
#        b = int(input())
#        s = a * b
#        print("s=", s)
#    if (choix == 4):
#        print("donez a")
#        a = int(input())
#        print("donez b")
#        b = int(input())
#        s = a / b
#        print("s=", s)
#    print("1:la some type")
#    print("2:la diff type")
#    print("3:molphicah type")
#    print("4:la division type")
 #   print("5:sortir")
#    print("votre achoix")
#    choix = int(input())



n=int(input("donnez le nomber de note"))
s=0
m=0
i=1
while(i<=n):
    note=float(input("donnez la note"))
    coeficion=int(input("donner la coefition"))
    s=s+note*coeficion
    m=m+coeficion
    i = i + 1
    moy=s/m
print("la moyenne c'est",moy)



t=[14,17,"a","hello",133.2,132]
print(t[2:6])