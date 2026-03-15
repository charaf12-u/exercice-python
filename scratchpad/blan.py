#from
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from classBlan import *




#fenétre
root=Tk()
root.geometry("1300x700")
root.resizable(False,False)
root.title("condicteur")
img=PhotoImage(file="chef.png")
root.iconphoto(True,img)



#list
list=[]


#style
style="{arial} 20 bold"
style2="century 20 bold"
style3="{arial} 17 bold"


#stringvar
tx1=StringVar()
tx2=StringVar()
tx3=StringVar()
tx4=StringVar()
tx5=StringVar()
tx6=StringVar()
tx7=StringVar()
tx8=StringVar()
tx9=StringVar()
tx10=StringVar()
tx11=StringVar()
tx12=StringVar()



#canvas
c=Canvas(root,bg="#212529").place(x=0,y=0,width=1300,height=700)
c2=Canvas(root,bg="#dc3545").place(x=550,y=0,width=10,height=700)
c1=Canvas(root,bg="orange").place(x=190,y=27,width=360,height=10)
c3=Canvas(root,bg="orange").place(x=190,y=340,width=360,height=10)
c4=Canvas(root,bg="#dc3545").place(x=1050,y=0,width=10,height=700)
c5=Canvas(root,bg="orange").place(x=750,y=27,width=300,height=10)
c6=Canvas(root,bg="orange").place(x=750,y=200,width=300,height=10)
c7=Canvas(root,bg="orange").place(x=750,y=483,width=300,height=10)



#label
l=Label(root,text="__AJOUTER__",font=style3,bg="#212529",fg="#664d03").place(x=10,y=3)
l1=Label(root,text="NUM C",font=style,bg="#212529",fg="#0dcaf0").place(x=20,y=60)
l2=Label(root,text="NOM C",font=style,bg="#212529",fg="#0dcaf0").place(x=20,y=110)
l3=Label(root,text="ADV C",font=style,bg="#212529",fg="#0dcaf0").place(x=20,y=160)
l4=Label(root,text="__CHERCHE__",font=style3,bg="#212529",fg="#664d03").place(x=10,y=317)
l5=Label(root,text="Entrer un NUM",font=style2,bg="#212529",fg="red").place(x=20,y=370)
l6=Label(root,text="LE NOM",font=style,bg="#212529",fg="#0dcaf0").place(x=40,y=500)
l7=Label(root,text="ADV",font=style,bg="#212529",fg="#0dcaf0").place(x=40,y=550)
l8=Label(root,text="NB AV",font=style,bg="#212529",fg="#0dcaf0").place(x=40,y=600)
l9=Label(root,text="nb BLAN",font=style,bg="#212529",fg="#0dcaf0").place(x=40,y=650)
l10=Label(root,text="_____MAJ_____",font=style3,bg="#212529",fg="#664d03").place(x=560,y=5)
l11=Label(root,text="Entrer un NUM",font=style2,bg="#212529",fg="red").place(x=560,y=40)
l12=Label(root,text="__Déplacement_",font=style3,bg="#212529",fg="#664d03").place(x=560,y=177)
l13=Label(root,text="le NUM",font=style,bg="#212529",fg="#0dcaf0").place(x=620,y=237)
l14=Label(root,text="le NOM",font=style,bg="#212529",fg="#0dcaf0").place(x=620,y=280)
l15=Label(root,text="__AVENTIMEN_",font=style3,bg="#212529",fg="#664d03").place(x=560,y=460)
l16=Label(root,text="Entrer un NUM",font=style2,bg="#212529",fg="red").place(x=560,y=500)
l18=Label(root,text=":",font=style,bg="#212529",fg="orange").place(x=180,y=60)
l20=Label(root,text=":",font=style,bg="#212529",fg="orange").place(x=180,y=110)
l30=Label(root,text=":",font=style,bg="#212529",fg="orange").place(x=180,y=160)
l50=Label(root,text=":",font=style2,bg="#212529",fg="red").place(x=250,y=370)
l60=Label(root,text=":",font=style,bg="#212529",fg="orange").place(x=180,y=500)
l70=Label(root,text=":",font=style,bg="#212529",fg="orange").place(x=180,y=550)
l80=Label(root,text=":",font=style,bg="#212529",fg="orange").place(x=180,y=600)
l90=Label(root,text=":",font=style,bg="#212529",fg="orange").place(x=180,y=650)
l110=Label(root,text=":",font=style2,bg="#212529",fg="red").place(x=790,y=40)
l130=Label(root,text=":",font=style,bg="#212529",fg="orange").place(x=740,y=237)
l140=Label(root,text=":",font=style,bg="#212529",fg="orange").place(x=740,y=280)
l160=Label(root,text=":",font=style2,bg="#212529",fg="red").place(x=780,y=500)


