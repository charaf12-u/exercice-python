#from
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from classSalairi import *



#fenétre
root=Tk()
root.geometry("1300x700")
root.resizable(False,False)
root.title("Gestion salarie")
img=PhotoImage(file="chef.png")
root.iconphoto(True,img)


#list
list=[]



#les fonction
def CHERCHER():
    pos=-1
    num=tx4.get()
    for i in range(0,len(list)):
        if(list[i].num==num):
            pos=i
    return pos

def ajouter():
    if(tx1.get()==""):
        messagebox.showerror("salairi","NOOO ajouter le num c'est vide")
    if (tx2.get() == ""):
        messagebox.showerror("salairi", "NOOO ajouter le nom c'est vide")
    if (tx3.get() == ""):
        messagebox.showerror("salairi", "NOOO ajouter le salair c'est vide")
    else:
        num = tx1.get()
        nom = tx2.get()
        salaire = tx3.get()
        E = salairi(num, nom, salaire)
        list.append(E)
        tx1.set("")
        tx2.set("")
        tx3.set("")
        messagebox.showinfo("salairi","C'EST ajouter")
def chercher():
    pos=CHERCHER()
    if(len(list)==0):
        messagebox.showerror("salairi","LISTE de salairi c'est vide")
    else:
        if(tx4.get()==""):
            messagebox.showerror("salairi","taper un num par chercher")
        else:
            if(pos==-1):
                messagebox.showerror("salairi", "NO Exist")
            else:
                messagebox.showinfo("salairi", "C'EST Exist")
                tx5.set(list[pos].num)
                tx6.set(list[pos].nom)
                tx7.set(list[pos].getSAL())



def modifier():
    pos = CHERCHER()
    if (len(list) == 0):
        messagebox.showerror("salairi", "LISTE de salairi c'est vide")
    else:
        if (tx4.get() == ""):
            messagebox.showerror("salairi", "taper un num par chercher")
        else:
            if (pos == -1):
                messagebox.showerror("salairi", "NO Exist")
            else:
                messagebox.showinfo("salairi", "C'EST Exist")
                if (tx1.get() == ""):
                    messagebox.showerror("salairi", "NOOO modifier le num c'est vide")
                if (tx2.get() == ""):
                    messagebox.showerror("salairi", "NOOO modifier le nom c'est vide")
                if (tx3.get() == ""):
                    messagebox.showerror("salairi", "NOOO modifier le salair c'est vide")
                else:
                    list[pos].num = tx1.get()
                    list[pos].nom = tx2.get()
                    list[pos].setSAL(tx3.get())
                    messagebox.showinfo("salairi", "C'EST Modifier")
                    tx1.set("")
                    tx2.set("")
                    tx3.set("")

def supprimer():
    pos = CHERCHER()
    if (len(list) == 0):
        messagebox.showerror("salairi", "LISTE de salairi c'est vide")
    else:
        if (tx4.get() == ""):
            messagebox.showerror("salairi", "taper un num par chercher")
        else:
            if (pos == -1):
                messagebox.showerror("salairi", "NO Exist")
            else:
                messagebox.showinfo("salairi", "C'EST Exist")
                list.pop(pos)
                messagebox.showinfo("salairi", "C'EST Supprimer")

def vider():
    if(tx1.get()=="" and tx2.get()=="" and tx3.get()==""):
        messagebox.showinfo("salairi","C'est déja vide")
    else:
        tx1.set("")
        tx2.set("")
        tx3.set("")
        messagebox.showinfo("salairi", "C'est vidé")


def lister():
    li.delete(0,END)
    li.insert(END, f"        NUM")
    li.insert(END, f"")
    for salairi in list:
        li.insert(END,f"{salairi.num}")

    li1.delete(0, END)
    li1.insert(END, f"        NOM")
    li1.insert(END, f"")
    for salairi in list:
        li1.insert(END, f"{salairi.nom}")

i=0

def yamin():
    pos = 0
    if pos == -1:
        messagebox.showinfo('conduteur Info', 'the conducteur with this Num does not exist')
    else:
        tx7.set(list[pos + 1].num)
        tx8.set(list[pos + 1].nom)
def yasar():
    pos = 0
    if pos == -1:
        messagebox.showinfo('conduteur Info', 'the conducteur with this Num does not exist')
    else:
        tx7.set(list[pos - 1].num)
        tx8.set(list[pos - 1].nom)
