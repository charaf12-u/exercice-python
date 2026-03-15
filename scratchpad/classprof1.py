class Prof:
    def __init__(self,ref,nom):
        self.__ref=ref
        self.__nom=nom

    def getREF(self):
        return self.__ref
    def setREF(self,value):
        self.__ref=value

    def getNOM(self):
        return self.__nom
    def setNOM(self,value):
        self.__nom=value