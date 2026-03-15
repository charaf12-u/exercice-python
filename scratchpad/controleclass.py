class Client:
    def __init__(self, reference, name, chiffA, city, gender, level):
        self.reference = reference
        self.name = name
        self.__chiffA = chiffA
        self.city = city
        self.gender = gender
        self.level = level
    def get_chA(self):
        return self.__chiffA
    def set_chA(self,value):
        self.__chiffA=value