class pc:
    nb=0
    def __init__(self,ref,marque):
        self.ref=ref
        self.marque=marque
        pc.nb=pc.nb+1


from exept import *
class prof :
    nb = 0
    def __init__(self,num,nom,age):
        try:
            if(age>=18):
                self.num = num
                self.nom = nom
                self.__age = age
                pc.nb = pc.nb + 1
            else:
                raise exage("erour age")
        except exage:
            print("age must be >=18")



