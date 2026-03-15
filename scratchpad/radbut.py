from tkinter import *
root=Tk()
def calcules():
    a=v1.get()
    if(a==1):
        c = t1.get()
        b = t2.get()
        s = int(c) + int(b)
        t3.set(s)
    if (a == 2):
        c = t1.get()
        b = t2.get()
        s = int(c) / int(b)
        t3.set(s)
    if (a == 3):
        c = t1.get()
        b = t2.get()
        s = int(c) * int(b)
        t3.set(s)
    if (a == 4):
        c = t1.get()
        b = t2.get()
        s = int(c) - int(b)
        t3.set(s)
v1=IntVar()
t1=StringVar()
t2=StringVar()
t3=StringVar()
root.geometry("400x500")
root.title("calucatris")
root.iconbitmap("20àç.ico")
myStyle="{arial} 21 bold"
root.resizable(True , True)
l=Label(root,font=myStyle,bg="black",fg="white").place(x=0,y=0,width=400,height=500)
l1=Label(root,font=myStyle,text="taper nomber").place(x=22,y=12)
e1=Entry(root,font=myStyle,textvariable=t1,bg="orange",fg="white",border="0").place(x=222,y=12,width=141,height=38)
l2=Label(root,font=myStyle,text="taper nomber").place(x=22,y=73)
e2=Entry(root,font=myStyle,textvariable=t2,bg="orange",fg="white",border="0").place(x=222,y=73,width=141,height=38)
r1=Radiobutton(root,fg="black",variable=v1,value=1,text="SOMME").place(x=33 ,y=140,width=81,height=30)
r2=Radiobutton(root,fg="black",variable=v1,value=2,text="DIV").place(x=33 ,y=200,width=81,height=30 )
r3=Radiobutton(root,fg="black",variable=v1,value=3,text="MUL").place(x=33 ,y=270,width=81,height=30 )
r4=Radiobutton(root,fg="black",variable=v1,value=4,text="DIFF").place(x=33 ,y=340,width=81,height=30 )




b=Button(root,font=myStyle,text="calcules",command=calcules).place(x=22,y=400)
e3=Entry(root,font=myStyle,textvariable=t3,bg="orange",fg="white",border="0").place(x=222,y=405,width=141,height=45)

root.mainloop()