def toutYAMINE():
    tx7.set(list[len(list) - 1].num)
    tx8.set(list[len(list) - 1].nom)
def toutYASSAR():
    tx7.set(list[0].num)
    tx8.set(list[0].nom)
def Ougmente():
    root.withdraw()
    #fenétre
    fen=Toplevel()
    fen.geometry("600x420")
    fen.resizable(False,False)
    #canvas
    cc = Canvas(fen, bg="#664d03")
    cc.place(x=0, y=0, width=600, height=420)
    #label
    la = Label(fen, text="taper le NUM", font=style, bg="#664d03", fg="#58151c")
    la.place(x=50, y=60)
    la1 = Label(fen, text="Entry oug", font=style, bg="#664d03", fg="#58151c")
    la1.place(x=50, y=120)
    la21 = Label(fen, text=":", font=style, bg="#664d03", fg="#ffc107")
    la21.place(x=240, y=60)
    la22 = Label(fen, text=":", font=style, bg="#664d03", fg="#ffc107")
    la22.place(x=240, y=120)
    #stringvar
    t1=StringVar()
    t2=StringVar()
    #entry
    ee = Entry(fen, font=style, textvariable=t1)
    ee.place(x=280, y=65, width=250, height=30)
    ee1 = Entry(fen, font=style, textvariable=t2)
    ee1.place(x=280, y=125, width=250, height=30)
    #les fonction
    def retour():
        fen.withdraw()
        root.deiconify()
    def ougmenter():
        if(t1.get()==""):
            messagebox.showerror("salairi","NOO ougmenter le num c'est vide")
        if(t2.get() == ""):
            messagebox.showerror("salairi", "NOO ougmenter le nomber de ougmenter c'est vide")
        else:
            pos=-1
            num=t1.get()
            s=int(t2.get())
            for i in range(0,len(list)):
                if(list[i].num==num):
                    pos=i
                    s=int(s)+int(list[pos].getSAL())
                    list[pos].setSAL(s)
                    messagebox.showinfo("salairi","C'EST ougmenter")
            return pos
    #les button
    bu = Button(fen, font=style2, bg="red", fg="white", text="OUGMENTER", border=2, command=ougmenter)
    bu.place(x=50, y=180,width=220,height=50)
    bu1 = Button(fen, font=style2, bg="#055160", fg="#ffc107", text="<<<<", border=2, command=retour)
    bu1.place(x=5, y=360, width=100, height=50)
    fen.mainloop()
def Exporter():
    root.withdraw()


#stringvar
tx1=StringVar()
tx2=StringVar()
tx3=StringVar()
tx4=StringVar()
tx5=StringVar()
tx6=StringVar()
tx7=StringVar()
tx8=StringVar()




#style
style="{arial} 20 bold"
style2="century 20 bold"
style3="{arial} 17 bold"



#canvas
c=Canvas(root,bg="#212529").place(x=0,y=0,width=1300,height=700)
c1=Canvas(root,bg="orange").place(x=0,y=340,width=1300,height=10)
c2=Canvas(root,bg="#dc3545").place(x=645,y=0,width=10,height=340)
c3=Canvas(root,bg="#0dcaf0").place(x=600,y=350,width=10,height=400)
c4=Canvas(root,bg="#0dcaf0").place(x=1130,y=350,width=10,height=400)



