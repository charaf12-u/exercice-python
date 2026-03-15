#install import required libraries (tkinter , time , detetime , winsound , threading )
from tkinter import *
import datetime
import time
import winsound
import threading

def Threading():
    t1=threading.Thread(target=alarm)
    t1.start()

def alarm():
    while True:
        if hour.get() == minute.get() == seconde.get() == '00' :
            #print('please , select time!')
            state.config(text="please , select time!")
            break
        else:
            state.config(text="alarm started")
            user = f"{hour.get()}:{minute.get()}:{seconde.get()}"
            time.sleep(1)
            currentTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(user, currentTime)
            if user == currentTime:
                state.config(text="Time to wake up!")
                winsound.PlaySound(
                    r"C:\Users\Dell\Pictures\Ai\alarm-clock-short-6402.wav",
                    winsound.SND_ALIAS
                )
                hour.set(hours[0])
                minute.set(hours[0])
                seconde.set(hours[0])
                print("Time to wake up!")
                break


#design opp using tkinter
master=Tk()
master.geometry("400x250")
master.title("Alarm klock")
ph=PhotoImage(file=r"calculatrice.png")
master.iconphoto(False,ph)
appTitle=Label(master,text="Alarm",font=("century 21 bold"))
appTitle.pack()
setTime=Label(master,text="set Time",font=("century 15"))
setTime.pack(pady=11)
frame=Frame(master)
frame.pack()
#hours=('00','01','02','03','04','05','06','07',
 #      '08','09','10','11','12','13','14','15',
  #     '16','17','18','19','20','21','22','23','24')

hour=StringVar(master)
hours=[]
for num in range(0,25):
    if num <= 9 :
        num ='0' +str(num)
    hours.append(num)
hrs= OptionMenu(frame,hour, *hours)
hrs.pack(side=LEFT)
hrs.config(font=("centry 13 bold"))
hour.set(hours[0])


minute=StringVar(master)
minutes=[]
for num in range(0,61):
    if num <= 9 :
        num ='0' +str(num)
    minutes.append(num)
minu= OptionMenu(frame,minute, *minutes)
minu.pack(side=LEFT)
minu.config(font=("centry 13 bold"))
minute.set(minutes[0])


seconde=StringVar(master)
secondes=[]
for num in range(0,61):
    if num <= 9 :
        num ='0' +str(num)
    secondes.append(num)
sec= OptionMenu(frame,seconde, *secondes)
sec.pack(side=LEFT)
sec.config(font=("centry 13 bold"))
seconde.set(secondes[0])



btn=Button(master,text="start alarm" ,command=Threading,font=("contry 15 bold"),fg="white",bg="blue")
btn.pack(pady=11)

state=Label(master,font="arial 12 bold",fg="orange")
state.pack()


master.mainloop()

