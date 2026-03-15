from classE import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
fen=Tk()
list=[]
listC=["casa","bni mlal","marakech","agadir","tanger"]
t1=StringVar()
t2=StringVar()
t3=StringVar()
t4=StringVar()
t5=StringVar()
t6=StringVar()
t7=StringVar()
t8=StringVar()
t9=StringVar()
t10=StringVar()
t11=StringVar()
t12=StringVar()
t13=StringVar()
v1=IntVar()
r1=IntVar()
r2=IntVar()
r3=IntVar()

#LES FONCTINO
def defCerche():
    pos=-1
    ref=t7.get()
    for i in range(0,len(list)):
        if(list[i].ref==ref):
            pos=i
    return pos
def ajouter():
    ref = t1.get()

    nom=t2.get()
    chiffr=t3.get()
    if (v1.get() == 1):
        gender = "M"
    if (v1.get() == 2):
        gender = "F"
    niveau = ""
    if (r1 == 1):
        niveau = niveau + " BAC ."
    if (r2 == 1):
        niveau = niveau + " DEUG ."
    if (r3 == 1):
        niveau = niveau + " MMTC ."
    vill=ld.get()
    e=employer(ref,nom,chiffr,vill,gender,niveau)
    list.append(e)
    messagebox.showinfo("c'est ajouter")
def chercher():
    pos = defCerche()
    if (pos == -1):
        messagebox.showinfo("no exist")
    else:
        messagebox.showinfo("exist")
def vider():
    t1.set("")
    t2.set("")
    t3.set("")
    v1.set("")
    r1.set("")
    r2.set("")
    r3.set("")
    ld.current(0)
def Vider():
    t8.set("")
    t9.set("")
    t10.set("")
    t11.set("")
    t12.set("")
    t13.set("")
def lister():
    pos = defCerche()
    if (pos == -1):
        messagebox.showinfo("no exist")
    else:
        messagebox.showinfo("exist")
        t8.set(str(list[pos].ref))
        t9.set(list[pos].nom)
        t10.set(list[pos].getChiffr())
        t11.set(list[pos].vill)
        t12.set(list[pos].gender)
        t13.set(list[pos].niveau)
def modifier():
    pos = defCerche()
    if (pos == -1):
        messagebox.showinfo("no exist")
    else:
        messagebox.showinfo("exist")
        list[pos].ref=t1.get()
        list[pos].nom=t2.get()
        list[pos].chiffr=t3.get()
        list[pos].vill=ld.get()
        if (v1.get() == 1):
            Ngender = "M"
        if (v1.get() == 2):
            Ngender = "F"
        list[pos].gender=Ngender
        niveau = ""
        if (r1 == 1):
            niveau = niveau + " BAC ."
        if (r2 == 1):
            niveau = niveau + " DEUG ."
        if (r3 == 1):
            niveau = niveau + " MMTC ."
        list[pos].niveau=niveau

def suprimer():
    pos = defCerche()
    if (pos == -1):
        messagebox.showinfo("no exist")
    else:
        messagebox.showinfo("exist")
        list.pop(pos)
        messagebox.showinfo("c'est suprimer")

#FENETRE
fen.title("employer")
fen.geometry("1200x600")
fen.resizable(False,False)

#STYLE
myStyle="{arial} 20 bold"
style="century 20 bold"
style2="century 16 bold"

#CANVAS
C=Canvas(fen,bg="black",border=0).place(x=0,y=0,width=1200,height=600)
c1=Canvas(fen,bg="orange",border=0).place(x=595,y=0,width=10,height=600)
c2=Canvas(fen,bg="blue",border=0).place(x=595,y=100,width=10,height=20)
c3=Canvas(fen,bg="brown",border=0).place(x=595,y=200,width=10,height=20)
c4=Canvas(fen,bg="black",border=0).place(x=595,y=300,width=10,height=20)
c5=Canvas(fen,bg="green",border=0).place(x=595,y=400,width=10,height=20)
c6=Canvas(fen,bg="white",border=0).place(x=595,y=500,width=10,height=17)

