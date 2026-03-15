####1####
print("****_1_****")
a=int(input("donnez le nomber a"))
b=int(input("donnez le nomber b"))
s=a*b
if(s==0):
    print("impossipl")
else:
    som=a/(s)
    print("la somme =",som)




####2####
print("****_2_****")
a=int(input("donnez le nomber a"))
b=int(input("donnez le nomber b"))
c=int(input("donnez le nomber c"))
s=a*a
m=b*b
l=c*c
if(s==(m+l)):
    print("motalt 9aim zawiya")
if(m==(s+l)):
    print("motalt 9aim zawiya")
if(l==(m+s)):
    print("motalt 9aim zawiya")
else:
    print("motalt laysa 9aim zawiya")




####3####
print("****_3_****")
n=int(input("donner le nomber n"))
s=0
i=1
for i in range(0,10):
    i=i+1
    s=s+i*n
    print(i,"*",n,"=",i*n)




print("***_4_***")
s=0
i=0
n = int(input("donner n"))
while(1==1):

    if(n>=0):
        break
    else:
        n=int(input("envoiyer n"))
for i in range(1,n+1):
    s=s+i/(1+i)
print("s=",s)


####5####
print("***_5_***")
décimal=int(input("donner un nember décimal"))
binair=" "
while (décimal>0):
    décimal = décimal // 2
    binair=str(décimal%2)+binair
print("binair =",binair)



####6####
print("*****_-6_-*****")
list=[]
while(True):
    print("1:sortir")
    print("2:ajouter" )
    print("3:afficher")
    print("4:la moyenne")
    choix=int(input("donner le choix"))
    if(choix==1):
        print("mrc")
        break

    if(choix==2):
        n=int(input("donner le nomber de note"))
        for i in range(1,n+1):
            if(i<=n):
                note=int(input("donnez la note"))
                list.append(note)
                print(list)
    print("*****_-_-*****")

    if(choix==3):
        nb=0
        for i in range(0, len(list)):
            if(list[i]>=10 and list[i]<12):
                nb=nb+1
        print("le nomberb de étudiants ayant la mention passable=",nb)
    print("*****_-_-*****")

    if(choix==4):
        g=0
        for i in range(0,len(list)):
            g=g+list[i]
        s=g/len(list)
        print("la moyenne de la class=",s)


####7####
print("***_7_***")
d=int(input("give positif value"))
for i in range(1,d+1):
    for j in range(i):
        print('*',end='')
    print("\n")



####8####
print("***_8_***")
list=[]
list.append("charaf")
list.append("RCA")
list.append(13)
list.append(12)
rech=input("ecrire un element :")
if rech in list:
    print("l'element exist dans la list")
else:
    print("l'element non exist dans la list")