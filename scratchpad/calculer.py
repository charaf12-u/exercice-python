from tkinter import *
fen=Tk()
fen.geometry("600x600")
fen.title("calculer")
l1=Label(fen,bg="black").place(x=0,y=0,width=600,height=600)
fen.iconbitmap('20àç.ico')
myStyle="{arial} 22 bold"
t1=StringVar()

op=""
b=0
a=0
ch=""

def AC():
    global ch
    ch = ""
    t1.set("")
def N1():
    global a
    a = "1"
    t1.set(a)
    t1.get()
def N2():
    global a
    a = "2"
    t1.set(a)
    t1.get()


def N3():
    global a
    a = "3"
    t1.set(a)
    t1.get()
def N4():
    global a
    a = "4"
    t1.set(a)
    t1.get()
def N5():
    global a
    a = "5"
    t1.set(a)
    t1.get()
def N6():
    global a
    a = "6"
    t1.set(a)
    t1.get()
def N7():
    global a
    a = "7"
    t1.set(a)
    t1.get()
def N8():
    global a
    a = "8"
    t1.set(a)
    t1.get()
def N9():
    global a
    a = "9"
    t1.set(a)
    t1.get()
def N0():
    global a
    a = "0"
    t1.set(a)
    t1.get()
def ADD():
    global op
    global b
    global ch
    b=a
    op="+"
    t1.set(op)
    ch=""
def MUL():
    global op
    global b
    global ch
    b = a
    op = "/"
    t1.set(op)
    ch = ""
def RSL():
    t1.set("")
    if(op=="+"):
        res=int(b)+int(a)
        t1.set(res)
    if (op == "-"):
        res = int(b) - int(a)
        t1.set(res)
    if (op == "*"):
        res = int(b) * int(a)
        t1.set(res)
    if (op == "/"):
        res = int(b) + int(a)
        t1.set(res)
def DIV():
    global op
    global b
    global ch
    b = a
    op = "*"
    t1.set(op)
    ch = ""
def N9S():
    global op
    global b
    global ch
    b = a
    op = "-"
    t1.set(op)
    ch = ""

e1=Entry(fen,font=myStyle,bg="white",fg="black",textvariable=t1).place(x=100,y=50,width=400,height=50)
b1=Button(fen,text="AC",command=AC, font=myStyle,bg="red"   ,fg="black").place(x=130,y=130,width=40,height=40)
b2=Button(fen,text="1", command=N1, font=myStyle,bg="orange",fg="black").place(x=230,y=130,width=40,height=40)
b3=Button(fen,text="2", command=N2, font=myStyle,bg="orange",fg="black").place(x=330,y=130,width=40,height=40)
b4=Button(fen,text="3", command=N3, font=myStyle,bg="orange",fg="black").place(x=430,y=130,width=40,height=40)
b5=Button(fen,text="4", command=N4, font=myStyle,bg="orange",fg="black").place(x=130,y=230,width=40,height=40)
b6=Button(fen,text="5", command=N5, font=myStyle,bg="orange",fg="black").place(x=230,y=230,width=40,height=40)
b7=Button(fen,text="6", command=N6, font=myStyle,bg="orange",fg="black").place(x=330,y=230,width=40,height=40)
b8=Button(fen,text="7", command=N7, font=myStyle,bg="orange",fg="black").place(x=430,y=230,width=40,height=40)
b9=Button(fen,text="8", command=N8, font=myStyle,bg="orange",fg="black").place(x=130,y=330,width=40,height=40)
b10=Button(fen,text="9",command=N9, font=myStyle,bg="orange",fg="black").place(x=230,y=330,width=40,height=40)
b11=Button(fen,text="0",command=N0, font=myStyle,bg="orange",fg="black").place(x=330,y=330,width=40,height=40)
b12=Button(fen,text="+",command=ADD,font=myStyle,bg="orange",fg="black").place(x=430,y=330,width=40,height=40)
b13=Button(fen,text="/",command=MUL,font=myStyle,bg="orange",fg="black").place(x=130,y=430,width=40,height=40)
b14=Button(fen,text="-",command=N9S,font=myStyle,bg="orange",fg="black").place(x=230,y=430,width=40,height=40)
b15=Button(fen,text="*",command=DIV,font=myStyle,bg="orange",fg="black").place(x=330,y=430,width=40,height=40)
b16=Button(fen,text="=",command=RSL,font=myStyle,bg="orange",fg="black").place(x=430,y=430,width=40,height=40)
e2=Label(fen,font=myStyle,bg="blue",fg="black",text="calculer").place(x=100,y=500,width=400,height=40)












fen.mainloop()