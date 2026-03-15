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
    global ch
    global a
    global b
    a="1"
    ch=ch+a
    t1.set(ch)
def N2():
    global ch
    global a
    global b
    a = "2"
    ch = ch + a
    t1.set(ch)


def N3():
    global ch
    global a
    global b
    a = "3"
    ch = ch + a
    t1.set(ch)
def N4():
    global ch
    global a
    global b
    a = "4"
    ch = ch + a
    t1.set(ch)
def N5():
    global ch
    global a
    global b
    a = "5"
    ch = ch + a
    t1.set(ch)
def N6():
    global ch
    global a
    global b
    a = "6"
    ch = ch + a
    t1.set(ch)
def N7():
    global a
    global ch
    global a
    global b
    a = "7"
    ch = ch + a
    t1.set(ch)
def N8():
    global ch
    global a
    global b
    a = "8"
    ch = ch + a
    t1.set(ch)
def N9():
    global ch
    global a
    global b
    a = "9"
    ch = ch + a
    t1.set(ch)
def N0():
    global ch
    global a
    global b
    a = "0"
    ch = ch + a
    t1.set(ch)
def ADD():
    global op
    global b
    global ch
    b=a
    op="+"
    ch=ch+op
    t1.set(ch)

def MUL():
    global op
    global b
    global ch
    b = a
    op = "/"
    ch = ch + op
    t1.set(ch)

def RSL():
    t1.set("")
    if (op == "+"):
        res = int(b) + int(a)
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
    ch = ch + op
    t1.set(ch)
def N9S():
    global op
    global b
    global ch
    b = a
    op = "-"
    ch = ch + op
    t1.set(ch)

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