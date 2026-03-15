####ex1####
print("****_-1-_****")
print("donner une chain")
ch=input()
l=len(ch)
print("loyen=",l)
def lfonction(ch):
    l=len(ch)
    return l
print("donner une chaine")
ch=input()
res=lfonction(ch)
print("loyon",res)


###ex2###
print("****_-2-_****")
print("donner une chaine")
l=len(ch)
if(l==0):
    print("chaine vide")
else:
    for i in range(0,l):
        print(ch[i])
ch1=""
for i in range(0,l):
    ch1=ch1+ch[l-1-i]
if(ch1==ch):
    print("oui palontrene")
else:
    print("non palontrene")


###ex3###
print("****_-3-_****")
lv=["a","o","i","y","u","e","A","O","I","Y","U","E"]
print("donner une chaine")
ch=input()
cp=0
l=len(ch)
for i in range(0,l):
    if ch[i] in lv:
        cp=cp+1
print("nb de vos",cp)


###ex4###
print("****_-4-_****")
print("donner une phraze")
ph=input()
l=ph.split("#")
for i in range(0,len(l)):
    print(l[i])


###ex5###
print("****_-5-_****")
def testBinaire(ch):
    lis=["o","1"]
    res=True
    if(len(ch)==0):
        res=False
    else:
        for i in range(0,len(ch)==0):
            if ch[i] in lis:
                res=True
            else:
                res=False
                break
        return res
print("donner une chaine binaire")
ch=input()
res=testBinaire(ch)
if(res==True):
    print("OUI c'est chaine binair")
else:
    print("no binaire")

###ex6###
print("****_-6-_****")
import math
while(1==1):
    print("donnez ch")
    ch=input()
    res=testBinaire(ch)
    if(res==True):
        break
s=0
for i in range(0,len(ch)):
    s=s+int(ch[l-1-i])*math.pow(2,i)
print(s)
