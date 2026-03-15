#les from
from tkinter import *
from tkinter import messagebox
from hash_utility import *


#fenétre
fen=Tk()
fen.geometry("600x600")
fen.resizable(False,False)


#list
list=[]


#les fonction
def chiffr():
    pass





#style
s="{arial} 20 bold"
s1="centenur 20 bold"


#canvas
c=Canvas(fen,bg="black").place(x=0,y=0,width=600,height=600)
C1=Canvas(fen,bg="red").place(x=390,y=0,width=10,height=600)
C2=Canvas(fen,bg="white").place(x=400,y=0,width=200,height=600)


#label
l=Label(fen,font=s,text="taper un chain",bg="black",fg="orange")
l.place(x=20,y=20,)


#stringvar
tx=StringVar()


#entry
e=Entry(fen,font=s,textvariable=tx).place(x=20,y=80,width=350,height=50)


#buton
b=Button(fen,command=chiffr,borderwidth=4,font=s1,text="chiffrer")
b.place(x=120,y=160,width=150,height=40)


#listbox
li=Listbox(fen,font="bold")
li.place(x=20,y=240,width=350,height=300)



















fen.mainloop()
