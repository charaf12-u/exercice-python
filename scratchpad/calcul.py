from tkinter import *
fen=Tk()
r=""
a=0
def somme():
    global r
    global a
    r="+"
    a = int(input())
    t1.set(r)
    t1.set(a)
def add():
    r = "-"
    a = int(input())
    t1.set(a)
def l9isma():
    r = "/"
    a = int(input())
    t1.set(a)
def mul():
    r = "*"
    a = int(input())
    t1.set(a)
def calcules():
    s=int(a),r,int(a)
    t2.set(s)
fen.geometry("600x600")
t1=StringVar
t2=StringVar
l3=Label(fen,bg="black").place(x=0,y=0,width=600,height=600)

l1=Label(fen,text="taper les nomber",fg="white",bg="blue").place(x=22,y=12,width=160,height="40")

l2=Entry(fen,textvariable=t1,bg="orange",fg="white",border="0").place(x=222,y=12,width=141,height=38)

b=Button(fen,bg="red",fg="black",text=" + ",command=somme,border="0").place(x=60,y=160,width=41,height=35)
b1=Button(fen,bg="red",fg="black",text=" - ",command=add,border="0").place(x=160,y=160,width=41,height=35)
b2=Button(fen,bg="red",fg="black",text=" / ",command=l9isma,border="0").place(x=260,y=160,width=41,height=35)

b3=Button(fen,bg="red",fg="black",text=" 1 ",command=mul,border="0").place(x=60,y=230,width=41,height=35)
b4=Button(fen,bg="red",fg="black",text=" 2 ",command=somme,border="0").place(x=160,y=230,width=41,height=35)
b5=Button(fen,bg="red",fg="black",text=" 3 ",command=add,border="0").place(x=260,y=230,width=41,height=35)

b6=Button(fen,bg="red",fg="black",text=" 4 ",command=l9isma,border="0").place(x=60,y=290,width=41,height=35)
b7=Button(fen,bg="red",fg="black",text=" 5 ",command=mul,border="0").place(x=160,y=290,width=41,height=35)
b8=Button(fen,bg="red",fg="black",text=" 6 ",command=somme,border="0").place(x=260,y=290,width=41,height=35)

b9=Button(fen,bg="red",fg="black",text=" 7 ",command=add,border="0").place(x=60,y=350,width=41,height=35)
b10=Button(fen,bg="red",fg="black",text=" 8 ",command=l9isma,border="0").place(x=160,y=350,width=41,height=35)
b11=Button(fen,bg="red",fg="black",text=" 9 ",command=mul,border="0").place(x=260,y=350,width=41,height=35)

b12=Button(fen,bg="red",fg="black",text=" 0 ",command=add,border="0").place(x=60,y=410,width=41,height=35)
b13=Button(fen,bg="red",fg="black",text=" . ",command=l9isma,border="0").place(x=160,y=410,width=41,height=35)
b14=Button(fen,bg="red",fg="black",text=" = ",command=mul,border="0").place(x=260,y=410,width=41,height=35)


l5=Button(fen,text="CALCULES" ,command=calcules).place(x=30,y=490,width=160,height="40")
l6=Entry(fen,textvariable=t2,bg="blue",fg="white",border="0").place(x=230,y=490,width=141,height=38)

fen.mainloop()