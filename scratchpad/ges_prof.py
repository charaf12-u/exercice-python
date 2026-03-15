#from
from tkinter import *
from tkinter import messagebox
from  classPROF import *
from tkinter import ttk

#list
list=[]

#fenetre
root=Tk()
root.title("PROF")
root.geometry("1080x690")
root.resizable(False,False)
img=PhotoImage(file="prof.png")
root.iconphoto(True,img)

#LES FONCTION
def modify():
    ref = int(tx3.get())
    pos = -1
    for i in range(len(list)):
        if list[i].getREF() == ref:
            pos = i
            break
    if pos != -1:
        new_ref = tx1.get()
        new_nam = tx2.get()
        list[pos].setREF(new_ref)
        list[pos].setNOM(new_nam)
        messagebox.showinfo(" ", "ok modifier")
    else:
        messagebox.showerror("Error", "Prof no exist")

def delete():
    ref = int(tx3.get())
    pos = -1
    for i in range(0, len(list)):
        if list[i].getREF() ==ref:
            pos = i

    if pos != -1:
        list.pop(pos)
        messagebox.showinfo("exist", "Prof c'est suprimer")
    else:
        messagebox.showerror("Error", "Prof no exist")

def chercher():
    ref = int(tx3.get())
    pos=-1

    for i in range(0,len(list)):
        if list[i].getREF() == ref:
            pos=i

    if pos!=-1:
        tx4.set("ref : "+str(list[pos].getREF()))
        tx5.set("nom : "+list[pos].getNOM())
        messagebox.showinfo(" ", "Prof exist")

    else:
        messagebox.showerror(" ", "Prof no exist")
def aficher():
    lisbox.delete(0, END)
    for Prof in list:
        lisbox.insert(END, f"ref par PROF:{Prof.getREF()} ## Prof name: {Prof.getNOM()}")

def ajouter():
    ref = int(tx1.get())
    nom = tx2.get()
    P = Prof(ref, nom)
    list.append(P)
    tx1.set('')
    tx2.set('')
    messagebox.showinfo(" ", "Prof c'est ajouter")


def clear():
    tx1.set('')
    tx2.set('')
    tx3.set('')
    tx4.set('')
    tx5.set('')
    list_client.clear()
    lisbox.delete(0, END)


#canvas
c=Canvas(root,bg="#343a40").place(x=0,y=0,width=1080,height=690)
canvas = Canvas(root, width=4, height=800, background="white", bd=0, highlightthickness=0)
canvas.place(x=350, y=0)
C=Canvas(root,bg="#198754").place(x=330,y=0,width=10,height=800)
C1=Canvas(root,bg="#0dcaf0").place(x=190, y=590,width=10,height=100)
C2=Canvas(root,bg="#0dcaf0").place(x=190, y=590,width=900,height=10)



#style
myStyle="{arial} 20 bold"
style="century 20 bold"
style2="century 16 bold"

#les image
img1 = PhotoImage(file="add_client.png")
img2 = PhotoImage(file="find_client.png")
img3 = PhotoImage(file="display_client.png")
img4 = PhotoImage(file="delete_client.png")
img5 = PhotoImage(file="modify_client.png")
img6 = PhotoImage(file="DELET-TOUT.png")
image=PhotoImage(file="icoProf.png")


#stringvar
tx1 = StringVar()
tx2 = StringVar()
tx3 = StringVar()
tx4 = StringVar()
tx5 = StringVar()




#lisbox
lisbox = Listbox()
list_client = []
lisbox = Listbox(root, fg="black",width=250)
lisbox.place(x=200, y=600)


#les button
B=Button(root,image=image,cursor="hand2",bg="#343a40",border=0).place(x=590,y=150)
b1 = Button(root, image=img1, border=0, cursor="hand2",bg="#343a40",command=ajouter ).place(x=180, y=5)
b2 = Button(root, image=img3, border=0, cursor="hand2",bg="#343a40",command=aficher).place(x=180, y=100)
b3 = Button(root, image=img2, border=0, cursor="hand2",bg="#343a40",command=chercher).place(x=180, y=200)
b4 = Button(root, image=img4, border=0, cursor="hand2",bg="#343a40",command=delete).place(x=180, y=300)
b5 = Button(root, image=img5, border=0, cursor="hand2",bg="#343a40",command=modify).place(x=180, y=400)
b6 = Button(root, image=img6, border=0, cursor="hand2",bg="#343a40",command=clear).place(x=180, y=500)

#labell
l1 = Label(root, bg="#343a40", fg="orange", text="Ref P",font=style).place(x=370, y=50)
l2 = Label(root, bg="#343a40", fg="orange", text="Name P",font=style).place(x=370, y=150)
l3 = Label(root, bg="#343a40", image=image).place(x=590, y=160)
l4 = Label(root, bg="#343a40", fg="orange", text="Taper ref",font=style).place(x=870, y=150)
l5 = Label(root, bg="#343a40", fg="#dc3545", text=":",font=style).place(x=500, y=50)
l6 = Label(root, bg="#343a40", fg="#dc3545", text=":",font=style).place(x=500, y=150)



#entry
e1 = Entry(root, textvariable=tx1,font=myStyle).place(x=540, y=55, height=35,width=190)
e2 = Entry(root, textvariable=tx2,font=myStyle).place(x=540, y=155,height=35,width=190)
e3 = Entry(root, textvariable=tx3,font=myStyle).place(x=855, y=190,height=30,width=170)
e4 = Entry(root, textvariable=tx4,font=myStyle).place(x=855, y=260,height=30,width=170)
e5 = Entry(root, textvariable=tx5,font=myStyle).place(x=855, y=330,height=30,width=170)




root.mainloop()