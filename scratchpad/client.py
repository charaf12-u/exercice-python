class client:
    def __init__(self,num,nom,salair):
        self.num=num
        self.nom = nom
        self.__salair=salair
    def __str__(self):
        return f"({self.num}) {self.nom} ({self.__salair})"
    def aficher(self):
        print("le num =",self.num)
        print("le nom =", self.nom)
        print("le salair =", self.__salair)
    def getSalaire(self):
        return self.__salair
    def setSalaire(self,value):
        self.__salair=value
    def augmenter(self):
        self.__salair=self.__salair+(10/100)*self.__salair

