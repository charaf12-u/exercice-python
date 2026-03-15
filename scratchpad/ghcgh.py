from tajriba import stagair
num=int(input("donner le num"))
nom=input("donner le nom")
dateDeNaissance=int(input("donner le dateDeNaissance"))
note=int(input("donner le note"))
l=stagair(num,nom,dateDeNaissance,note)
#print(l)
l.augenter()
print(l)