from tkinter import *
fen=Tk()
a=0
b=0
ch=""
c=""
def bt1():
    global ch
    global a
    a="1"
    ch=ch+a
    t1.set(ch)

def bt2():
    global ch
    global a
    a = "2"
    ch = ch + a
    t1.set(ch)
def bt3():
    global ch
    global a
    a = "3"
    ch = ch + a
    t1.set(ch)
def bt4():
    global ch
    global a
    a = "4"
    ch = ch + a
    t1.set(ch)
def bt5():
    global ch
    global a
    a = "5"
    ch = ch + a
    t1.set(ch)
def bt6():
    global ch
    global a
    a = "6"
    ch = ch + a
    t1.set(ch)
def bt7():
    global ch
    global a
    a = "7"
    ch = ch + a
    t1.set(ch)
def bt8():
    global ch
    global a
    a = "8"
    ch = ch + a
    t1.set(ch)
def bt9():
    global ch
    global a
    a = "ç"
    ch = ch + a
    t1.set(ch)
def bt0():
    global ch
    global a
    a = "0"
    ch = ch + a
    t1.set(ch)
def point():
    global ch
    global a
    a = "."
    ch = ch + a
    t1.set(ch)
def somme():
    global ch
    global a
    c = "+"
    ch = ch + c
    t1.set(ch)
def div():
    global ch
    global a
    c = "*"
    ch = ch + c
    t1.set(ch)
def n9s():
    global ch
    global a
    c = "-"
    ch = ch + c
    t1.set(ch)
def mul():
    global ch
    global a
    c = "/"
    ch = ch + c
    t1.set(ch)
def RSL():
    t1.set("")
    try:
        s=eval(ch)
        t1.set(s)
    except:
        t1.set("erour")
def AC():
    global ch
    t1.set("")
    ch=""

fen.geometry("600x600")
fen.resizable(False,False)
l=Canvas(fen,bg="black",).place(x=0,y=0,width=600,height=600)
fen.title("calculatrice")
ph=PhotoImage(file="15361.png")
ph1=PhotoImage(file="calculatrice.png")
fen.iconphoto(True, ph1)
l1=Label(fen,image=ph,bg="black").place(x=20,y=10)
myStyle="{arial} 21 bold"
t1=StringVar()
l2=Label(fen,text="calculer",font="{arial} 18 bold",bg="black",fg="orange").place(x=42,y=4)
e=Entry(fen, borderwidth=7,textvariable=t1,font=myStyle).place(x=145,y=50,width=348,height=45)

b0=Button(fen, borderwidth=3,text="+",font=myStyle,bg="red",fg="black",command=somme).place(x=130,y=150,height=40,width=40)
b1=Button(fen, borderwidth=3,text="-",font=myStyle,bg="red",fg="black",command=n9s).  place(x=230,y=150,height=40,width=40)
b2=Button(fen, borderwidth=3,text="*",font=myStyle,bg="red",fg="black",command=div).  place(x=330,y=150,height=40,width=40)
b3=Button(fen, borderwidth=3,text="/",font=myStyle,bg="red",fg="black",command=mul).  place(x=430,y=150,height=40,width=40)

b4=Button(fen,border="3.5",text="1",font=myStyle,bg="orange",fg="black",command=bt1).place(x=130,y=230,height=40,width=40)
b5=Button(fen,border="3.5",text="2",font=myStyle,bg="orange",fg="black",command=bt2).place(x=230,y=230,height=40,width=40)
b6=Button(fen,border="3.5",text="3",font=myStyle,bg="orange",fg="black",command=bt3).place(x=330,y=230,height=40,width=40)
b7=Button(fen,border="3.5",text="4",font=myStyle,bg="orange",fg="black",command=bt4).place(x=430,y=230,height=40,width=40)

b8=Button( fen,border="3.5",text="5",font=myStyle,bg="orange",fg="black",command=bt5).place(x=130,y=310,height=40,width=40)
b9=Button( fen,border="3.5",text="6",font=myStyle,bg="orange",fg="black",command=bt6).place(x=230,y=310,height=40,width=40)
b10=Button(fen,border="3.5",text="7",font=myStyle,bg="orange",fg="black",command=bt7).place(x=330,y=310,height=40,width=40)
b11=Button(fen,border="3.5",text="8",font=myStyle,bg="orange",fg="black",command=bt8).place(x=430,y=310,height=40,width=40)

b12=Button(fen, border="3.5", text="9", font=myStyle,bg="orange", fg="black",command=bt9).  place(x=130,y=390  ,height=40,width=40)
b13=Button(fen, border="3.5", text="0", font=myStyle,bg="orange", fg="black",command=bt0).  place(x=230,y=390  ,height=40,width=40)
b14=Button(fen, border="3.5", text=".", font=myStyle,bg="orange", fg="black",command=point).place(x=330,y=390 ,height=40,width=40)
b15=Button(fen, borderwidth=3,text="=", font=myStyle,bg="blue",   fg="black",command=RSL).  place(x=430,y=380  ,height=55,width=40)
b16=Button(fen, borderwidth=3,text="AC",font=myStyle,bg="#00A896",fg="black",command=AC).   place(x=100,y=50   ,height=47,width=43)




fen.mainloop()