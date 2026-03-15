class conducteur:
    def __init__(self,NC,NomC,Adr,nbAvirtissment,Nblan):
        self.__NC=NC
        self.__NomC=NomC
        self.__Adr=Adr
        self.__nbAvirtissment=nbAvirtissment
        self.__Nblan=Nblan

    def getNC(self):
        return self.__NC
    def getNomC(self):
        return self.__NomC
    def getAdr(self):
        return self.__Adr
    def getNBA(self):
        return self.__nbAvirtissment
    def getNbl(self):
        return self.__Nblan

    def setNc(self,x):
        self.__NC=x
    def setNomC(self,x):
        self.__NomC=x
    def setAdr(self,x):
        self.__Adr=x
    def setNBA(self,x):
        self.__nbAvirtissment=x
    def setNbl(self,x):
        self.__Nblan=x
