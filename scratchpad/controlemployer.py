#from
from tkinter import *
from tkinter import messagebox
from  CONTROLECLASS import *
from tkinter import ttk

#fenetre
listitem = ["CasaBlanka", "Beni Mellal", "Marrakech", "Tanger","Fes","Meknas",]
root=Tk()
root.title("Client")
root.geometry("1080x690")
root.resizable(False,False)
img=PhotoImage(file="chef.png")
root.iconphoto(True,img)

#LES FONCTION
def modify():
    reference_to_find = int(txf.get())
    pos = -1
    for i in range(len(list_client)):
        if list_client[i].reference == reference_to_find:
            pos = i
            break
    if pos != -1:
        new_name = tx2.get()
        new_chiffA = tx3.get()
        new_ville = tx5.get()
        new_gender = "M" if RG.get() == 1 else "F"

        new_niveau = ""
        if vx1.get():
            new_niveau += "Bac "
        if vx2.get():
            new_niveau += "DEUG "
        if vx3.get():
            new_niveau += "MASTER"

        list_client[pos].name = new_name
        list_client[pos].city = new_ville
        list_client[pos].gender = new_gender
        list_client[pos].level = new_niveau
        list_client[pos].set_chA(new_chiffA)

    else:
        messagebox.showerror("Error", "Client not found")

def delete_client():
    reference_to_delete = int(txf.get())
    pos = -1
    for i in range(0, len(list_client)):
        if list_client[i].reference ==reference_to_delete:
            pos = i

    if pos != -1:
        list_client.pop(pos)
        messagebox.showinfo("Success", "Client deleted successfully")
    else:
        messagebox.showerror("Error", "Client not found")

def find_client():
    reference_to_find = int(txf.get())
    pos=-1

    for i in range(0,len(list_client)):
        if list_client[i].reference == reference_to_find:
            pos=i

    if pos!=-1:
        tx1.set(str(list_client[pos].reference))
        tx2.set(list_client[pos].name)
        tx3.set(list_client[pos].get_chA())
        tx5.set(list_client[pos].city)
        txO1.set("Exist")
    else:
        txO2.set("not Exist")
        messagebox.showerror("Error", "Client not found")
def display_clients():
    lisbox.delete(0, END)
    for client in list_client:
        lisbox.insert(END, f"Client reference:{client.reference} //Client name: {client.name} //Client city: {client.city} //Client CA:{client.get_chA()}//GENDER:{client.gender}-//Niveau:{client.level}")

def add_client():
    ref = int(tx1.get())
    nom = tx2.get()
    chiffA = tx3.get()
    ville = tx5.get()  # Use the selected city from the combobox
    gender = "M" if RG.get() == 1 else "F"

    niveau = ""
    if vx1.get():
        niveau += "Bac "
    if vx2.get():
        niveau += "DEUG "
    if vx3.get():
        niveau += "MASTER"
    c = Client(ref, nom, chiffA, ville, gender, niveau)
    list_client.append(c)

    tx1.set('')
    tx2.set('')
    tx3.set('')
    tx5.set('')
    RG.set(0)
    vx1.set(0)
    vx2.set(0)
    vx3.set(0)
def clear():
    tx1.set('')
    tx2.set('')
    tx3.set('')
    txf.set('')
    tx5.set('')
    RG.set(0)
    vx1.set(0)
    vx2.set(0)
    vx3.set(0)
    txO1.set('')
    txO2.set('')
    list_client.clear()
    lisbox.delete(0, END)


#canvas
c=Canvas(root,bg="#343a40").place(x=0,y=0,width=1080,height=690)
canvas = Canvas(root, width=4, height=800, background="white", bd=0, highlightthickness=0)
canvas.place(x=350, y=0)
C=Canvas(root,bg="#198754").place(x=330,y=0,width=10,height=800)
C1=Canvas(root,bg="#0dcaf0").place(x=190, y=590,width=10,height=100)
C2=Canvas(root,bg="#0dcaf0").place(x=190, y=590,width=900,height=10)