#label
l=Label(root,text="NUM Employer",font=style,bg="#212529",fg="orange").place(x=20,y=20)
l1=Label(root,text="NOM Employer",font=style,bg="#212529",fg="orange").place(x=20,y=60)
l2=Label(root,text="Salaire",font=style,bg="#212529",fg="orange").place(x=20,y=110)
l3=Label(root,text="Recherch par num",font=style,bg="#212529",fg="orange").place(x=20,y=360)
l4=Label(root,text="Taper num",font=style2,bg="#212529",fg="red").place(x=20,y=400)
l5=Label(root,text="NUM",font=style,bg="#212529",fg="orange").place(x=200,y=510)
l6=Label(root,text="NOM",font=style,bg="#212529",fg="orange").place(x=200,y=550)
l7=Label(root,text="Afichage",font=style,bg="#212529",fg="green").place(x=610,y=350)
l8=Label(root,text="Déplacement",font=style,bg="#212529",fg="green").place(x=660,y=5)
l9=Label(root,text="LE NUM",font=style,bg="#212529",fg="orange").place(x=760,y=50)
l10=Label(root,text="LE NOM",font=style,bg="#212529",fg="orange").place(x=760,y=110)
l11=Label(root,text="Fichier",font=style,bg="#212529",fg="green").place(x=1170,y=350)
l12=Label(root,text=":",font=style,bg="#212529",fg="#ffc107").place(x=260,y=20)
l13=Label(root,text=":",font=style,bg="#212529",fg="#ffc107").place(x=260,y=60)
l14=Label(root,text=":",font=style,bg="#212529",fg="#ffc107").place(x=260,y=110)
l15=Label(root,text=":",font=style,bg="#212529",fg="#ffc107").place(x=280,y=360)
l16=Label(root,text=":",font=style2,bg="#212529",fg="#ffc107").place(x=190,y=403)
l17=Label(root,text=":",font=style,bg="#212529",fg="#ffc107").place(x=290,y=507)
l18=Label(root,text=":",font=style,bg="#212529",fg="#ffc107").place(x=290,y=547)
l19=Label(root,text=":",font=style,bg="#212529",fg="#ffc107").place(x=730,y=350)
l20=Label(root,text=":",font=style,bg="#212529",fg="#ffc107").place(x=840,y=5)
l21=Label(root,text=":",font=style,bg="#212529",fg="#ffc107").place(x=880,y=48)
l22=Label(root,text=":",font=style,bg="#212529",fg="#ffc107").place(x=880,y=108)


#entry
e=Entry(root,font=style,textvariable=tx1).place(x=280,y=25,width=250,height=30)
e1=Entry(root,font=style,textvariable=tx2).place(x=280,y=65,width=250,height=30)
e2=Entry(root,font=style,textvariable=tx3).place(x=280,y=115,width=250,height=30)
e3=Entry(root,font=style,textvariable=tx4).place(x=210,y=408,width=240,height=30)
e4=Entry(root,font=style,textvariable=tx5).place(x=310,y=512,width=200,height=30)
e5=Entry(root,font=style,textvariable=tx6).place(x=310,y=552,width=200,height=30)
e6=Entry(root,font=style,textvariable=tx7).place(x=910,y=53,width=250,height=30)
e7=Entry(root,font=style,textvariable=tx8).place(x=910,y=113,width=250,height=30)



#LES BUTTON
b=Button(root,font=style2,bg="red",fg="white",text="AJOUTER",border=2,command=ajouter).place(x=160,y=200,width=150,height=47)
b1=Button(root,font=style2,bg="red",fg="white",text="VIDER",border=2,command=vider).place(x=330,y=200,width=150,height=47)
b2=Button(root,font=style2,bg="red",fg="white",text="CHERCHER",border=2,command=chercher).place(x=20,y=450,width=180,height=47)
b3=Button(root,font=style2,bg="red",fg="white",text="SUPRIMER",border=2,command=supprimer).place(x=100,y=620,width=180,height=47)
b4=Button(root,font=style2,bg="red",fg="white",text="MODIFIER",border=2,command=modifier).place(x=300,y=620,width=180,height=47)
b5=Button(root,font=style2,bg="red",fg="white",text="Exporter",border=2,command=Exporter).place(x=1145,y=500,width=150,height=47)
b6=Button(root,font=style2,bg="red",fg="white",text="Ougmente",border=2,command=Ougmente).place(x=1145,y=600,width=150,height=47)
b7=Button(root,font=style2,bg="red",fg="white",text="LISTER",border=2,command=lister).place(x=630,y=400,width=150,height=47)
b8=Button(root,font=style2,bg="red",fg="white",text="<",border=2,command=yasar).place(x=740,y=200,width=100,height=47)
b9=Button(root,font=style2,bg="red",fg="white",text=">",border=2,command=yamin).place(x=853,y=200,width=100,height=47)
b10=Button(root,font=style2,bg="red",fg="white",text="<<",border=2,command=toutYASSAR).place(x=970,y=200,width=100,height=47)
b11=Button(root,font=style2,bg="red",fg="white",text=">>",border=2,command=toutYAMINE).place(x=1085,y=200,width=100,height=47)


#Listbox
li=Listbox(root,bg="#0dcaf0",font=style3)
li.place(x=720,y=500,width=150,height=200)
li1=Listbox(root,bg="#0dcaf0",font=style3)
li1.place(x=871,y=500,width=150,height=200)


root.mainloop()