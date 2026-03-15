#from
from tkinter import *
from ClassPROF1 import *
from tkinter import messagebox
from tkinter import ttk


#list
list=[]


#fenétre
root=Tk()
root.title("PROF")
root.geometry("1080x690")
root.resizable(False,False)
img=PhotoImage(file="chef.png")
root.iconphoto(True,img)


#canvas
c=Canvas(root,bg="#343a40").place(x=0,y=0,width=1080,height=690)
c1=Canvas(root,bg="white",highlightthickness=0).place(x=350,y=0,width=4,height=800)
c2=Canvas(root,bg="#198754").place(x=330,y=0,width=10,height=800)
c3=Canvas(root,bg="#0dcaf0").place(x=190,y=590,width=10,height=100)
c4=Canvas(root,bg="#0dcaf0").place(x=190,y=590,width=900,height=10)


#myStyle
myStyle="{arial} 20 bold"
style="{arial} 20 bold"
style2="{arial} 16 bold"


#les image
img1=PhotoImage(file="add_client.png")
img2=PhotoImage(file="find_client.png")
img3=PhotoImage(file="display_client.png")
img4=PhotoImage(file="delete_client.png")
img5=PhotoImage(file="modify_client.png")
img6=PhotoImage(file="DELET-TOUT.png")
img7=PhotoImage(file="icoProf.png")


#stringvar
tx1=StringVar()
tx2=StringVar()
tx3=StringVar()
tx4=StringVar()
tx5=StringVar()


#LES FONCTION
def ajouter():
    if(tx1.get()==""):
        messagebox.showerror("prof","NOOOO ajoter c'est le ref est vide")
    if (tx2.get() == ""):
        messagebox.showerror("prof", "NOOOO ajoter c'est le nom est vide")
    else:
        ref = tx1.get()
        nom = tx2.get()
        P = Prof(ref, nom)
        list.append(P)
        tx1.set("")
        tx2.set("")
        messagebox.showinfo("client", "PROF c'est ajouter")
def chercher():
    ref=tx3.get()
    pos=-1
    for i in range(0,len(list)):
        if(list[i].getREF()==ref):
            pos=i
    if(pos==-1):
        messagebox.showerror("prof","NNNOOO exist")
    else:
        messagebox.showinfo("prof","Exist")
        tx4.set("le ref :"+str(list[pos].getREF()))
        tx5.set("le nom :"+str(list[pos].getNOM()))
def modifier():
    ref = tx3.get()
    pos = -1
    for i in range(0, len(list)):
        if (list[i].getREF() == ref):
            pos = i
    if (pos == -1):
        messagebox.showerror("prof", "NNNOOO exist")
    else:
        messagebox.showinfo("prof", "Exist")
        list[pos].setREF(tx1.get())
        list[pos].setNOM(tx2.get())
        messagebox.showinfo("prof", "C'EST modifier")
def suprimer():
    ref = tx3.get()
    pos = -1
    for i in range(0, len(list)):
        if (list[i].getREF() == ref):
            pos = i
    if (pos == -1):
        messagebox.showerror("prof", "NNNOOO exist")
    else:
        messagebox.showinfo("prof", "Exist")
        list.pop(pos)
def vider():
    if(tx1.get()=="" and tx2.get()=="" and tx3.get()=="" and tx4.get()==""and tx5.get()=="" and len(li)==0):
        messagebox.showerror("prof","tout vider")

    else:
        tx1.set("")
        tx2.set("")
        tx3.set("")
        tx4.set("")
        tx5.set("")
        li.delete(0, END)
        messagebox.showinfo("prof","C'EST vider")
def lister():
    if(len(list)==0):
        messagebox.showerror("prof","list c'est vider taper un prof")
    else:
        li.delete(0,END)
        for Prof in list:
            li.insert(END,f"ref de prof c'est :{Prof.getREF()}  ##  EST le nom c'est : {Prof.getNOM()}")



#lisbox
li=Listbox(root,fg="black")
li.place(x=200,y=600,width=900)

#les button
b=Button(root,image=img1,border=0,bg="#343a40",cursor="hand2",command=ajouter).place(x=180,y=5)
b1=Button(root,image=img2,border=0,bg="#343a40",cursor="hand2",command=chercher).place(x=180,y=100)
b2=Button(root,image=img3,border=0,bg="#343a40",cursor="hand2",command=lister).place(x=180,y=200)
b3=Button(root,image=img4,border=0,bg="#343a40",cursor="hand2",command=suprimer).place(x=180,y=300)
b4=Button(root,image=img5,border=0,bg="#343a40",cursor="hand2",command=modifier).place(x=180,y=400)
b5=Button(root,image=img6,border=0,bg="#343a40",cursor="hand2",command=vider).place(x=180,y=500)



#label
l=Label(root,text="REF P",font=style,bg="#343a40",fg="orange").place(x=370,y=50)
l1=Label(root,text="NOM P",font=style,bg="#343a40",fg="orange").place(x=370,y=150)
l2=Label(root,text="taper le ref",font=style,bg="#343a40",fg="orange").place(x=870,y=150)
l3=Label(root,text=":",font=style,bg="#343a40",fg="red").place(x=500,y=50)
l4=Label(root,text=":",font=style,bg="#343a40",fg="red").place(x=500,y=150)
l5=Label(root,image=img7,bg="#343a40").place(x=590,y=189)


#entry
e=Entry(root,font=myStyle,textvariable=tx1).place(x=540,y=55,height=35,width=190)
e1=Entry(root,font=myStyle,textvariable=tx2).place(x=540,y=155,height=35,width=190)
e2=Entry(root,font=myStyle,textvariable=tx3).place(x=855,y=190,height=30,width=170)
e3=Entry(root,font=myStyle,textvariable=tx4).place(x=855,y=260,height=30,width=170)
e4=Entry(root,font=myStyle,textvariable=tx5).place(x=855,y=330,height=30,width=170)








root.mainloop()