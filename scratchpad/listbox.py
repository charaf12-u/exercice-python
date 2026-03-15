from employe import *
from tkinter import *
from tkinter import messagebox
list=[]
fen=Tk()
fen.geometry("520x490")
myStyle="{arial} 21 bold"
style="century 21 bold"
fen.title("list")
fen.resizable(False,False)
f=Canvas(fen,bg="black").place(x=0,y=0,width=600,height=600)
t1=StringVar()
t2=StringVar()
t3=StringVar()
def defCerche():
    pos=-1
    num=t1.get()
    for i in range(0,len(list)):
        if(list[i].num==num):
            pos=i
    return pos
def ajouter():
    num=t1.get()
    nom=t2.get()
    lm=employe(num,nom)
    list.append(lm)
def chercher():
    pos=defCerche()
    if(pos==-1):
        messagebox.showinfo("no exist")
           # msg = "no exist"
           # lB.insert(END, msg)
    else:
        #msg = "exist"
        #lB.insert(END, msg)
        messagebox.showinfo("exist")
        t1.set(list[pos].num)
        t2.set(list[pos].nom)
        #numE=list[pos].num
        #nomE = list[pos].nom
        #s="le num :",numE
       # s1=" le nom :",nomE
        #lB.insert(END,s,s1)
def vider():
    t1.set("")
    t2.set("")
def lister():
    for i in range(0,len(list)):
        msg=str(list[i].num)+"#"+str(list[i].nom)
        lB.insert(END,msg)

def modifier():
    pos = defCerche()
    if (pos == -1):
        #msg = "no exist"
        #lB.insert(END, msg)
        messagebox.showinfo("no exist")

    else:
        messagebox.showinfo("exist")
        #lB.insert(END,msg, ms)
        list[pos].num=t1.get()
        list[pos].nom=t2.get()
def suprimer():
    pos = defCerche()
    if (pos == -1):
        #msg = "no exist"
        #lB.insert(END, msg)
        messagebox.showinfo("no exist")
    else:
        #msg = "exist"
        #lB.insert(END, msg)
        messagebox.showinfo("exist")
        list.pop(pos)
        #ms="ok suprimer"
       # lB.insert(END, ms)
        messagebox.showinfo("OK sopprimer")
l1=Label(fen,text="taper le num",font="{arial} 18 bold",bg="black",fg="orange").place(x=62,y=15)
e=Entry(fen, borderwidth=4,textvariable=t1,font=myStyle).place(x=225,y=15,width=222,height=45)
l2=Label(fen,text="taper le nom",font="{arial} 18 bold",bg="black",fg="orange").place(x=62,y=70)
e1=Entry(fen, borderwidth=4,textvariable=t2,font=myStyle).place(x=225,y=70,width=222,height=45)
b=Button(fen, text="AJOUTER", command=ajouter,border=3,font=style,bg="red",fg="black").place(x=22,y=160,width=180,height=38)
b1=Button(fen,text="LISTER",  command=lister,border=3,font=style,bg="red",fg="black").place(x=22,y=210,width=180,height=38)
b2=Button(fen,text="CHERCHER",command=chercher,border=3,font=style,bg="red",fg="black").place(x=22,y=260,width=180,height=38)
b3=Button(fen,text="MODIFIER",command=modifier,border=3,font=style,bg="red",fg="black").place(x=22,y=310,width=180,height=38)
b4=Button(fen,text="SUPRIMER",command=suprimer,border=3,font=style,bg="red",fg="black").place(x=22,y=360,width=180,height=38)
b5=Button(fen,text="VIDER",   command=vider   ,border=3,font=style,bg="red",fg="black").place(x=22,y=410,width=180,height=38)
lB=Listbox(fen,border="2",font="{arial} 20 bold",fg="blue")
lB.place(x=211,y=160,width=290,height=290)






fen.mainloop()