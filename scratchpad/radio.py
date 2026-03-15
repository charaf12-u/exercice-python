from tkinter import *
root=Tk()
def display():
    a=v1.get()
    if(a==1):
        t1.set("bac")
    if (a == 2):
        t1.set("dueg")
    if (a == 3):
        t1.set("master")
v1=IntVar()
t1=StringVar()
root.geometry("500x500")
styl="{arial} 21 bold"
l=Label(root,bg="orange",font=styl).place(x=0,y=0,width=500,height=500)
l2=Label(root,font=styl,text="Chose your gradiat",fg="black").place(x=40 ,y=40 )

r1=Radiobutton(root,fg="black",variable=v1,value=1,text="bac").place(x=40 ,y=100 )
r2=Radiobutton(root,fg="black",variable=v1,value=2,text="deug").place(x=40 ,y=200 )
r3=Radiobutton(root,fg="black",variable=v1,value=3,text="master").place(x=40 ,y=300 )
l1=Button(root,font=styl,text="your diplom :",fg="black",command=display).place(x=40 ,y=400 )
e1=Entry(root,textvariable=t1,font=styl,bg="black",fg="blue").place(x=250 ,y=400 )
root.mainloop()