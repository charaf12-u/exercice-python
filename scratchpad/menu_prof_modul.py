from tkinter import *
from classPROF import *
from classMOD import modul
fen=Tk()
fen.geometry("400x400")
fen.title("menu")
c=Canvas(fen,bg="#0dcaf0").place(x=0,y=0,width=400,height=400)
fen.resizable(False,False)
tx1=StringVar()
tx2=StringVar()
tx3=StringVar()
tx4=StringVar()
tx5=StringVar()


def prof():
    root=Toplevel()
    # from
    from tkinter import messagebox
    from tkinter import ttk
    from classPROF import Prof
    img = PhotoImage(file="prof.png")
    root.iconphoto(True, img)


    # list
    list = []

    # fenetre
    root = Tk()
    root.title("PROF")
    root.geometry("1080x690")
    root.resizable(False, False)


    #dala mo9adasa
    def defCHERCHER():
        pos = -1
        ref=tx3.get()
        for i in range(0,len(list)):
            if(list[i].getREF()==ref):
                pos=i
        return pos



    # LES FONCTION
    def modify():
        pos = defCHERCHER()
        if pos != -1:
            ref = tx1.get()
            nam = tx2.get()
            list[pos].setREF(ref)
            list[pos].setNOM(nam)
            messagebox.showinfo(" ", "ok modifier")
        else:
            messagebox.showerror("Error", "Prof no exist")

    def delete():
        pos=defCHERCHER()
        if pos != -1:
            list.pop(pos)
            messagebox.showinfo("exist", "Prof c'est suprimer")
        else:
            messagebox.showerror("Error", "Prof no exist")

    def chercher():
        pos=defCHERCHER()
        if pos != -1:
            tx4.set("ref : " + str(list[pos].getREF()))
            tx5.set("nom : " + list[pos].getNOM())
            messagebox.showinfo(" ", "Prof exist")

        else:
            messagebox.showerror(" ", "Prof no exist")

    def aficher():
        lisbox.delete(0, END)
        for Prof in list:
            lisbox.insert(END, f"ref par PROF:{Prof.getREF()} ## Prof name: {Prof.getNOM()}")

    def ajouter():
        ref= tx1.get()
        nom= tx2.get()
        P= Prof(ref,nom)
        list.append(P)
        tx1.set("")
        tx2.set("")
        messagebox.showinfo(" ", "Prof c'est ajouter")

    def clear():
        tx1.set("")
        tx2.set("")
        tx3.set("")
        tx4.set("")
        tx5.set("")
        list.clear()
        lisbox.delete(0, END)

    # canvas
    c = Canvas(root, bg="#343a40").place(x=0, y=0, width=1080, height=690)
    canvas = Canvas(root, width=4, height=800, background="white", bd=0, highlightthickness=0)
    canvas.place(x=350, y=0)
    C = Canvas(root, bg="#198754").place(x=330, y=0, width=10, height=800)
    C1 = Canvas(root, bg="#0dcaf0").place(x=190, y=590, width=10, height=100)
    C2 = Canvas(root, bg="#0dcaf0").place(x=190, y=590, width=900, height=10)

    # style
    myStyle = "{arial} 20 bold"
    style = "century 20 bold"

    # global
    global tx1
    global tx2
    global tx3
    global tx4
    global tx5

    # lisbox
    lisbox = Listbox()
    lisbox = Listbox(root, fg="black", width=250)
    lisbox.place(x=200, y=600)

    # les button
    B = Button(root, cursor="hand2", bg="#343a40", border=0)
    B.place(x=590, y=150)
    b1 = Button(root,text="AJOUTER", border=2, cursor="hand2", bg="#dc3545",fg="white",font=style, command=ajouter)
    b1.place(x=120, y=5,width=200)
    b2 = Button(root,text="AFICHER", border=2, cursor="hand2", bg="#dc3545",fg="white",font=style, command=aficher)
    b2.place(x=120, y=100,width=200)
    b3 = Button(root,text="CHERCHER", border=2, cursor="hand2", bg="#dc3545",fg="white",font=style, command=chercher)
    b3.place(x=120, y=200,width=200)
    b4 = Button(root,text="SUPPRIMER", border=2, cursor="hand2", bg="#dc3545",fg="white",font=style, command=delete)
    b4.place(x=120, y=300,width=200)
    b5 = Button(root,text="MODIFIER", border=2, cursor="hand2", bg="#dc3545",fg="white",font=style, command=modify)
    b5.place(x=120, y=400,width=200)
    b6 = Button(root,text="VIDER", border=2, cursor="hand2", bg="#dc3545",fg="white",font=style, command=clear)
    b6.place(x=120, y=500,width=200)


    # labell
    l1 = Label(root, bg="#343a40", fg="orange", text="Ref P", font=style)
    l1.place(x=370, y=50)
    l2 = Label(root, bg="#343a40", fg="orange", text="Name P", font=style)
    l2.place(x=370, y=150)
    l3 = Label(root, bg="#343a40")
    l3.place(x=590, y=160)
    l4 = Label(root, bg="#343a40", fg="orange", text="Taper ref", font=style)
    l4.place(x=870, y=150)
    l5 = Label(root, bg="#343a40", fg="#dc3545", text=":", font=style)
    l5.place(x=500, y=50)
    l6 = Label(root, bg="#343a40", fg="#dc3545", text=":", font=style)
    l6.place(x=500, y=150)

    # entry
    e1 = Entry(root, textvariable=tx1, font=myStyle)
    e1.place(x=540, y=55, height=35, width=190)
    e2 = Entry(root, textvariable=tx2, font=myStyle)
    e2.place(x=540, y=155, height=35, width=190)
    e3 = Entry(root, textvariable=tx3, font=myStyle)
    e3.place(x=855, y=190, height=30, width=170)
    e4 = Entry(root, textvariable=tx4, font=myStyle)
    e4.place(x=855, y=260, height=30, width=170)
    e5 = Entry(root, textvariable=tx5, font=myStyle)
    e5.place(x=855, y=330, height=30, width=170)


