class program:
    list=[]
    @classmethod
    def rechercher_pos(cls,num):
        pos=-1
        if(len(list)>0):
            for i in range(0,len(list)):
                if(list[i].get_num==num):
                    pos=i
        return pos
