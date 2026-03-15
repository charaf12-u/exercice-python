#q1
from exept import *
class actor:
    #q2
    nbObjet=0
   # def __init__(self,num,nom,nb):
    #    self.num=num
    #    self.nom=nom
    #    self.__nb=nb
        #q3
    #    actor.nbObjet=actor.nbObjet+1
    #q4
    def __str__(self):
        return f"({self.num}) {self.nom} ({self.__nb})"
    #q5
    def getAge(self):
        return self.__nb
    def setAge(self,x):
        self.__nb=x
    #q6
    def augmenter(self,p):
        self.__nb=self.__nb+(p/100)*self.__nb
    #q7
    def __init__(self,num,nom,nb):
        try:
            if(nb>=4):
                 self.num = num
                 self.nom = nom
                 self.__nb = nb
                 actor.nbObjet = actor.nbObjet + 1
            else:
                raise nbobjet ("errour nb")
        except nbobjet:
            print("nb <4")
    #q9


