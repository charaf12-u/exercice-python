from tkinter import *
root=Tk()
def afficher():
    ch=t1.get()
    t2.set(ch)
root.geometry("600x600")
root.title("afficher")
root.iconbitmap("20àç.ico")
myStyl="{arial} 18 bold"
t1=StringVar()
t2=StringVar()
l3=Label(root,font=myStyl,bg="black",fg="white").place(x=0,y=0,width=600,height=600)
l=Label(root,font=myStyl,text="taper le nom",bg="black",fg="white").place(x=100,y=50)
e=Entry(root,font=myStyl,textvariable=t1,bg="orange",fg="blue").place(x=300,y=50,width=131,height=33)
l1=Label(root,font=myStyl,text="votre nom est",bg="black",fg="white").place(x=100,y=250)
e1=Entry(root,font=myStyl,textvariable=t2,bg="orange",fg="blue").place(x=300,y=250,width=131,height=33)
b=Button(root,font=myStyl,bg="red",fg="black",text="afficher",command=afficher,border="0").place(x=100,y=150)


root.mainloop()