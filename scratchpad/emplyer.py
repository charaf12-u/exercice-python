class employer:
    def __init__(self,num,nom):
        self.__num=num
        self.__nom=nom
    def get_num(self):
        return self.__num
    def get_nom(self):
        return self.__nom
    def set_num(self,val):
        self.__num=val
    def set_nom(self,val):
        self.__nom=val