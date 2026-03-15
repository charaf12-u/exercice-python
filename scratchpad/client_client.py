#from
from tkinter import *
from CLASSclient import *
from tkinter import messagebox
from tkinter import ttk

#list
listC=[]
list=[]
for i in range(18,66):
    age=str(i)
    list.append(age)


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


#intvar
r=IntVar()


#les fonction
def CHercher():
    pos=-1
    num=t3.get()
    for i in range(0,len(listC)):
        if(listC[i].num==num):
            pos=i
    return pos
def ajouter():
    if(t1.get()==""):
        messagebox.showerror("","No ajourt le num c'est vider")
    elif(t2.get()==""):
        messagebox.showerror("","No ajourt le nom c'est vider")
    #elif (r.get()!=1 or r.get()!=2):
    #    messagebox.showerror("", "No ajourt le gender c'est vider")

    else:
        num = t1.get()
        nom = t2.get()
        if (r.get() == 1):
            gender= "M"
        if (r.get() == 2):
            gender= "F"
        age = ld.get()
        e = client(num, nom,gender, age)
        listC.append(e)
        messagebox.showinfo("", "CLIENT c'est ajouter")
        t1.set("")
        t2.set("")
        r.set(0)
        ld.current(0)
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
def chercher():
    pos=CHercher()
    if(pos==-1):
        messagebox.showerror("client","NO exist")
    else:
        messagebox.showinfo("client","C'EST exist")
        t4.set(listC[pos].num)
        t5.set(listC[pos].nom)
        t6.set(listC[pos].gender)
        t7.set(listC[pos].age)
def suprimer():
    pos=CHercher()
    if(pos==-1):
        messagebox.showerror("client","NO exist")
    else:
        listC.pop(pos)
        messagebox.showinfo("client","C'EST supprimer")
def modifier():
    pos=CHercher()
    if(pos==-1):
        messagebox.showerror("client","NO exist")
    else:
        if (t1.get() == ""):
            messagebox.showerror("", "No modifier le num c'est vider")
        elif (t2.get() == ""):
            messagebox.showerror("", "No modifier le nom c'est vider")
        #elif (r != 1 and r != 2):
         #   messagebox.showerror("", "No modifier le gender c'est vider")
        else:
            listC[pos].num=t1.get()
            listC[pos].nom=t2.get()
            listC[pos].age=ld.get()
            if(r.get()==1):
                listC[pos].gender = "M"
            if (r.get() == 1):
                listC[pos].gender = "F"
            messagebox.showinfo("client", "C'EST modifier")

def lister():
    l.delete(0,END)
    for client in listC:
        l.insert(END,f"le num c'est :{client.num} ## le nom :{client.nom} ## le gender :{client.gender} ## l'age :{client.age}")

#canvas
c=Canvas(root,bg="black").place(x=0,y=0,width=1200,height=600)
c1=Canvas(root,bg="orange").place(x=490,y=0,width=10,height=600)
c2=Canvas(root,bg="blue").place(x=540,y=470,width=700,height=10)
c3=Canvas(root,bg="blue").place(x=540,y=470,width=10,height=200)





#label
l1=Label(root,text="NUM",bg="black",fg="orange",font=style).place(x=30,y=30)
l2=Label(root,text="NOM",bg="black",fg="orange",font=style).place(x=30,y=90)
l3=Label(root,text="taper le num",bg="black",fg="orange",font=style).place(x=650,y=30)
l4=Label(root,text="le num",bg="black",fg="orange",font=style).place(x=650,y=200)
l5=Label(root,text="le nom",bg="black",fg="orange",font=style).place(x=650,y=250)
l6=Label(root,text="le gender",bg="black",fg="orange",font=style).place(x=650,y=300)
l7=Label(root,text="l'age",bg="black",fg="orange",font=style).place(x=650,y=350)
l8=Label(root,text=":",bg="black",fg="red",font=style).place(x=140,y=27)
l9=Label(root,text=":",bg="black",fg="red",font=style).place(x=140,y=87)
l10=Label(root,text=":",bg="black",fg="red",font=style).place(x=841,y=30)
l11=Label(root,text=":",bg="black",fg="red",font=style).place(x=783,y=200)
l12=Label(root,text=":",bg="black",fg="red",font=style).place(x=783,y=250)
l13=Label(root,text=":",bg="black",fg="red",font=style).place(x=783,y=300)
l14=Label(root,text=":",bg="black",fg="red",font=style).place(x=783,y=350)
l15=Label(root,text="Gender",bg="black",fg="orange",font=style).place(x=30,y=180)
l16=Label(root,text=":",bg="black",fg="red",font=style).place(x=140,y=180)
l17=Label(root,text="Age",bg="black",fg="orange",font=style).place(x=30,y=250)
l18=Label(root,text=":",bg="black",fg="red",font=style).place(x=140,y=250)





#entry
e1=Entry(root,font=style,textvariable=t1).place(x=165,y=34,width=220,height=35)
e2=Entry(root,font=style,textvariable=t2).place(x=165,y=94,width=220,height=35)
e3=Entry(root,font=style,textvariable=t3).place(x=875,y=34,width=220,height=35)
e4=Entry(root,font=style,textvariable=t4).place(x=805,y=204,width=220,height=35)
e5=Entry(root,font=style,textvariable=t5).place(x=805,y=254,width=220,height=35)
e6=Entry(root,font=style,textvariable=t6).place(x=805,y=304,width=220,height=35)
e7=Entry(root,font=style,textvariable=t7).place(x=805,y=354,width=220,height=35)



#BUTTON
b1=Button(root,command=ajouter,text="AJOUTER",font=myStyle,bg="red",fg="white",border=3).place(x=60,y=400,width=170,height=50)
b2=Button(root,command=vider,text="VIDER",font=myStyle,bg="green",fg="white",border=3).place(x=250,y=400,width=170,height=50)
b3=Button(root,command=chercher,text="CHERCHER",font=myStyle,bg="red",fg="white",border=3).place(x=505,y=90,width=170,height=50)
b4=Button(root,command=modifier,text="MODIFIER",font=myStyle,bg="red",fg="white",border=3).place(x=678,y=90,width=170,height=50)
b5=Button(root,command=lister,text="LISTER",font=myStyle,bg="red",fg="white",border=3).place(x=852,y=90,width=170,height=50)
b6=Button(root,command=suprimer,text="SUPRIMER",font=myStyle,bg="red",fg="white",border=3).place(x=1025,y=90,width=170,height=50)
b7=Button(root,command=vider2,text="VIDER",font="contry 18 bold",bg="green",fg="white",border=3).place(x=897,y=393,width=130,height=30)



#RADIOBUTTON
r1=Radiobutton(root,variable=r,value="1",text="M",bg="black",fg="blue",font=myStyle).place(x=200,y=180)
r2=Radiobutton(root,variable=r,value="2",text="F",bg="black",fg="blue",font=myStyle).place(x=300,y=180)



#combobox
ld=ttk.Combobox(root,font=style,value=list)
ld.place(x=160,y=257,width=100,height=30)
ld.current(0)


#listbox
l=Listbox(root)
l.place(x=550,y=480,width=700)






root.mainloop()