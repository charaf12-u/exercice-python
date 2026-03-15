from tkinter import *
fen=Tk()
fen.geometry("600x600")
fen.title("calculer")
l1=Label(fen,bg="black").place(x=0,y=0,width=600,height=600)
fen.iconbitmap('20àç.ico')
myStyle="{arial} 22 bold"
t1=StringVar()
t2=StringVar()



pd=""
#def press(num):
def press(userInput):
    global pd
    pd=pd+str(userInput)
    t1.set(pd)
def AC():
    global pd
    pd=""
    pd.set("")

def result():
    try:
        global pd
        res=str(eval(pd))
        t2.set(res)
        t1.set(" ")
        pd = ""
    except:
        t2.set("erour")

e1=Entry(fen,font=myStyle,bg="white",fg="black",textvariable=t1).place(x=100,y=50,width=400,height=50)
b1=Button(fen,text=".",command=lambda: press('.'), font=myStyle,bg="orange",fg="black").place(x=130,y=130,width=40,height=40)
b2=Button(fen,text="1", command=lambda: press(1), font=myStyle,bg="orange",fg="black").place(x=230,y=130,width=40,height=40)
b3=Button(fen,text="2", command=lambda: press(2), font=myStyle,bg="orange",fg="black").place(x=330,y=130,width=40,height=40)
b4=Button(fen,text="3", command=lambda: press(3), font=myStyle,bg="orange",fg="black").place(x=430,y=130,width=40,height=40)
b5=Button(fen,text="4", command=lambda: press(4), font=myStyle,bg="orange",fg="black").place(x=130,y=230,width=40,height=40)
b6=Button(fen,text="5", command=lambda: press(5), font=myStyle,bg="orange",fg="black").place(x=230,y=230,width=40,height=40)
b7=Button(fen,text="6", command=lambda: press(6), font=myStyle,bg="orange",fg="black").place(x=330,y=230,width=40,height=40)
b8=Button(fen,text="7", command=lambda: press(7), font=myStyle,bg="orange",fg="black").place(x=430,y=230,width=40,height=40)
b9=Button(fen,text="8", command=lambda: press(8), font=myStyle,bg="orange",fg="black").place(x=130,y=330,width=40,height=40)
b10=Button(fen,text="9",command=lambda: press(9), font=myStyle,bg="orange",fg="black").place(x=230,y=330,width=40,height=40)
b11=Button(fen,text="0",command=lambda: press(0), font=myStyle,bg="orange",fg="black").place(x=330,y=330,width=40,height=40)
b12=Button(fen,text="+",command=lambda: press('+'),font=myStyle,bg="orange",fg="black").place(x=430,y=330,width=40,height=40)
b13=Button(fen,text="/",command=lambda: press('/'),font=myStyle,bg="orange",fg="black").place(x=130,y=430,width=40,height=40)
b14=Button(fen,text="-",command=lambda: press('-'),font=myStyle,bg="orange",fg="black").place(x=230,y=430,width=40,height=40)
b15=Button(fen,text="*",command=lambda: press('*'),font=myStyle,bg="orange",fg="black").place(x=330,y=430,width=40,height=40)
b17=Button(fen,text="AC",command=AC,font=myStyle,bg="orange",fg="black").place(x=530,y=430,width=40,height=40)

b16=Button(fen,text="=",command=result,font=myStyle,bg="orange",fg="black").place(x=430,y=430,width=40,height=40)
e2=Entry(fen,font=myStyle,bg="white",fg="black",textvariable=t2).place(x=100,y=500,width=400,height=50)












fen.mainloop()