#entry
e=Entry(root,font=style,textvariable=tx1).place(x=200,y=65,width=250,height=30)
e1=Entry(root,font=style,textvariable=tx2).place(x=200,y=115,width=250,height=30)
e2=Entry(root,font=style,textvariable=tx3).place(x=200,y=165,width=250,height=30)
e3=Entry(root,font=style,textvariable=tx4).place(x=270,y=375,width=180,height=30)
e4=Entry(root,font=style,textvariable=tx5).place(x=200,y=505,width=250,height=30)
e5=Entry(root,font=style,textvariable=tx6).place(x=200,y=555,width=250,height=30)
e6=Entry(root,font=style,textvariable=tx7).place(x=200,y=605,width=250,height=30)
e7=Entry(root,font=style,textvariable=tx8).place(x=200,y=655,width=250,height=30)
e8=Entry(root,font=style,textvariable=tx9).place(x=820,y=45,width=200,height=30)
e9=Entry(root,font=style,textvariable=tx10).place(x=790,y=242,width=200,height=30)
e10=Entry(root,font=style,textvariable=tx11).place(x=790,y=285,width=200,height=30)
e11=Entry(root,font=style,textvariable=tx12).place(x=805,y=505,width=200,height=30)


#les fonction
i=0
def CHERCHER():
    pos=-1
    num=tx4.get()
    for i in range(0,len(list)):
        if(list[i].getNC()==num):
            pos=i
    return pos

def ajouter():
    if(tx1.get()==""):
        messagebox.showerror("conducteur", "NOO ajouter le num c'est vider")
    if (tx2.get() == ""):
        messagebox.showerror("conducteur", "NOO ajouter le nom c'est vider")
    if (tx3.get() == ""):
        messagebox.showerror("conducteur", "NOO ajouter le Adr c'est vider")
    else:
        NC = tx1.get()
        NomC = tx2.get()
        Adr = tx3.get()
        c = conducteur(NC, NomC, Adr, 0, 0)
        list.append(c)
        messagebox.showinfo("conducteur", "C'EST ajouter")
        tx1.set("")
        tx2.set("")
        tx3.set("")
def chercher():
    if(tx4.get()==""):
        messagebox.showerror("conducteur", "NOO chercher taper un num")
    else:
        tx5.set("")
        tx6.set("")
        tx7.set("")
        tx8.set("")
        pos = CHERCHER()
        if (pos == -1):
            messagebox.showerror("conducteur", "NO exist")
        else:
            messagebox.showinfo("conducteur", "C'EST exist")
            tx5.set(list[pos].getNomC())
            tx6.set(list[pos].getAdr())
            tx7.set(list[pos].getNBA())
            tx8.set(list[pos].getNbl())

def modifier():
    if (tx4.get() == ""):
        messagebox.showerror("conducteur", "NOO modifier taper un num")
    else:
        pos = CHERCHER()
        if (pos == -1):
            messagebox.showerror("conducteur", "NO exist")
        else:
            messagebox.showinfo("conducteur", "C'EST exist")
            if (tx5.get() == ""):
                messagebox.showerror("conducteur", "NOO modifier le nom c'est vider")
            if (tx6.get() == ""):
                messagebox.showerror("conducteur", "NOO modifier le Adr c'est vider")
            if (tx7.get() == ""):
                messagebox.showerror("conducteur", "NOO modifier le NBA c'est vider")
            if (tx8.get() == ""):
                messagebox.showerror("conducteur", "NOO modifier le NBL c'est vider")

            else:
                list[pos].setNomC(tx5.get())
                list[pos].setAdr(tx6.get())
                list[pos].setNBA(tx7.get())
                list[pos].setNbl(tx8.get())
                messagebox.showinfo("conducteur", "C'EST modifier")
                tx5.set("")
                tx6.set("")
                tx7.set("")
                tx8.set("")

def supprimer():
    if (tx9.get() == ""):
        messagebox.showerror("conducteur", "NOO supprimer taper un num")
    else:
        pos = -1
        num = tx9.get()
        for i in range(0, len(list)):
            if (list[i].getNC() == num):
                pos = i
        if (pos == -1):
            messagebox.showerror("conducteur", "NO exist")
        else:
            messagebox.showinfo("conducteur", "C'EST exist")
            list.pop(pos)
            messagebox.showinfo("conducteur", "C'EST supprimer")

def vider():
    if(tx1.get()=="" and tx2.get()=="" and tx3.get()==""):
        messagebox.showinfo("conducteur", "C'EST déja vide")
    else:
        tx1.set("")
        tx2.set("")
        tx3.set("")
        messagebox.showinfo("conducteur", "C'EST vide")
