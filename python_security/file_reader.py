class read:
    def readlist(self,x):
        with open(x, "r") as OR:
            return OR.readlines()
#rr=read()
#alltext=rr.readlist("x.txt")
#for i in alltext:
#    i=i.rstrip("\n")
#    print(i)