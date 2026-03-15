#from
from classMOD import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#FENETRE
fen=Tk()
fen.title("employer")
fen.geometry("1200x600")
fen.resizable(False,False)

#STYLE
myStyle="{arial} 20 bold"
style="century 20 bold"
style2="century 16 bold"

#CANVAS
C=Canvas(fen,bg="black").place(x=0,y=0,width=1200,height=600)
c1=Canvas(fen,bg="orange").place(x=595,y=0,width=10,height=600)


#LIST
list=[]
listC=["dev","BIG BATA","IOT","IOF"]

#lisbox
lisbox = Listbox()
lisbox = Listbox(fen, fg="black",width=250)
lisbox.place(x=700, y=470)

#stringvar
t1=StringVar()
t2=StringVar()
t3=StringVar()
t4=StringVar()
t5=StringVar()
t6=StringVar()
t7=StringVar()

#INTVAR
v1=IntVar()
r1=IntVar()
r2=IntVar()
r3=IntVar()

#LES FONCTION
def defCerche():
    pos=-1
    num=t3.get()
    for i in range(0,len(list)):
        if(list[i].numM==num):
            pos=i
    return pos
def ajouter():
    numM=t1.get()
    nom=t2.get()
    if (v1.get() == 1):
        oblipar = "obligé"
    if (v1.get() == 2):
        oblipar = "Facultative"
    spésialiser = ld.get()

    e=modul(numM,nom,oblipar,spésialiser)
    list.append(e)
    messagebox.showinfo(" ","c'est ajouter")
def chercher():
    pos = defCerche()
    if (pos == -1):
        messagebox.showerror(" ","no exist")
    else:
        messagebox.showinfo(" ", "exist")
        t4.set(str(list[pos].numM))
        t5.set(list[pos].nom)
        t6.set(list[pos].oblipar)
        t7.set(list[pos].spésialiser)

def vider():
    t1.set("")
    t2.set("")
    v1.set("")
    ld.current(0)
def vider2():
    t4.set("")
    t5.set("")
    t6.set("")
    t7.set("")
    list.clear()
    lisbox.delete(0, END)
def lister():
    lisbox.delete(0, END)
    for modul in list:
        lisbox.insert(END, f"num :{modul.numM} ## name: {modul.nom} ## oblipar :{modul.oblipar} ## spésialiser :{modul.spésialiser}")


def modifier():
    pos = defCerche()
    if (pos == -1):
        messagebox.showerror(" ","no exist")
    else:
        messagebox.showinfo("","exist")
        list[pos].numM=t1.get()
        list[pos].nom=t2.get()
        list[pos].spésialiser=ld.get()
        if (v1.get() == 1):
            oblipar = "obligatior"
        if (v1.get() == 2):
            oblipar = "Faculter"
        list[pos].oblipar=oblipar

def suprimer():
    pos = defCerche()
    if (pos == -1):
        messagebox.showerror(" ","no exist")
    else:
        messagebox.showinfo(" ","exist")
        list.pop(pos)
        messagebox.showinfo(" ","c'est suprimer")



#label
l=Label(fen,text="NUM       :",fg="orange",bg="black",font=myStyle).place(y=50,x=70)
l1=Label(fen,text="NOM       :",fg="orange",bg="black",font=myStyle).place(y=140,x=70)
l2=Label(fen,text="spésialiser m :",fg="orange",bg="black",font="{arial} 19 bold").place(y=320,x=70)
l3=Label(fen,text="taper le num   :",fg="orange",bg="black",font=myStyle).place(y=40,x=640)
l4=Label(fen,text="NUM              :",fg="orange",bg="black",font=myStyle).place(y=220,x=680)
l5=Label(fen,text="NNOM            :",fg="orange",bg="black",font=myStyle).place(y=270,x=680)
l6=Label(fen,text="oblipar          :",fg="orange",bg="black",font=myStyle).place(y=320,x=680)
l7=Label(fen,text="spésialiser m:",fg="orange",bg="black",font=myStyle).place(y=370,x=680)



#entry
e=Entry(fen,border=2,textvariable=t1,fg="black",bg="white",font=myStyle).place(y=50,x=250,width=260,height=40)
e1=Entry(fen,border=2,textvariable=t2,fg="black",bg="white",font=myStyle).place(y=140,x=250,width=260,height=40)
e2=Entry(fen,border=2,textvariable=t3,fg="black",bg="white",font=myStyle).place(y=40,x=850,width=300,height=40)
e3=Entry(fen,border=2,textvariable=t4,fg="black",bg="white",font=myStyle).place(y=220,x=880,width=240,height=40)
e4=Entry(fen,border=2,textvariable=t5,fg="black",bg="white",font=myStyle).place(y=270,x=880,width=240,height=40)
e5=Entry(fen,border=2,textvariable=t6,fg="black",bg="white",font=myStyle).place(y=320,x=880,width=240,height=40)
e6=Entry(fen,border=2,textvariable=t7,fg="black",bg="white",font=myStyle).place(y=370,x=880,width=240,height=40)


#combobox
ld=ttk.Combobox(fen,font=myStyle,value=listC)
ld.place(y=320,x=250,width=260,height=40)
ld.current(0)
ld.bind("<<ComboxSelected>>")

#radiobutton
rB=Radiobutton(fen,fg="blue",font=style,bg="black",variable=v1,value=1,text="obligatoir").place(y=230,x=80)
rB1=Radiobutton(fen,fg="blue",font=style,bg="black",variable=v1,value=2,text="Facultative").place(y=230,x=300)


#button
b=Button(fen,text="AJOUTER",command=ajouter,borderwidth=4,font=style,bg="red",fg="white").place(y=430,x=110,width=170,height=60)
b1=Button(fen,text="VIDER",command=vider,borderwidth=4,font=style,bg="red",fg="white").place(y=430,x=300,width=170,height=60)
b2=Button(fen,text="CHERCHER",command=chercher,borderwidth=4,font=style2,bg="red",fg="white").place(y=100,x=615,width=140,height=50)
b3=Button(fen,text="MODIFIER",command=modifier,borderwidth=4,font=style2,bg="red",fg="white").place(y=100,x=760,width=140,height=50)
b4=Button(fen,text="SUPRIMER",command=suprimer,borderwidth=4,font=style2,bg="red",fg="white").place(y=100,x=905,width=140,height=50)
b5=Button(fen,text="LISTER",command=lister,borderwidth=4,font=style2,bg="red",fg="white").place(y=100,x=1050,width=140,height=50)
b6=Button(fen,text="vider",command=vider2,borderwidth=4,font=style2,bg="green",fg="white").place(y=415,x=1012,width=110,height=30)






fen.mainloop()
