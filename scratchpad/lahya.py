#n=float(input("donnez n"))
#i=1
#while(1==1):
 #   if(i<=n+1):
 #       i=i+1
 #       print("bonjour")



#i=0
#while(1==1):
#    print("bonjour")
#    i=i+1
#    if(i==5):
#        break


#i=1
#s=0
#while(1==1):
#    s=s+(1/i)
#    print("la somme =",s)
#    i = i + 1
#    if(i==8):
#        break


#i=1
#s=0
#b=0
#while(1==1):
#    note=float(input("donez la note",))
#    c=int(input("donez la ceufition",))
#    i = i + 1
#    b=b+note*c
#    s=s+c
#    m=b/s
#    if(i==8):
#        break
#print("la moiyane c'est", m)



#t=[1,2,14,17,18]
#tab=[1,True,"hello",3.14]
#print("list t=",t)
#print("list tab=",tab)


#list=["omar","charaf","mohamed"]
#print("le nam=",list[1])


#t=["x","charaf",14,17]
#print("t=",t)
#t[1]="charaf soubi"
#print("the now list=",t)


#t=["x","charaf",14,17]
#print("t=",t[1])
#t[1]="charaf soubi"
#print("the now list=",t[1])


#t=["x","z","abc",14,17]
#for x in t:
#    print(x)

#import math
#tab=[1,12,17,math.sqrt(12),"charaf"]
#nb=len(tab)
#for i in range(0,nb):
#    print(tab[i])



#t=[14,17,"a","hello",133.2,132]
#print(t[2:6])


#list=["cg","charaf","ali"]
#print("the bedlist=",list)
#list.append("nono")
#print("the bedlist=",list)


#list=["cg","charaf","ali"]
#print("the bedlist=",list)
#list.remove("ali")
#print("the bedlist=",list)



#list=["cg","charaf","ali"]
#print("the bedlist=",list)
#list.append("nono")
#print("the bedlist=",list)
#list.append("soubi")
#print("the bedlist=",list)
#list.remove("ali")
#print("the bedlist=",list)
#list.append("mohamed")
#print(list)
#list.pop()
#print(list)


#list=["cg","charaf","ali"]
#print("the bedlist=",list)
#list.append("mohamed")
#print(list)



#list=["cg","charaf","ali"]
#print("the bedlist=",list)
#list.pop()
#print(list)



#t=[]
#while(1==1):    #  or   while(True):
#     print("*****")
#     print("choix=1:Ajouter un nouveu élément")
#     print("choix=2:Lister les élément")
#     print("choix=3:Cherche un élément")
#     print("choix=4:Supprimer un élément")
#     print("choix=0:Sortir")
#     print("entrer votre choix")
#     choix=int(input())
#     if(choix==0):
#          print("mrc")
#          break
#    if(choix==1):
#          print("donner le nom")
#          nom=input()
#         t.append(nom)
#    if(choix==2):
#          nb=len(t)
#          for i in range(0,nb):
#              print("ele in dice",i+1,"=",t[i])
#     if(choix==3):
#          print("donner le nom que.v.v.c")
#          nom=input()
#          trouve=0
#          nb=len(t)
#         for i in range(0,nb):
#               if(t[i]==nom):
#                    trouve=1
#                    print("exist")
#          if(trouve==0):
#               print("nom exist")
#     if (choix == 4):
#          print("donner le nom que.v.v.c")
#          nom = input()
#          trouve = 0
#          nb = len(t)
#          for i in range(0, nb):
#              if (t[i] == nom):
#                  trouve = 1
#          if (trouve == 0):
#             print("affecher no exist")
#          else:
#              t.remove(nom)
#     if(choix==5):
#          print("donner nom q.v.v.modifier")
#         nom=input()
#         pos=1
#          nb=len(t)
#          for i in range(0,nb):
#              if(t[i]==nom):
#                   pos=i
#          if(pos==-1):
#              print("no exit")
#          else:
#              print("donner nouveu nom")
#              newn=input()
#              t[pos]=newn
#     else:
#         print("le choix no trouver")




##bach t9bl rir al a3dad ##
#while(1==1):
#    print("donner n")
#    ch=input()
#    if(ch.isnumeric()==True):
#        n=int(ch)
#        break
##or##
#while(1==1):
#    try:
#        print("donnez n")
#        n=int(input())
#        if(n>=0):
#            break
#    except:
#        print("try again")



