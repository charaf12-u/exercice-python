from tajriba import *
pc1=pc(1,"dell")
pc2=pc(5,"le novo")
print("le nomber de pc c'est",pc.nb)


from tajriba import *
prof1=prof(1,"dell",44)
prof2=prof(5,"le novo",19)
print("le nomber de pc c'est",prof.nb)

#q8
from actor import *
numA=int(input("donner le num"))
nomA=input("donner le nom")
nbA=int(input("donner le nb"))
s=actor(numA,nomA,nbA)
print("le nb de objet",actor.nbObjet)
print("les num",s.num)
print("les nom",s.nom)
print(s)
