class salairi:
    def __init__(self,num,nom,salaire):
        self.num=num
        self.nom=nom
        self.__salaire=salaire
    def getSAL(self):
        return self.__salaire
    def setSAL(self,x):
        self.__salaire=x