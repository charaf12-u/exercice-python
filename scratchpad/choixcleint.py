from client import *
def chercher():
    while(True):
        pos=-1
        num = int(input("donner un num par chercher"))
        for i in range(0, len(t)):
            if (num == t[i].num):
                pos = i
                return pos
t=[]
while(True):
    print("0 sortir")
    print("1 ajouter")
    print("2 cherch")
    print("3 afficher")
    print("4 supprimer")
    print("5 modifier")
    while (True):
        try:
            choix = int(input("donner le choix"))
            if (choix <= 5 and choix >= 0):

                break

        except:
            print("erour donner un choix")
    if(choix==0):
        break
    if(choix==1):
        num=int(input("donner le num"))
        nom = input("donner le nom")
        salair = int(input("donner le salair"))
        c=client(num,nom,salair)
        t.append(c)
    if(choix==2):
        pos=chercher()
        if(choix==-1):
            print("no exist")
        else:
            print("exist")
    if (choix == 3):
        for x in t:
            print(x)
    if (choix == 4):
        pos = chercher()
        if (choix == -1):
            print("no exist")
        else:
            print("exist")
            t.pop(pos)
    if (choix == 5):
        pos = chercher()
        if (choix == -1):
            print("no exist")
        else:
            print("exist")
            nvNOM=input("donner nouveu nom")
            nvNUM=int(input("donner neuveu num"))
            nvsalair=int(input("donner neuveu salair"))
            t[pos].num=nvNUM
            t[pos].nom = nvNOM
            t[pos].setSalaire(nvsalair)