from actor import *
t=[]
while(True):
    print("1 sortir")
    print("2 ajouter")
    print("3 lister")
    print("4 chercher")
    print("5 supprimer")
    print("6 modifier")
    choix = int(input("donner le choix"))
    if(choix==1):
        break
    if(choix==2):
        numA = int(input("donner le num"))
        nomA = input("donner le nom")
        nbA = int(input("donner le nb"))
        s = actor(numA, nomA, nbA)
        t.append(s)
    if(choix==4):
        num=int(input("donner le num par chercher"))
        pos=-1
        for i in range(0,len(t)):
            if(num==t[i]):
                pos=i
                if(pos==-1):
                    print("no exist")
                else:
                    print("exist")
    if(choix==3):
        num = int(input("donner le num par chercher"))
        pos = -1
        for i in range(0, len(t)):
            if (num == t[i]):
                pos = i
                if (pos == -1):
                    print("no exist")
                else:
                    print("exist")
                    print(t[pos])
    if(choix==5):
        num = int(input("donner le num par chercher"))
        pos = -1
        for i in range(0, len(t)):
            if (num == t[i]):
                pos = i
                if (pos == -1):
                    print("no exist")
                else:
                    print("exist")
                    t.pop(pos)
    if(choix==6):
        num = int(input("donner le num par chercher"))
        pos = -1
        for i in range(0, len(t)):
            if (num == t[i]):
                pos = i
                if(pos == -1):
                    print ("no exist")
                else:
                    print("exist")
                    NumA = int(input("donner le num"))
                    NomA = input("donner le nom")
                    NbA = int(input("donner le nb"))
                    actor.num = NumA
                    actor.nom = NomA
                    actor.nb = NbA