def modul():
    # from

    from tkinter import messagebox
    from tkinter import ttk
    from classMOD import modul

    # FENETRE
    fen = Tk()
    fen.title("employer")
    fen.geometry("1200x600")
    fen.resizable(False, False)

    # STYLE
    myStyle = "{arial} 20 bold"
    style = "century 20 bold"
    style2 = "century 16 bold"

    # CANVAS
    C = Canvas(fen, bg="black").place(x=0, y=0, width=1200, height=600)
    c1 = Canvas(fen, bg="orange").place(x=595, y=0, width=10, height=600)

    # LIST
    list = []
    listC = ["dev", "BIG BATA", "IOT", "IOF"]

    # lisbox
    lisbox = Listbox()
    lisbox = Listbox(fen, fg="black", width=250)
    lisbox.place(x=700, y=470)

    # stringvar
    t1 = StringVar()
    t2 = StringVar()
    t3 = StringVar()
    t4 = StringVar()
    t5 = StringVar()
    t6 = StringVar()
    t7 = StringVar()

    # INTVAR
    v1 = IntVar()
    r1 = IntVar()
    r2 = IntVar()
    r3 = IntVar()

    # LES FONCTION
    def defCerche():
        pos = -1
        num = t3.get()
        for i in range(0, len(list)):
            if (list[i].numM == num):
                pos = i
        return pos

    def ajouter():
        numM = t1.get()
        nom = t2.get()
        oblipar=""
        if (v1.get() == 1):
            oblipar = "obligé"
        if (v1.get() == 2):
            oblipar = "Facultative"
        spésialiser = ld.get()

        e=modul(numM, nom, oblipar, spésialiser)
        list.append(e)
        messagebox.showinfo(" ", "c'est ajouter")

    def chercher():
        pos = defCerche()
        if (pos == -1):
            messagebox.showinfo(" ", "no exist")
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
            lisbox.insert(END,
                          f"num :{modul.numM} ## name: {modul.nom} ## oblipar :{modul.oblipar} ## spésialiser :{modul.spésialiser}")

    def modifier():
        pos = defCerche()
        if (pos == -1):
            messagebox.showinfo(" ", "no exist")
        else:
            messagebox.showinfo("", "exist")
            list[pos].numM = t1.get()
            list[pos].nom = t2.get()
            list[pos].spésialiser = ld.get()
            if (v1.get() == 1):
                oblipar = "obligatior"
            if (v1.get() == 2):
                oblipar = "Faculter"
            list[pos].oblipar = oblipar

    def suprimer():
        pos = defCerche()
        if (pos == -1):
            messagebox.showinfo(" ", "no exist")
        else:
            messagebox.showinfo(" ", "exist")
            list.pop(pos)
            messagebox.showinfo(" ", "c'est suprimer")

    # label
    l = Label(fen, text="NUM       :", fg="orange", bg="black", font=myStyle).place(y=50, x=70)
    l1 = Label(fen, text="NOM       :", fg="orange", bg="black", font=myStyle).place(y=140, x=70)
    l2 = Label(fen, text="spésialiser m :", fg="orange", bg="black", font="{arial} 19 bold").place(y=320, x=70)
    l3 = Label(fen, text="taper le num   :", fg="orange", bg="black", font=myStyle).place(y=40, x=640)
    l4 = Label(fen, text="NUM              :", fg="orange", bg="black", font=myStyle).place(y=220, x=680)
    l5 = Label(fen, text="NNOM            :", fg="orange", bg="black", font=myStyle).place(y=270, x=680)
    l6 = Label(fen, text="oblipar          :", fg="orange", bg="black", font=myStyle).place(y=320, x=680)
    l7 = Label(fen, text="spésialiser m:", fg="orange", bg="black", font=myStyle).place(y=370, x=680)

    # entry
    e = Entry(fen, border=2, textvariable=t1, fg="black", bg="white", font=myStyle).place(y=50, x=250, width=260,
                                                                                          height=40)
    e1 = Entry(fen, border=2, textvariable=t2, fg="black", bg="white", font=myStyle).place(y=140, x=250, width=260,
                                                                                           height=40)
    e2 = Entry(fen, border=2, textvariable=t3, fg="black", bg="white", font=myStyle).place(y=40, x=850, width=300,
                                                                                           height=40)
    e3 = Entry(fen, border=2, textvariable=t4, fg="black", bg="white", font=myStyle).place(y=220, x=880, width=240,
                                                                                           height=40)
    e4 = Entry(fen, border=2, textvariable=t5, fg="black", bg="white", font=myStyle).place(y=270, x=880, width=240,
                                                                                           height=40)
    e5 = Entry(fen, border=2, textvariable=t6, fg="black", bg="white", font=myStyle).place(y=320, x=880, width=240,
                                                                                           height=40)
    e6 = Entry(fen, border=2, textvariable=t7, fg="black", bg="white", font=myStyle).place(y=370, x=880, width=240,
                                                                                           height=40)

    # combobox
    ld = ttk.Combobox(fen, font=myStyle, value=listC)
    ld.place(y=320, x=250, width=260, height=40)
    ld.current(0)
    ld.bind("<<ComboxSelected>>")

    # radiobutton
    rB = Radiobutton(fen, fg="blue", font=style, bg="black", variable=v1, value=1, text="obligatoir").place(y=230, x=80)
    rB1 = Radiobutton(fen, fg="blue", font=style, bg="black", variable=v1, value=2, text="Facultative").place(y=230,
                                                                                                              x=300)

    # button
    b = Button(fen, text="AJOUTER", command=ajouter, borderwidth=4, font=style, bg="red", fg="white").place(y=430,
                                                                                                            x=110,
                                                                                                            width=170,
                                                                                                            height=60)
    b1 = Button(fen, text="VIDER", command=vider, borderwidth=4, font=style, bg="red", fg="white").place(y=430, x=300,
                                                                                                         width=170,
                                                                                                         height=60)
    b2 = Button(fen, text="CHERCHER", command=chercher, borderwidth=4, font=style2, bg="red", fg="white").place(y=100,
                                                                                                                x=615,
                                                                                                                width=140,
                                                                                                                height=50)
    b3 = Button(fen, text="MODIFIER", command=modifier, borderwidth=4, font=style2, bg="red", fg="white").place(y=100,
                                                                                                                x=760,
                                                                                                                width=140,
                                                                                                                height=50)
    b4 = Button(fen, text="SUPRIMER", command=suprimer, borderwidth=4, font=style2, bg="red", fg="white").place(y=100,
                                                                                                                x=905,
                                                                                                                width=140,
                                                                                                                height=50)
    b5 = Button(fen, text="LISTER", command=lister, borderwidth=4, font=style2, bg="red", fg="white").place(y=100,
                                                                                                            x=1050,
                                                                                                            width=140,
                                                                                                            height=50)
    b6 = Button(fen, text="vider", command=vider2, borderwidth=4, font=style2, bg="green", fg="white").place(y=415,
                                                                                                             x=1012,
                                                                                                             width=110,
                                                                                                             height=30)

    fen.mainloop()


b=Button(fen,text=" Gestion Prof  ",command=prof,border=2,bg="#343a40",font="century 20 bold",fg="black").place(x=100,y=100)
b1=Button(fen,text="Gestion Modul",command=modul,border=2,bg="#343a40",font="century 20 bold",fg="black").place(x=100,y=200)




fen.mainloop()