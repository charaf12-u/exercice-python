from tkinter import *
root=Tk()
root.geometry("600x600")
myStyle="{ariale} 21 bold"
root.title("edition")
root.iconbitmap("20àç.ico")
root.resizable(False,False)
l=Label(root,font=myStyle,bg="black",fg="white").place(x=0,y=0,width=600,height=600)
t1=StringVar()
t2=StringVar()
def vider():
    t1.set("")
def combter():
    ch=t1.get()
    l=len(ch)
    t2.set(l)
def copier():
    ch = t1.get()
    t2.set(ch)
def coper():
    ch = t1.get()
    t2.set(ch)
    t1.set("")
def revers():
    ch=t1.get()
    l=len(ch)
    ch1=""
    for i in range(0,l):
        ch1=ch1+ch[l-i-1]
    t2.set(ch1)
def nb():
    l=['a','e','u','i','o','A','E','U','I','O']
    ch=t1.get()
    l1=len(ch)
    cp=0
    for i in range(0,l1):
        if ch[i] in l:
            cp=cp+1
    t2.set(cp)
l1=Label(root,font=myStyle,text="entrer une chaine",bg="white",fg="black").place(x=50,y=50,width=240)
e1=Entry(root,font=myStyle,textvariable=t1,bg="orange",fg="blue").place(x=300,y=50,width=250)
b1=Button(root,font=myStyle,bg="red",fg="white",command=vider,text="vider",border="0").place(x=100,y=115,width=150)
b2=Button(root,font=myStyle,bg="red",fg="white",command=combter,text="combter",border="0").place(x=350,y=115,width=150)
b3=Button(root,font=myStyle,bg="red",fg="white",command=copier,text="copier",border="0").place(x=100,y=215,width=150)
b4=Button(root,font=myStyle,bg="red",fg="white",command=coper,text="coper",border="0").place(x=350,y=215,width=150)
b5=Button(root,font=myStyle,bg="red",fg="white",command=revers,text="revers",border="0").place(x=100,y=315,width=150)
b6=Button(root,font=myStyle,bg="red",fg="white",command=nb,text="nb",border="0").place(x=350,y=315,width=150)


l2=Label(root,font=myStyle,text="resultat",bg="white",fg="black").place(x=50,y=395,width=240)
e2=Entry(root,font=myStyle,textvariable=t2,bg="orange",fg="blue").place(x=300,y=395,width=250)

root.mainloop()