def lister():
    li.delete(0,END)
    for conducteur in list:
        li.insert(END,f"num:{conducteur.getNC()}#nom:{conducteur.getNomC()}#Adr:{conducteur.getAdr()}#nbA:{conducteur.getNBA()}#Nblan:{conducteur.getNbl()}")

def toutYAMINE():
    global i
    for i in range(0,len(list)):
        tx10.set(list[i].getNC())
        tx11.set(list[i].getNomC())
        i=i+1
    i=len(list)
def toutYASSAR():
    global i
    tx10.set(list[0].getNC())
    tx11.set(list[0].getNomC())
    i=0
def AjAventiment():
    if (tx12.get() == ""):
        messagebox.showerror("conducteur", "NOO Aventiment taper un num")
    else:
        pos = -1
        nm = tx12.get()
        for i in range(0, len(list)):
            if (list[i].getNC() == nm):
                pos = i
        if (pos == -1):
            messagebox.showerror("conducteur", "NO exist")
        else:
            messagebox.showinfo("conducteur", "C'EST exist")
            list[pos].setNBA(int(list[pos].getNBA())+int(1))
            messagebox.showinfo("conducteur", "C'EST avantiment ")
        if(list[pos].getNBA()%4==0):
            s=list[pos].getNBA()/4
            list[pos].setNbl(s)
def Exporter():
    file = open("ccc.txt", "w")
    file.write("")
    for item in range(0, len(list)):
        file.write(
            str(list[item].getNC()) + " ; " + list[item].getNomC() + " ; " + list[item].getAdr() + " ; " + str(
                list[item].getNBA()) + " ; " + str(list[item].getNbl()) + "\n")
    file.close()
    messagebox.showinfo("File info", "the file was writen")
def yamin():
    global i
    i = i + 1
    if (i == len(list)):
        tx10.set(list[0].getNC())
        tx11.set(list[0].getNomC())
        i = 0
    tx10.set(list[i].getNC())
    tx11.set(list[i].getNomC())


def yasar():
    #global i
    #if (i == 0):
   #     for i in range(0, len(list)):
   #         tx10.set(list[i].getNC())
   #         tx11.set(list[i].getNomC())
   #         i = i + 1
   #     i = len(list)
   # i = i - 1
   # if (i == len(list)):
   #     i = 0
   #     tx10.set(list[i].getNC())
   #     tx11.set(list[i].getNomC())
  #  tx10.set(list[i].getNC())
   # tx11.set(list[i].getNomC())


    global i

    if(i==0):
        i=len(list)
    i = i - 1
    if (i == len(list)):
        tx10.set(list[0].getNC())
        tx11.set(list[0].getNomC())
        i = 0
    tx10.set(list[i].getNC())
    tx11.set(list[i].getNomC())



#LES BUTTON
b=Button(root,font=style2,bg="#212529",fg="white",text="AJOUTER",border=2,command=ajouter).place(x=80,y=230,width=150,height=47)
b1=Button(root,font=style2,bg="#212529",fg="white",text="VIDER",border=2,command=vider).place(x=250,y=230,width=150,height=47)
b2=Button(root,font=style2,bg="#212529",fg="white",text="CHERCHER",border=2,command=chercher).place(x=20,y=420,width=180,height=47)
b3=Button(root,font=style2,bg="#212529",fg="white",text="SUPRIMER",border=2,command=supprimer).place(x=720,y=100,width=180,height=47)
b4=Button(root,font=style2,bg="#212529",fg="white",text="MODIFIER",border=2,command=modifier).place(x=270,y=420,width=180,height=47)
b5=Button(root,font=style2,bg="#212529",fg="white",text="Exporter",border=2,command=Exporter).place(x=1105,y=550,width=150,height=47)
b6=Button(root,font=style2,bg="#212529",fg="white",text="Aj AVENT",border=2,command=AjAventiment).place(x=745,y=550,width=150,height=47)
b7=Button(root,font=style2,bg="#212529",fg="white",text="LISTER",border=2,command=lister).place(x=1100,y=20,width=150,height=47)
b8=Button(root,font=style2,bg="#055160",fg="#ffc107",text="<",border=2,command=toutYASSAR).place(x=580,y=350,width=100,height=47)
b9=Button(root,font=style2,bg="#055160",fg="#ffc107",text=">",border=2,command=toutYAMINE).place(x=700,y=350,width=100,height=47)
b10=Button(root,font=style2,bg="#055160",fg="#ffc107",text="<<",border=2,command=yasar).place(x=815,y=350,width=100,height=47)
b11=Button(root,font=style2,bg="#055160",fg="#ffc107",text=">>",border=2,command=yamin).place(x=930,y=350,width=100,height=47)



#Listbox
li=Listbox(root,bg="#adb5bd")
li.place(x=1080,y=90,width=200,height=400)




root.mainloop()