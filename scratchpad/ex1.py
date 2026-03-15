class client:
    def __init__(self,numC,nomC,chiffA):
        self.__numC=numC
        self.__nomC = nomC
        self.__chiffA = chiffA
    def __str__(self):
        return f"({self.numC}) {self.nomC} ({self.chiffA})"
    def getNumc(self):
       return self.__numC
    def getNomc(self):
       return self.__nomC
    def getChiffA(self):
       return self.__chiffA
    def setNumc(self,x):
       self.__numC=x
    def setNomc(self,x):
       self.__nomC=x
    def setChiffA(self,x):
       self.__chiffA=x