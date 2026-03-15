from tkinter import *
fen=Tk()
t1=StringVar()
r1=IntVar()
r2=IntVar()
r3=IntVar()
fen.geometry("400x500")
myStyle="{arial} 16 bold"
fen.resizable(False,False)
fen.title("calculatris")
fen.iconbitmap("20àç.ico")
l=Label(fen,bg="black").place(x=0,y=0,width=400,height=600)
l1=Label(fen,bg="blue",fg="black",text="choisir",font=myStyle).place(x=80,y=50,width=240,height=40)
def aficher():
    a=r1.get()
    b = r2.get()
    c = r3.get()
    ch=""
    if(a==1):
        ch=ch+" foot ."
    if (b == 1):
        ch = ch + " tenice ."
    if (c == 1):
        ch = ch + " basket ."
    t1.set(ch)
c1=Checkbutton(fen,font=myStyle,bg="black",fg="orange",text="footbal",variable=r1).place(x=100,y=100)
c2=Checkbutton(fen,font=myStyle,bg="black",fg="orange",text="tenice",variable=r2).place(x=100,y=150)
c3=Checkbutton(fen,font=myStyle,bg="black",fg="orange",text="basket",variable=r3).place(x=100,y=200)
b=Button(fen,bg="red",fg="black",text="afficher",command=aficher,font=myStyle).place(x=10,y=300,width=100,height=40)

l2=Label(fen,bg="orange",fg="black",text="var sport reverce",font=myStyle).place(x=10,y=350)
e1=Entry(fen,bg="white",fg="black",textvariable=t1,font=myStyle).place(x=200,y=350,width=200,height=30)






fen.mainloop()




