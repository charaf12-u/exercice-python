##1:lire un chain puis calculer la langeur##
print("***-_1_-***")
ch="bonjour"
ch1=input("donner un chain")
l1=len(ch1)
print(l1)

##2:lire un chain et afficher les caractéres voyelle##
print("***-_2_-***")
cV=["a","e","y","u","i","o","A","E","Y","U","I","O"]
ch=input("donner un caractér")
cp=0
for i in range(0,len(ch)):
    if ch[i] in cV:
       cp=cp+1
print("les caractéres voyelle c'est",cp)


##3:lire deux chain ch1 et ch2 puis afficher contaténationde ce deux chain##
print("***-_3_-***")
ch1=input("donnez le nome et prénon")
ch2=int(input("donner un lage"))
print("my name is",ch1,", my old are you",ch2)

##4:reme exercice avec les fonction##
print("***-_4_-***")
def CH1(ch1):
    ch1=input("donnez le nome et prénon")
    return ch1
def CH2(ch2):
    ch2=input("donner un lage")
    return ch2
res1=CH1(ch1)
res2=CH2(ch2)
print("my name is",res1,",my old ar you",res2)

##5##
print("***-_5_-***")
ch1=input("donnez la phraze")
ch2 = input("donner la chain")
for i in range(0,len(ch1)):
    if ch2 in ch1:
        cp=ch1.count(ch2)
print("le nomber de rébitition c'est",cp)


##6##
print("***-_6_-***")
n=int(input("donnez le nomber des nombres"))
for i in range(0,n):
    a=float(input("donner le",i,"nomber":))



##12##
    t = []
    while (True):
        print("0:sortir")
        print("1:ajouter")
        print("2:lister le tout")
        print("3:chercher")
        print("4:lister le stokag")
        print("5:supprimer")
        print("6:modifier")
        print("7:lister par ref")
        choix = int(input("taper le choix"))

        if (choix == 0):
            print("mrc")
            break
        if (choix == 1):
            md = {
                "ref": 3,
                "nom": "vitamin C",
                "stok": 43,
                "ncas": 1
            }
            REF = int(input("donner le ref"))
            NOM = input("donner le NOM")
            STOK = int(input("donner le STOK"))
            NCAS = int(input("donner le NCAS"))
            md["ref"] = REF
            md["nom"] = NOM
            md["stok"] = STOK
            md["ncas"] = NCAS
            t.append(md)
        if (choix == 2):
            print(t)
        if (choix == 7):
            ref = input("donner le ref par recherch")
            pos = -1
            for i in range(0, len(t)):
                if (pos == -1):
                    pos = i
                    if (pos == -1):
                        print("no exist")
                    else:
                        print("ref=", t[pos]["ref"])
                        print("nom=", t[pos]["nom"])
                        print("stok=", t[pos]["stok"])
                        print("ncaz=", t[pos]["ncas"])
        if (choix == 3):
            ref = input("donner le ref par recherch")
            pos = -1
            for i in range(0, len(t)):
                if (pos == -1):
                    pos = i
                    if (pos == -1):
                        print("no exist")
                    else:
                        print("exist")
        if (choix == 4):
            ref = input("donner le ref par recherch")
            pos = -1
            for i in range(0, len(t)):
                if (pos == -1):
                    pos = i
                    if (pos == -1):
                        print("no exist")
                    else:
                        print("stok=", t[pos]["stok"])
        if (choix == 5):
            ref = input("donner le ref par recherch")
            pos = -1
            for i in range(0, len(t)):
                if (pos == -1):
                    pos = i
                    if (pos == -1):
                        print("no exist")
                    else:
                        t.pop(pos)
        if (choix == 6):
            ref = input("donner le ref par recherch")
            pos = -1
            for i in range(0, len(t)):
                if (pos == -1):
                    pos = i
                    if (pos == -1):
                        print("no exist")
                    else:
                        Ref = int(input("donner le ref"))
                        Nom = input("donner le ref")
                        Stok = int(input("donner le ref"))
                        Ncas = int(input("donner le ref"))
                        t[pos]["ref"] = Ref
                        t[pos]["nom"] = Nom
                        t[pos]["stok"] = Stok
                        t[pos]["ncas"] = Ncas