#canvas.create_line(1, 0, 1, 800, fill="green", width=2)



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
image=PhotoImage(file="klipartz.com  (1).png")


#stringvar
tx1 = StringVar()
tx2 = StringVar()
tx3 = StringVar()
txf = StringVar()
tx4 = StringVar()
tx5 = StringVar()
tx6 = StringVar()
txO1 = StringVar()
txO2 = StringVar()

#intvar
vx1 =IntVar()
vx2 =IntVar()
vx3 =IntVar()
RG =IntVar()


#lisbox
lisbox = Listbox()
list_client = []
lisbox = Listbox(root, fg="black",width=250)
lisbox.place(x=200, y=600)


#les button
B=Button(root,image=image,cursor="hand2",bg="#343a40",border=0).place(x=590,y=150)
b1 = Button(root, image=img1, border=0, cursor="hand2",bg="#343a40",command=add_client ).place(x=180, y=5)
b2 = Button(root, image=img3, border=0, cursor="hand2",bg="#343a40",command=display_clients).place(x=180, y=100)
b3 = Button(root, image=img2, border=0, cursor="hand2",bg="#343a40",command=find_client).place(x=180, y=200)
b4 = Button(root, image=img4, border=0, cursor="hand2",bg="#343a40",command=delete_client).place(x=180, y=300)
b5 = Button(root, image=img5, border=0, cursor="hand2",bg="#343a40",command=modify).place(x=180, y=400)
b6 = Button(root, image=img6, border=0, cursor="hand2",bg="#343a40",command=clear).place(x=180, y=500)

#labell
l1 = Label(root, bg="#343a40", fg="orange", text="reference",font=style).place(x=370, y=50)
l2 = Label(root, bg="#343a40", fg="orange", text="name",font=style).place(x=370, y=100)
l3 = Label(root, bg="#343a40", fg="orange", text="chiffre A",font=style).place(x=370, y=150)
l4 = Label(root, bg="#343a40", fg="orange", text="chercher par reference",font=style).place(x=740, y=100)
l5 = Label(root, bg="#343a40", fg="orange", text="Ville",font=style).place(x=370, y=200)
l6 = Label(root, bg="#343a40", fg="orange", text="Gender",font=style).place(x=370, y=250)
l7=Label(root, bg="#343a40", fg="orange", text="Niveau",font=style).place(x=370,y=300)


#entry
e1 = Entry(root, textvariable=tx1,font=myStyle).place(x=540, y=60, height=30,width=170)
e2 = Entry(root, textvariable=tx2,font=myStyle).place(x=540, y=110,height=30,width=170)
e3 = Entry(root, textvariable=tx3,font=myStyle).place(x=540, y=160,height=30,width=170)
e4 = Entry(root, textvariable=txf,font=myStyle).place(x=910, y=150,height=35,width=160)
e5 = Entry(root, textvariable=txO1,fg="green",font=myStyle).place(x=910, y=200,height=35,width=160)
e6 = Entry(root, textvariable=txO2,fg="red",font=myStyle).place(x=910, y=250,height=35,width=160)

#combobox
combo = ttk.Combobox(root, values=listitem, textvariable=tx5,font=myStyle).place(x=540, y=210,height=30,width=170)


#radiobutton
c1 =Radiobutton(root, bg="#343a40",text="H",value=1,variable=RG,font=style,fg="#dc3545").place(x=530, y=250)
c2 =Radiobutton(root, bg="#343a40",text="F",value=2,variable=RG,font=style,fg="#dc3545").place(x=590, y=250)


#checkbutton
c_1=Checkbutton(root, bg="#343a40",fg="#0d6efd",text="Bac",variable=vx1,font=myStyle).place(x=500,y=300)
c_2=Checkbutton(root, bg="#343a40",fg="#0d6efd",text="DEUG",variable=vx2,font=myStyle).place(x=500,y=345)
c_3=Checkbutton(root, bg="#343a40",fg="#0d6efd",text="MASTER",variable=vx3,font=myStyle).place(x=500,y=390)



root.mainloop()