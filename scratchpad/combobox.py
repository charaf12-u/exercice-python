from tkinter import *
from tkinter import ttk
fen=Tk()
fen.geometry("550x470")
fen.title("Calcules")
ph=PhotoImage(file="15361.png")
myStyle="{arial} 21 bold"
fen.iconphoto(False,ph)
a=0
b=0
list=["somme","diff","div","mul"]

def afficher():
    global a
    global b
    for i in range(0,len(list)):
        if("somme"==ld.get()):
            a=t1.get()
            b=t2.get()
            s=int(a)+int(b)
            t3.set(s)
        if ("diff" == ld.get()):
            a = t1.get()
            b = t2.get()
            s = int(a) - int(b)
            t3.set(s)
        if ("div" == ld.get()):
            a = t1.get()
            b = t2.get()
            s = int(a) * int(b)
            t3.set(s)
        if ("mul" == ld.get()):
            a = t1.get()
            b = t2.get()
            s = int(a) / int(b)
            t3.set(s)
t1=StringVar()
t2=StringVar()
t3=StringVar()
l=Canvas(fen,bg="black").place(x=0,y=0,width=600,height=600)
l1=Label(fen,fg="white",font=myStyle,text="entre a :",bg="black").place(x=50,y=20)
e1=Entry(fen,fg="black",font=myStyle,textvariable=t1).place(x=170,y=20,width=300,height=45)
l2=Label(fen,fg="white",font=myStyle,text="entre b :",bg="black").place(x=50,y=70)
e2=Entry(fen,fg="black",font=myStyle,textvariable=t2).place(x=170,y=70,width=300,height=45)
l3=Label(fen,fg="white",font=myStyle,text="choisir l'operation :",bg="black").place(x=50,y=170)
ld=ttk.Combobox(fen,font=myStyle,value=list)
ld.place(x=50,y=210,width=260)
ld.current(0)
ld.bind("<<ComboxSelected>>")
b1=Button(fen,command=afficher,text="afficher",bg="orange",fg="black",font=myStyle,borderwidth=6).place(x=50,y=300,width=150,height=40)
l4=Label(fen,fg="white",font=myStyle,text="resultat ",bg="black").place(x=50,y=350)
e3=Entry(fen,fg="blue",bg="red",font=myStyle,textvariable=t3).place(x=170,y=350,width=300,height=45)







fen.mainloop()