#from
from tkinter import *
from  CLASSclient import *
from tkinter import messagebox
from tkinter import ttk


#list
list=[]
listC=[]
for i in range(18,66):
    age=str(i)
    listC.append(age)


#fenétre
root=Tk()
root.geometry("1200x600")
root.title("client")
img=PhotoImage(file="chef.png")
root.iconphoto(True,img)
root.resizable(False,False)


#style
style="{arial} 21 bold"
myStyle="century 19 bold"


#stringVar
t1=StringVar()
t2=StringVar()
t3=StringVar()
t4=StringVar()
t5=StringVar()
t6=StringVar()
t7=StringVar()



#INTVAR
r=IntVar()


#les fonction
def CHERCHER():
    pos=-1
    num=t3.get()
    for i in range(0,len(list)):
        if(list[i].num==num):
            pos=i
    return pos
def ajouter():
    if(t1.get()==""):
        messagebox.showerror("client","NO ajouter le num c'est vide")
    elif (t2.get() == ""):
        messagebox.showerror("client", "NO ajouter le nom c'est vide")
    else:
        num=t1.get()
        nom=t2.get()
        if(r.get()==1):
            gender="M"
        if (r.get() == 2):
            gender = "F"
        age=ld.get()
        C=client(num,nom,gender,age)
        list.append(C)
        messagebox.showinfo("client","CLIENT c'est ajouter")
        t1.set("")
        t2.set("")
        r.set(0)
        ld.current(0)
def chercher():
    if (t3.get() == ""):
        messagebox.showerror("client", "NO chercher le num c'est vide")
    else:
        pos = CHERCHER()
        if(pos==-1):
            messagebox.showerror("ERROR", "NO exist")
        else:
            messagebox.showinfo("client","C'EST exist")
            t4.set(list[pos].num)
            t5.set(list[pos].nom)
            t6.set(list[pos].gender)
            t7.set(list[pos].age)

def suprimer():
    if (t3.get() == ""):
        messagebox.showerror("client", "NO supprimer le num c'est vide")
    else:
        pos = CHERCHER()
        if (pos == -1):
            messagebox.showerror("ERROR", "CLIENT NO exist")
        else:
            list.pop(pos)
            messagebox.showinfo("client", "C'EST supprimer")

def lister():
    l.delete(0,END)
    for client in list:
        l.insert(END,f"le num :{client.num} ## le nom :{client.nom} ## le gender :{client.gender} ## l'age :{client.age}")
def modifier():
    if (t3.get() == ""):
        messagebox.showerror("client", "NO modifier le num c'est vide")
    else:
        pos = CHERCHER()
        if (pos == -1):
            messagebox.showerror("ERROR", "NO exist")
        else:
            messagebox.showinfo("client", "C'EST modifier")
            list[pos].num=t1.get()
            list[pos].nom=t2.get()
            if(r.get()==1):
                list[pos].gender="M"
            if (r.get() == 2):
                list[pos].gender = "F"
            list[pos].age=ld.get()
def vider():
    t1.set("")
    t2.set("")
    r.set(0)
    ld.current(0)
def vider2():
    t4.set("")
    t5.set("")
    t6.set("")
    t7.set("")
    l.delete(0,END)


#canvas
c=Canvas(root,bg="black").place(x=0,y=0,width=1200,height=600)
c1=Canvas(root,bg="orange").place(x=490,y=0,width=10,height=600)
c2=Canvas(root,bg="blue").place(x=540,y=470,width=700,height=10)
c3=Canvas(root,bg="blue").place(x=540,y=470,width=10,height=200)




#label
l1=Label(root,text="NUM",bg="black",fg="orange",font=style).place(x=30,y=30)
l2=Label(root,text="NOM",bg="black",fg="orange",font=style).place(x=30,y=90)
l3=Label(root,text="Gender",bg="black",fg="orange",font=style).place(x=30,y=180)
l4=Label(root,text="Age",bg="black",fg="orange",font=style).place(x=30,y=250)
l5=Label(root,text="taper le num",bg="black",fg="orange",font=style).place(x=650,y=30)
l6=Label(root,text="le num",bg="black",fg="orange",font=style).place(x=650,y=200)
l7=Label(root,text="le nom",bg="black",fg="orange",font=style).place(x=650,y=250)
l8=Label(root,text="le gender",bg="black",fg="orange",font=style).place(x=650,y=300)
l9=Label(root,text="l'age",bg="black",fg="orange",font=style).place(x=650,y=350)
l10=Label(root,text=":",bg="black",fg="red",font=style).place(x=140,y=30)
l12=Label(root,text=":",bg="black",fg="red",font=style).place(x=140,y=90)
l13=Label(root,text=":",bg="black",fg="red",font=style).place(x=140,y=180)
l14=Label(root,text=":",bg="black",fg="red",font=style).place(x=140,y=250)
l15=Label(root,text=":",bg="black",fg="red",font=style).place(x=841,y=30)
l16=Label(root,text=":",bg="black",fg="red",font=style).place(x=783,y=200)
l17=Label(root,text=":",bg="black",fg="red",font=style).place(x=783,y=250)
l18=Label(root,text=":",bg="black",fg="red",font=style).place(x=783,y=300)
l19=Label(root,text=":",bg="black",fg="red",font=style).place(x=783,y=350)



#ENTRY
e1=Entry(root,font=style,textvariable=t1).place(x=165,y=34,width=220,height=35)
e2=Entry(root,font=style,textvariable=t2).place(x=165,y=94,width=220,height=35)
e3=Entry(root,font=style,textvariable=t3).place(x=875,y=34,width=220,height=35)
e4=Entry(root,font=style,textvariable=t4).place(x=805,y=204,width=220,height=35)
e5=Entry(root,font=style,textvariable=t5).place(x=805,y=254,width=220,height=35)
e6=Entry(root,font=style,textvariable=t6).place(x=805,y=304,width=220,height=35)
e7=Entry(root,font=style,textvariable=t7).place(x=805,y=354,width=220,height=35)



#radiobutton
r1=Radiobutton(root,variable=r,font=myStyle,bg="black",fg="blue",value=1,text="M").place(x=200,y=180)
r2=Radiobutton(root,variable=r,font=myStyle,bg="black",fg="blue",value=2,text="F").place(x=300,y=180)



#button
b1=Button(root,font=myStyle,bg="red",fg="white",text="AJOUTER",command=ajouter,border=3).place(x=60,y=400,width=170,height=50)
b2=Button(root,font=myStyle,bg="green",fg="white",text="VIDER",command=vider,border=3).place(x=250,y=400,width=170,height=50)
b3=Button(root,font=myStyle,bg="red",fg="white",text="CHERCHER",command=chercher,border=3).place(x=505,y=90,width=170,height=50)
b4=Button(root,font=myStyle,bg="red",fg="white",text="MODIFIER",command=modifier,border=3).place(x=678,y=90,width=170,height=50)
b5=Button(root,font=myStyle,bg="red",fg="white",text="LISTER",command=lister,border=3).place(x=852,y=90,width=170,height=50)
b6=Button(root,font=myStyle,bg="red",fg="white",text="SUPRIMER",command=suprimer,border=3).place(x=1025,y=90,width=170,height=50)
b7=Button(root,font="contry 17 bold",bg="green",fg="white",text="VIDER",command=vider2,border=3).place(x=897,y=393,width=130,height=30)




#combobox
ld=ttk.Combobox(root,font=style,value=listC)
ld.place(x=160,y=257,width=100,height=30)
ld.current(0)


#listbox
l=Listbox(root)
l.place(x=550,y=480,width=700)


root.mainloop()