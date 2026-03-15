n=int(input("donnez le nomber de joueurs"))
print("donnez le nomber de buts marqueé par 1 joueur")
nb_buts=int(input())
pos=1
max=nb_buts
for i in range(2,n+1):
    print("donnez le nomber de buts marqueé par ",i,"joueur")
    nb_buts=int(input())
    if(nb_buts>=max):
        pos=i
        max=nb_buts
print("le max est ",max,"est marquuee par le joueur : ",pos)