#LABEL
l=Label(fen,text="Ref",fg="orange",bg="black",font=myStyle).place(y=50,x=20)
l1=Label(fen,text=":",fg="brown",bg="black",font=myStyle).place(y=50,x=130)
l2=Label(fen,text="Nom",fg="orange",bg="black",font=myStyle).place(y=110,x=20)
l3=Label(fen,text=":",fg="brown",bg="black",font=myStyle).place(y=110,x=130)
l4=Label(fen,text="Cheffr",fg="orange",bg="black",font=myStyle).place(y=170,x=20)
l5=Label(fen,text=":",fg="brown",bg="black",font=myStyle).place(y=170,x=130)
l6=Label(fen,text="Vill",fg="orange",bg="black",font=myStyle).place(y=230,x=20)
l7=Label(fen,text=":",fg="brown",bg="black",font=myStyle).place(y=230,x=130)
l8=Label(fen,text="Gender",fg="orange",bg="black",font=myStyle).place(y=290,x=20)
l9=Label(fen,text=":",fg="brown",bg="black",font=myStyle).place(y=290,x=130)
l10=Label(fen,text="Niveau",fg="orange",bg="black",font=myStyle).place(y=350,x=20)
l11=Label(fen,text=":",fg="brown",bg="black",font=myStyle).place(y=350,x=130)
l12=Label(fen,text="taper le ref",fg="orange",bg="black",font=myStyle).place(y=40,x=640)
l13=Label(fen,text=":",fg="brown",bg="black",font=myStyle).place(y=40,x=800)
l14=Label(fen,text="Ref",fg="orange",bg="black",font=myStyle).place(y=220,x=680)
l15=Label(fen,text=":",fg="brown",bg="black",font=myStyle).place(y=220,x=795)
l16=Label(fen,text="Nom",fg="orange",bg="black",font=myStyle).place(y=270,x=680)
l17=Label(fen,text=":",fg="brown",bg="black",font=myStyle).place(y=270,x=795)
l18=Label(fen,text="Cheffr",fg="orange",bg="black",font=myStyle).place(y=320,x=680)
l19=Label(fen,text=":",fg="brown",bg="black",font=myStyle).place(y=320,x=795)
l20=Label(fen,text="Vill",fg="orange",bg="black",font=myStyle).place(y=370,x=680)
l21=Label(fen,text=":",fg="brown",bg="black",font=myStyle).place(y=370,x=795)
l22=Label(fen,text="Gender",fg="orange",bg="black",font=myStyle).place(y=420,x=680)
l23=Label(fen,text=":",fg="brown",bg="black",font=myStyle).place(y=420,x=795)
l24=Label(fen,text="Niveau",fg="orange",bg="black",font=myStyle).place(y=470,x=680)
l25=Label(fen,text=":",fg="brown",bg="black",font=myStyle).place(y=470,x=795)


#ENTRY
e=Entry(fen,border=2,textvariable=t1,fg="black",bg="white",font=myStyle).place(y=50,x=160,width=300,height=40)
e1=Entry(fen,border=2,textvariable=t2,fg="black",bg="white",font=myStyle).place(y=110,x=160,width=300,height=40)
e2=Entry(fen,border=2,textvariable=t3,fg="black",bg="white",font=myStyle).place(y=170,x=160,width=300,height=40)
e3=Entry(fen,border=2,textvariable=t7,fg="black",bg="white",font=myStyle).place(y=40,x=850,width=300,height=40)
e4=Entry(fen,border=2,textvariable=t8,fg="black",bg="white",font=myStyle).place(y=220,x=860,width=240,height=40)
e5=Entry(fen,border=2,textvariable=t9,fg="black",bg="white",font=myStyle).place(y=270,x=860,width=240,height=40)
e6=Entry(fen,border=2,textvariable=t10,fg="black",bg="white",font=myStyle).place(y=320,x=860,width=240,height=40)
e7=Entry(fen,border=2,textvariable=t11,fg="black",bg="white",font=myStyle).place(y=370,x=860,width=240,height=40)
e8=Entry(fen,border=2,textvariable=t12,fg="black",bg="white",font=myStyle).place(y=420,x=860,width=240,height=40)
e9=Entry(fen,border=2,textvariable=t13,fg="black",bg="white",font=myStyle).place(y=470,x=860,width=240,height=40)

#COMBOBOX
ld=ttk.Combobox(fen,font=myStyle,value=listC)
ld.place(y=230,x=160,width=300,height=40)
ld.current(0)
ld.bind("<<ComboxSelected>>")

#RADIOBUTTON
rB=Radiobutton(fen,fg="blue",font=style,bg="black",variable=v1,value=1,text="M").place(y=290,x=220,width=60,height=40 )
rB1=Radiobutton(fen,fg="blue",font=style,bg="black",variable=v1,value=2,text="F").place(y=290,x=340,width=60,height=40 )

#CHECKBUTTON
cb=Checkbutton(fen,font=myStyle,bg="black",fg="blue",text="BAC",variable=r1).place(y=350,x=160)
cb1=Checkbutton(fen,font=myStyle,bg="black",fg="blue",text="DEUG",variable=r2).place(y=390,x=160)
cb2=Checkbutton(fen,font=myStyle,bg="black",fg="blue",text="MMTE",variable=r3).place(y=430,x=160)


#BUTTON
b=Button(fen,text="AJOUTER",command=ajouter,borderwidth=4,font=style,bg="red",fg="white").place(y=490,x=60,width=170,height=60)
b1=Button(fen,text="VIDER",command=vider,borderwidth=4,font=style,bg="red",fg="white").place(y=490,x=250,width=170,height=60)
b2=Button(fen,text="CHERCHER",command=chercher,borderwidth=4,font=style2,bg="red",fg="white").place(y=100,x=615,width=140,height=50)
b3=Button(fen,text="MODIFIER",command=modifier,borderwidth=4,font=style2,bg="red",fg="white").place(y=100,x=760,width=140,height=50)
b4=Button(fen,text="SUPRIMER",command=suprimer,borderwidth=4,font=style2,bg="red",fg="white").place(y=100,x=905,width=140,height=50)
b5=Button(fen,text="LISTER",command=lister,borderwidth=4,font=style2,bg="red",fg="white").place(y=100,x=1050,width=140,height=50)
b6=Button(fen,text="VIDER",command=Vider,borderwidth=4,font=style2,bg="green",fg="brown").place(y=520,x=992,width=110,height=30)




fen.mainloop()
