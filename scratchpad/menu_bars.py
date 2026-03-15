from tkinter import *
from emplYER import *
from program import *
from tkinter import messagebox


#image de button
#ph4=PhotoImage(file="klipartz.com (5).png")
#ph5=PhotoImage(file="klipartz.com (6).png).png")





#root
root=Tk()
root.title("gestion employer")
root.geometry("600x600")
root.config(bg="#343a40")
root.resizable(False,False)
ph1=PhotoImage(file="chef.png")
root.iconphoto(True,ph1)



#les fonction
def add_employe():
    #fenetre
    fen=Toplevel()
    fen.geometry("600x600")
    fen.title("add new amployer")
    fen.resizable(False,False)
    fen.config(bg="#007FFF")
    #label
    l1=Label(fen,text="employer ID",bg="#007FFF",fg="orange",font=style).place(x=50,y=70)
    l2=Label(fen,text="name",bg="#007FFF",fg="orange",font=style).place(x=50,y=140)
    #global
    global t2
    global t1
    global ph2
    #entry
    e1=Entry(fen,textvariable=t1,border=2,font=myStyle).place(x=250,y=70,width=300,height=40)
    e2=Entry(fen,textvariable=t2,border=2,font=myStyle).place(x=250,y=140,width=300,height=40)
    #button
    ph2 = PhotoImage(file="ajouterC.png")
    b=Button(fen,image=ph2,command=add,bg="#007FFF",border=0).place(x=250,y=190)
def chercher_employe():
    #fenetre
    fen=Toplevel()
    fen.geometry("600x600")
    fen.title("chercher amployer")
    fen.resizable(False,False)
    fen.config(bg="#007FFF")
    #label
    l1=Label(fen,text="GIVE ID",bg="#007FFF",fg="orange",font=style).place(x=90,y=70)
    #global
    global t2
    global t1
    #entry
    e1 = Entry(fen, textvariable=t1, border=2, font=myStyle).place(x=250, y=70, width=200, height=40)
    e2 = Entry(fen, textvariable=t2, border=2, font=myStyle).place(x=190, y=200, width=200, height=150)
    #button
    ph2= PhotoImage(file="chercherC.png")
    b = Button(fen,image=ph2, command=chercher_em,bg="#007FFF",border=0).place(x=70, y=210)
    b=Button(fen)
def lister_employe():
    #fenetre
    fen=Toplevel()
    fen.geometry("600x600")
    fen.title("lister amployer")
    fen.resizable(False,False)
    fen.config(bg="#007FFF")
    #global
    global libox
    global t1
    global t2
    global t3
    #button
    b=Button(fen,text="lister",command=lister_employe)
    #LABEL
    l1=Label(fen,text="GIVE ID",bg="#007FFF",fg="orange",font=style).place(x=90,y=70)
    l2=Label(fen,text="EM ID",bg="#007FFF",fg="orange",font=style).place(x=90,y=270)
    l3=Label(fen,text="NOME",bg="#007FFF",fg="orange",font=style).place(x=90,y=350)
    #ENTRY
    e1 = Entry(fen, textvariable=t1, border=2, font=myStyle).place(x=250, y=70, width=200, height=40)
    e2 = Entry(fen, textvariable=t2, border=2, font=myStyle).place(x=250, y=270, width=200, height=40)
    e3 = Entry(fen, textvariable=t3, border=2, font=myStyle).place(x=250, y=350, width=200, height=40)
def supprimer_employe():
    #fenetre
    fen=Toplevel()
    fen.geometry("600x600")
    fen.title("supprimer amployer")
    fen.resizable(False,False)
    fen.config(bg="#007FFF")
    #label
    l1=Label(fen,text="GIVE ID",bg="#007FFF",fg="orange",font=style).place(x=50,y=70)
    #global
    global t1
    #entry
    e1=Entry(fen,textvariable=t1,border=2,font=myStyle).place(x=250,y=70,width=200,height=40)
    #button
    b=Button(fen,text="suprimer",command=supprimer_employe)
def modifier_employe():
    # fenetre
    fen = Toplevel()
    fen.geometry("600x600")
    fen.title("modifier amployer")
    fen.resizable(False, False)
    fen.config(bg="#007FFF")
    #global
    global libox
    global t1
    global t2
    global t3
    # button
    b = Button(fen, text="modifier", command=lister_employe)
    # LABEL
    l1 = Label(fen, text="GIVE ID", bg="#007FFF", fg="orange", font=style).place(x=90, y=70)
    l2 = Label(fen, text="NVem ID", bg="#007FFF", fg="orange", font=style).place(x=90, y=270)
    l3 = Label(fen, text="NV NOME", bg="#007FFF", fg="orange", font=style).place(x=90, y=350)
    # ENTRY
    e1 = Entry(fen, textvariable=t1, border=2, font=myStyle).place(x=250, y=70, width=200, height=40)
    e2 = Entry(fen, textvariable=t2, border=2, font=myStyle).place(x=250, y=270, width=200, height=40)
    e3 = Entry(fen, textvariable=t3, border=2, font=myStyle).place(x=250, y=350, width=200, height=40)


def add():
    if(t1.get()!=""):
        num=t1.get()
        nom=t2.get()
        em=employer(num,nom)
        program.list.append(em)
        t1.set("")
        t2.set("")
        messagebox.showinfo("add employer")
    else:
        messagebox.showinfo("employer vide")
#libox
libox=Listbox()
def liste_em():
    global libox
    for i in range(0,len(program.list)):
        libox.insert(END,str(program.list[i].get_num())
                     +""+str(program.list[i].get_nom()))
def chercher_em():
    global t1
    global t2
    a=int(t1.get())
    pos=program.rechercher_pos(a,program.list)
    if(pos==-1):
        messagebox.showinfo("no exist")
    else:
        messagebox.showinfo("exist")
        t2.set(str(program.list[pos].get_num())+"nom"+program.list[pos].get_nom())
def supprimer_em():
    global t1
    a=int(t1.get())
    pos=program.rechercher_pos(a,program.list)
    if(pos==-1):
        messagebox.showinfo("no exist")
    else:
        program.list.pop(pos)
        messagebox.showinfo("delete ok")



#style
myStyle="{arial} 20 bold"
style="century 20 bold"
style2="century 16 bold"


#stringvar
t1=StringVar()
t2=StringVar()
t3=StringVar()

#menu
my_menu=Menu(root)
root.config(menu=my_menu)
#cree a menu etem
employe_m=Menu(my_menu,bg="#dc3545",font=style,fg="#0dcaf0")
my_menu.add_cascade(label="gestio employe",menu=employe_m)
employe_m.add_command(label="ajouter employer",command=add_employe)
employe_m.add_separator()
employe_m.add_command(label="chercher employer",command=chercher_employe)
employe_m.add_separator()
employe_m.add_command(label="lister employer",command=lister_employe)
employe_m.add_separator()
employe_m.add_command(label="supprimer employer",command=supprimer_employe)
employe_m.add_separator()
employe_m.add_command(label="modifier employer",command=modifier_employe)
employe_m.add_separator()










root.mainloop()