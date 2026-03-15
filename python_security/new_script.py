#form
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from caesar_utility import *

#fenéter
fen=Tk()
fen.title('cripty on kaysar')
fen.geometry('500x600')
fen.resizable(False,False)


#style
s='arial 19 bold'

#les fonction
def encrypt():
    #Enfin, merci d'avoir écouté
    #1$0+$?>²27!+>4'-;5+7>.!5%£.
   text=tx.get()
   # text1=text.replace('E','1').replace('n','$').replace('f','0').replace('i','+').replace(
   #     ',','?').replace(' ','>').replace('m','²').replace('e','2').replace('r','7').replace('c','!').replace('d','4').replace\
   #     ('a','-').replace('v',';').replace('o','5').replace('é','.').replace('u','%').replace('t','£')
   # tx1.set(text1)

   text1 = text.replace('1', 'E').replace('$', 'n').replace('0', 'f').replace('+', 'i').replace(
       '?', ',').replace('>', ' ').replace('²', 'm').replace('2', 'e').replace('7', 'r').replace('!', 'c').replace('4',
                                                                                                                   'd').replace \
       ('-', 'a').replace(';', 'v').replace('5', 'o').replace('.', 'é').replace('%', 'u').replace('£', 't')
   tx1.set(text1)



#canva
c1=Canvas(bg='black').place(x=0,y=0,width=500,height=600)

#StringVar
tx=StringVar()
tx1=StringVar()

#Entry
E1=Entry(fen,font=s,bg='white',fg='black',textvariable=tx).place(x=50,y=50 ,width=400,height=60)
E2=Entry(fen,font=s,bg='#E7E5E5',fg='black',textvariable=tx1).place(x=50,y=250 ,width=400,height=300)


#button
b1=Button(fen,command=encrypt,fg='orange',bg='#9C9C9C',text="Encryption",font=s).place(x=150,y=150 ,width=200,height=50)











fen.mainloop()
