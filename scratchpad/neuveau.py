from tkinter import *
fen=Tk()
t1=StringVar()
myStyl="{arial} 17 bold"
fen.geometry("700x580")
l=Label(fen,bg="black",fg="white").place(width=700,height=580)
fen.resizable(True,True)
fen.title("dev104")
fen.iconbitmap('20àç.ico')
l1=Label(fen,font=myStyl,text="bonjour", bg="black",fg="white" ).place(x=19 , y=19)
e=Entry(fen,font=myStyl,textvariable=t1, bg="orange",fg="white" ).place(x=200 , y=19,width=233,height=60)



fen.mainloop()

