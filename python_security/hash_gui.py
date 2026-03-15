

#les from
from tkinter import *
import hashlib
from hash_utility import *
from tkinter import messagebox


#les fenétre
fen=Tk()
fen.title("hach")
fen.geometry("600x600")
fen.resizable(False,False)


#Style
style1="{arial} 20 bold"
style2="centry 18 bold"


#list
list=[]


#LES FONCTIO
def hach():
    global tx
    list.append(tx)
    for i in range (0,len(list)):
        file = open("text.txt", "a")
        file.write(str(list[i]))
        file.close()

        r = read()
        alltext = r.readlist("text.txt")
        for text in alltext:
            list.pop(i)
            text = text.rstrip("\n")
            text = text.encode("utf-8")
            h = hashlib.new("md5")
            h.update(text)
            hv = h.hexdigest()
            li.insert(END, f"le value de hash c'est :" + str(hv))
        messagebox.showinfo("", "vv")


#stringvar
tx=StringVar()


#Canvas
c=Canvas(fen,bg="black").place(x=0,y=0,width=600,height=600)


#label
l=Label(fen,bg="black",fg="orange",font=style1,text="Entrer le TEXT")
l.place(x=20,y=20)
l1=Label(fen,bg="black",fg="red",font="bold 30",text=":")
l1.place(x=230,y=11)


#Entry
e=Entry(fen,textvariable=tx,font=style1)
e.place(x=20,y=80,width=560,height=50)


#button
b=Button(fen,command=hach,borderwidth=5,text="haching",font=style2,bg="black",fg="red")
b.place(x=200,y=160 ,width=200 ,height=50)


#listbox
li=Listbox(fen)
li.place(x=20,y=250,width=560,height=300)


fen.mainloop()