## les structurs ##
#listMed=[]
#while(1==1):
#    print("1:ajouter")
#    print("2:afficher le mds")
#    print("3:recherch par ref")
#    print("4:afficher cepture de stock")
#    print("5:supprimer")
#    print("6:modifier")
#    print("0:sortir")

#    choix=int(input("taper le choix"))
#    if(choix==0):
#        print("merc")
#       break
#    if(choix==1):
#        md={"ref":1,
#            "numM":"vitamin C",
#            "qts":150,
#            "nCas":11,
#        }
#        refm=int(input("donner refmd"))
#        numM=input("donner numMD")
#        qts = int(input("donner le qt stock"))
#        nCas = input("donner Numéro case")
#        md["ref"]=refm
#        md["numM"] = numM
#        md["qts"] = qts
#        md["nCas"] = nCas
#        listMed.append(md)
#    if(choix==2):
#        for i in range(0,len(listMed)):
#            print(",---***---,")
#            print("ref=",listMed[i]["ref"])
#            print("numM=", listMed[i]["numM"])
#            print("qts=", listMed[i]["qts"])
#            print("nCas=", listMed[i]["nCas"])

#   if(choix==3):
#        pos=-1
#        print("donnez ref medicamon chercher")
#       ref=int(input())
#        for i in range(0,len(listMed)):
#           if(listMed[i]["ref"]==ref):
#                 pos=i
#                 if(pos==-1):
#                    print("not exist")
#                 else:
#                    print("exist")
#                    print(":---***---:")

#    if (choix == 4):
#        pos = -1
#        print("donnez ref medicamon chercher")
#        ref = int(input())
#        for i in range(0, len(listMed)):
#            if (listMed[i]["ref"] == ref):
#                pos = i
#                if (pos == -1):
#                    print("not exist")
#                else:
#                    print("exist")
#                    print("exist des la case", listMed[pos]["qts"])
#                    print("*---£*£---*")

#    if (choix == 5):
#        pos = -1
#        print("donnez ref medicamon chercher")
#        ref = int(input())
#        for i in range(0, len(listMed)):
#            if (listMed[i]["ref"] == ref):
#               pos = i
#                if (pos == -1):
#                    print("not exist")
#                else:
#                    print("exist")
#                    listMed.pop(pos)
#                    print("ok supprimer")
#                    print("---*$*---")

#    if (choix == 6):
#        pos = -1
#        print("donnez ref medicamon chercher")
#        ref = int(input())
#        for i in range(0, len(listMed)):
#            if (listMed[i]["ref"] == ref):
#               pos = i
#                if (pos == -1):
#                    print("not exist")
#                else:
#                    print("exist")
#                    nvstock = int(input("donner le nouveau stock"))
#                    listMed[pos]["qts"] = nvstock
#                    nvref = int(input("donner le nouveau ref"))
#                    listMed[pos]["ref"] = nvref
#                    nvcase = int(input("donner le nouveau case"))
#                    listMed[pos]["nCas"] = nvcase
#                    nvnum = input("donner le nouveau num")
#                    listMed[pos]["numM"] = nvnum
#                    print("*---***---*")


###procedurer###
def salutationAR():
    print("السلام")
def salutationFR():
    print("salut")
def salutationANG():
    print("hello")
salutationAR()
salutationFR()
salutationANG()

###produi calcules la somme ,division,multiplication###
def somme():
    a=int(input("donner a"))
    b = int(input("donner b"))
    s=a+b
    print("la somme=",s)
def division():
    a = int(input("donner a"))
    b = int(input("donner b"))
    if(b==0):
        print("impossiple")
    else:
        res=a/b
def multiplication():
    a = int(input("donner a"))
    b = int(input("donner b"))
    m = a * b
    print("la somme=", m)
somme()
division()
multiplication()

###produi qui affich le max de deux nombre###
print("--**--")
def maxnum(a,b):
    if(a>=b):
        max=a
    else:
        max=b
    print("max=",max)
a=int(input("donner a"))
b = int(input("donner b"))
maxnum(a,b)



###fonction###
    ##1##
def somme(a,b):
    res=a+b
    return res
def multiplication(a,b):
    res=a*b
    return res
a = int(input("donner a"))
b = int(input("donner b"))
res=somme(a,b)
print("resulta=",res)
res1=multiplication(a,b)
print("resulta=",res1)

    ##2##
def fonctionnel(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s
n=int(input("donnez n"))
res=fonctionnel(n)
print("fonctionnel=",res)