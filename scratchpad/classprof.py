class Prof:
    def __init__(self,ref,nom):
        self.__ref=ref
        self.__nom=nom

    def getREF(self):
        return self.__ref
    def setREF(self,x):
        self.__ref=x

    def getNOM(self):
        return self.__nom
    def setNOM(self,x):
        self.__nom=x