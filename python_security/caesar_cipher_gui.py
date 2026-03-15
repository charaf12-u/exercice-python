#form
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from caesar_utility import *

#fenéter
fen=Tk()
fen.title('cripty on kaysar')
fen.geometry('1000x600')
fen.resizable(False,False)

#list
text=[]
list=[]

#les fonction
def encrypt():
    g=tx.get()
    j=0
    for j in range(0,len(g)):

        text.append(g[j])
        j=j+1
    if(text==''):
        messagebox.showerror('ERROR','Taper un chain')
    else:
        i = 0
        for i in range(0, len(text)):
            if (text[i] == 'a' or text[i] == 'A'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    cr = 'a'

                if (b == 1):
                    cr = 'b'
                if (b == 2):
                    cr = 'c'
                if (b == 3):
                    cr = 'd'
                if (b == 4):
                    cr = 'e'
                if (b == 5):
                    cr = 'f'
                if (b == 6):
                    cr = 'g'
                if (b == 7):
                    cr = 'h'
                if (b == 8):
                    cr = 'i'
                if (b == 9):
                    cr = 'j'
                if (b == 10):
                    cr = 'k'
                if (b == 11):
                    cr = 'l'
                if (b == 12):
                    cr = 'm'
                if (b == 13):
                    cr='n'
                    e = kaysar(cr)
                    list.append(e)
                if (b == 14):
                    cr = 'o'
                if (b == 15):
                    cr = 'p'
                if (b == 16):
                    cr = 'q'
                if (b == 17):
                    cr = 'r'
                if (b == 18):
                    cr = 's'
                if (b == 19):
                    cr = 't'
                if (b == 20):
                    cr = 'u'
                if (b == 21):
                    cr = 'v'
                if (b == 22):
                    cr = 'w'
                if (b == 23):
                    cr = 'x'
                if (b == 24):
                    cr = 'y'
                if (b == 25):
                    cr = 'z'


                li.delete(0, END)
                for kaysar in list:
                    li.insert(END,
                                  f"crypt :{kaysar.c}")

            if (text[i] == 'b' or text[i] == 'B'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                if (b == 1):
                    c = 'b'
                if (b == 2):
                    c = 'c'
                if (b == 3):
                    c = 'd'
                if (b == 4):
                    c = 'e'
                if (b == 5):
                    c = 'f'
                if (b == 6):
                    c = 'g'
                if (b == 7):
                    c = 'h'
                if (b == 8):
                    c = 'i'
                if (b == 9):
                    c = 'j'
                if (b == 10):
                    c = 'k'
                if (b == 11):
                    c = 'l'
                if (b == 12):
                    c = 'm'
                if (b == 13):
                    c = 'n'
                if (b == 14):
                    c = 'o'
                if (b == 15):
                    c = 'p'
                if (b == 16):
                    c = 'q'
                if (b == 17):
                    c = 'r'
                if (b == 18):
                    c = 's'
                if (b == 19):
                    c = 't'
                if (b == 20):
                    c = 'u'
                if (b == 21):
                    c = 'v'
                if (b == 22):
                    c = 'w'
                if (b == 23):
                    c = 'x'
                if (b == 24):
                    c = 'y'
                if (b == 25):
                    c = 'z'
                li.insert(tk.END, c)
            if (text[i] == 'c' or text[i] == 'C'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                if (b == 1):
                    c = 'b'
                if (b == 2):
                    c = 'c'
                if (b == 3):
                    c = 'd'
                if (b == 4):
                    c = 'e'
                if (b == 5):
                    c = 'f'
                if (b == 6):
                    c = 'g'
                if (b == 7):
                    c = 'h'
                if (b == 8):
                    c = 'i'
                if (b == 9):
                    c = 'j'
                if (b == 10):
                    c = 'k'
                if (b == 11):
                    c = 'l'
                if (b == 12):
                    c = 'm'
                if (b == 13):
                    c = 'n'
                if (b == 14):
                    c = 'o'
                if (b == 15):
                    c = 'p'
                if (b == 16):
                    c = 'q'
                if (b == 17):
                    c = 'r'
                if (b == 18):
                    c = 's'
                if (b == 19):
                    c = 't'
                if (b == 20):
                    c = 'u'
                if (b == 21):
                    c = 'v'
                if (b == 22):
                    c = 'w'
                if (b == 23):
                    c = 'x'
                if (b == 24):
                    c = 'y'
                if (b == 25):
                    c = 'z'
                li.insert(tk.END, c)
            if (text[i] == 'd' or text[i] == 'D'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                if (b == 1):
                    c = 'b'
                if (b == 2):
                    c = 'c'
                if (b == 3):
                    c = 'd'
                if (b == 4):
                    c = 'e'
                if (b == 5):
                    c = 'f'
                if (b == 6):
                    c = 'g'
                if (b == 7):
                    c = 'h'
                if (b == 8):
                    c = 'i'
                if (b == 9):
                    c = 'j'
                if (b == 10):
                    c = 'k'
                if (b == 11):
                    c = 'l'
                if (b == 12):
                    c = 'm'
                if (b == 13):
                    c = 'n'
                if (b == 14):
                    c = 'o'
                if (b == 15):
                    c = 'p'
                if (b == 16):
                    c = 'q'
                if (b == 17):
                    c = 'r'
                if (b == 18):
                    c = 's'
                if (b == 19):
                    c = 't'
                if (b == 20):
                    c = 'u'
                if (b == 21):
                    c = 'v'
                if (b == 22):
                    c = 'w'
                if (b == 23):
                    c = 'x'
                if (b == 24):
                    c = 'y'
                if (b == 25):
                    c = 'z'
                li.insert(tk.END, c)
            if (text[i] == 'e' or text[i] == 'E'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                if (b == 1):
                    c = 'b'
                if (b == 2):
                    c = 'c'
                if (b == 3):
                    c = 'd'
                if (b == 4):
                    c = 'e'
                if (b == 5):
                    c = 'f'
                if (b == 6):
                    c = 'g'
                if (b == 7):
                    c = 'h'
                if (b == 8):
                    c = 'i'
                if (b == 9):
                    c = 'j'
                if (b == 10):
                    c = 'k'
                if (b == 11):
                    c = 'l'
                if (b == 12):
                    c = 'm'
                if (b == 13):
                    c = 'n'
                if (b == 14):
                    c = 'o'
                if (b == 15):
                    c = 'p'
                if (b == 16):
                    c = 'q'
                if (b == 17):
                    c = 'r'
                if (b == 18):
                    c = 's'
                if (b == 19):
                    c = 't'
                if (b == 20):
                    c = 'u'
                if (b == 21):
                    c = 'v'
                if (b == 22):
                    c = 'w'
                if (b == 23):
                    c = 'x'
                if (b == 24):
                    c = 'y'
                if (b == 25):
                    c = 'z'
                li.insert(tk.END, c)
            if (text[i] == 'f' or text[i] == 'F'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                if (b == 1):
                    c = 'b'
                if (b == 2):
                    c = 'c'
                if (b == 3):
                    c = 'd'
                if (b == 4):
                    c = 'e'
                if (b == 5):
                    c = 'f'
                if (b == 6):
                    c = 'g'
                if (b == 7):
                    c = 'h'
                if (b == 8):
                    c = 'i'
                if (b == 9):
                    c = 'j'
                if (b == 10):
                    c = 'k'
                if (b == 11):
                    c = 'l'
                if (b == 12):
                    c = 'm'
                if (b == 13):
                    c = 'n'
                if (b == 14):
                    c = 'o'
                if (b == 15):
                    c = 'p'
                if (b == 16):
                    c = 'q'
                if (b == 17):
                    c = 'r'
                if (b == 18):
                    c = 's'
                if (b == 19):
                    c = 't'
                if (b == 20):
                    c = 'u'
                if (b == 21):
                    c = 'v'
                if (b == 22):
                    c = 'w'
                if (b == 23):
                    c = 'x'
                if (b == 24):
                    c = 'y'
                if (b == 25):
                    c = 'z'
                li.insert(tk.END, c)
            if (text[i] == 'g' or text[i] == 'G'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                if (b == 1):
                    c = 'b'
                if (b == 2):
                    c = 'c'
                if (b == 3):
                    c = 'd'
                if (b == 4):
                    c = 'e'
                if (b == 5):
                    c = 'f'
                if (b == 6):
                    c = 'g'
                if (b == 7):
                    c = 'h'
                if (b == 8):
                    c = 'i'
                if (b == 9):
                    c = 'j'
                if (b == 10):
                    c = 'k'
                if (b == 11):
                    c = 'l'
                if (b == 12):
                    c = 'm'
                if (b == 13):
                    c = 'n'
                if (b == 14):
                    c = 'o'
                if (b == 15):
                    c = 'p'
                if (b == 16):
                    c = 'q'
                if (b == 17):
                    c = 'r'
                if (b == 18):
                    c = 's'
                if (b == 19):
                    c = 't'
                if (b == 20):
                    c = 'u'
                if (b == 21):
                    c = 'v'
                if (b == 22):
                    c = 'w'
                if (b == 23):
                    c = 'x'
                if (b == 24):
                    c = 'y'
                if (b == 25):
                    c = 'z'
                li.insert(tk.END, c)
            if (text[i] == 'h' or text[i] == 'H'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                if (b == 1):
                    c = 'b'
                if (b == 2):
                    c = 'c'
                if (b == 3):
                    c = 'd'
                if (b == 4):
                    c = 'e'
                if (b == 5):
                    c = 'f'
                if (b == 6):
                    c = 'g'
                if (b == 7):
                    c = 'h'
                if (b == 8):
                    c = 'i'
                if (b == 9):
                    c = 'j'
                if (b == 10):
                    c = 'k'
                if (b == 11):
                    c = 'l'
                if (b == 12):
                    c = 'm'
                if (b == 13):
                    c = 'n'
                if (b == 14):
                    c = 'o'
                if (b == 15):
                    c = 'p'
                if (b == 16):
                    c = 'q'
                if (b == 17):
                    c = 'r'
                if (b == 18):
                    c = 's'
                if (b == 19):
                    c = 't'
                if (b == 20):
                    c = 'u'
                if (b == 21):
                    c = 'v'
                if (b == 22):
                    c = 'w'
                if (b == 23):
                    c = 'x'
                if (b == 24):
                    c = 'y'
                if (b == 25):
                    c = 'z'
                li.insert(tk.END, c)
            if (text[i] == 'i' or text[i] == 'I'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                if (b == 1):
                    c = 'b'
                if (b == 2):
                    c = 'c'
                if (b == 3):
                    c = 'd'
                if (b == 4):
                    c = 'e'
                if (b == 5):
                    c = 'f'
                if (b == 6):
                    c = 'g'
                if (b == 7):
                    c = 'h'
                if (b == 8):
                    c = 'i'
                if (b == 9):
                    c = 'j'
                if (b == 10):
                    c = 'k'
                if (b == 11):
                    c = 'l'
                if (b == 12):
                    c = 'm'
                if (b == 13):
                    c = 'n'
                if (b == 14):
                    c = 'o'
                if (b == 15):
                    c = 'p'
                if (b == 16):
                    c = 'q'
                if (b == 17):
                    c = 'r'
                if (b == 18):
                    c = 's'
                if (b == 19):
                    c = 't'
                if (b == 20):
                    c = 'u'
                if (b == 21):
                    c = 'v'
                if (b == 22):
                    c = 'w'
                if (b == 23):
                    c = 'x'
                if (b == 24):
                    c = 'y'
                if (b == 25):
                    c = 'z'
                li.insert(tk.END, c)
            if (text[i] == 'j' or text[i] == 'J'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                if (b == 1):
                    c = 'b'
                if (b == 2):
                    c = 'c'
                if (b == 3):
                    c = 'd'
                if (b == 4):
                    c = 'e'
                if (b == 5):
                    c = 'f'
                if (b == 6):
                    c = 'g'
                if (b == 7):
                    c = 'h'
                if (b == 8):
                    c = 'i'
                if (b == 9):
                    c = 'j'
                if (b == 10):
                    c = 'k'
                if (b == 11):
                    c = 'l'
                if (b == 12):
                    c = 'm'
                if (b == 13):
                    c = 'n'
                if (b == 14):
                    c = 'o'
                if (b == 15):
                    c = 'p'
                if (b == 16):
                    c = 'q'
                if (b == 17):
                    c = 'r'
                if (b == 18):
                    c = 's'
                if (b == 19):
                    c = 't'
                if (b == 20):
                    c = 'u'
                if (b == 21):
                    c = 'v'
                if (b == 22):
                    c = 'w'
                if (b == 23):
                    c = 'x'
                if (b == 24):
                    c = 'y'
                if (b == 25):
                    c = 'z'
                li.insert(tk.END, c)
            if (text[i] == 'k' or text[i] == 'K'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                if (b == 1):
                    c = 'b'
                if (b == 2):
                    c = 'c'
                if (b == 3):
                    c = 'd'
                if (b == 4):
                    c = 'e'
                if (b == 5):
                    c = 'f'
                if (b == 6):
                    c = 'g'
                if (b == 7):
                    c = 'h'
                if (b == 8):
                    c = 'i'
                if (b == 9):
                    c = 'j'
                if (b == 10):
                    c = 'k'
                if (b == 11):
                    c = 'l'
                if (b == 12):
                    c = 'm'
                if (b == 13):
                    c = 'n'
                if (b == 14):
                    c = 'o'
                if (b == 15):
                    c = 'p'
                if (b == 16):
                    c = 'q'
                if (b == 17):
                    c = 'r'
                if (b == 18):
                    c = 's'
                if (b == 19):
                    c = 't'
                if (b == 20):
                    c = 'u'
                if (b == 21):
                    c = 'v'
                if (b == 22):
                    c = 'w'
                if (b == 23):
                    c = 'x'
                if (b == 24):
                    c = 'y'
                if (b == 25):
                    c = 'z'
                li.insert(tk.END, c)
            if (text[i] == 'l' or text[i] == 'L'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                if (b == 1):
                    c = 'b'
                if (b == 2):
                    c = 'c'
                if (b == 3):
                    c = 'd'
                if (b == 4):
                    c = 'e'
                if (b == 5):
                    c = 'f'
                if (b == 6):
                    c = 'g'
                if (b == 7):
                    c = 'h'
                if (b == 8):
                    c = 'i'
                if (b == 9):
                    c = 'j'
                if (b == 10):
                    c = 'k'
                if (b == 11):
                    c = 'l'
                if (b == 12):
                    c = 'm'
                if (b == 13):
                    c = 'n'
                if (b == 14):
                    c = 'o'
                if (b == 15):
                    c = 'p'
                if (b == 16):
                    c = 'q'
                if (b == 17):
                    c = 'r'
                if (b == 18):
                    c = 's'
                if (b == 19):
                    c = 't'
                if (b == 20):
                    c = 'u'
                if (b == 21):
                    c = 'v'
                if (b == 22):
                    c = 'w'
                if (b == 23):
                    c = 'x'
                if (b == 24):
                    c = 'y'
                if (b == 25):
                    c = 'z'
                li.insert(tk.END, c)
            if (text[i] == 'm' or text[i] == 'M'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                if (b == 1):
                    c = 'b'
                if (b == 2):
                    c = 'c'
                if (b == 3):
                    c = 'd'
                if (b == 4):
                    c = 'e'
                if (b == 5):
                    c = 'f'
                if (b == 6):
                    c = 'g'
                if (b == 7):
                    c = 'h'
                if (b == 8):
                    c = 'i'
                if (b == 9):
                    c = 'j'
                if (b == 10):
                    c = 'k'
                if (b == 11):
                    c = 'l'
                if (b == 12):
                    c = 'm'
                if (b == 13):
                    c = 'n'
                if (b == 14):
                    c = 'o'
                if (b == 15):
                    c = 'p'
                if (b == 16):
                    c = 'q'
                if (b == 17):
                    c = 'r'
                if (b == 18):
                    c = 's'
                if (b == 19):
                    c = 't'
                if (b == 20):
                    c = 'u'
                if (b == 21):
                    c = 'v'
                if (b == 22):
                    c = 'w'
                if (b == 23):
                    c = 'x'
                if (b == 24):
                    c = 'y'
                if (b == 25):
                    c = 'z'
                li.insert(tk.END, c)
            if (text[i] == 'n' or text[i] == 'N'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                if (b == 1):
                    c = 'b'
                if (b == 2):
                    c = 'c'
                if (b == 3):
                    c = 'd'
                if (b == 4):
                    c = 'e'
                if (b == 5):
                    c = 'f'
                if (b == 6):
                    c = 'g'
                if (b == 7):
                    c = 'h'
                if (b == 8):
                    c = 'i'
                if (b == 9):
                    c = 'j'
                if (b == 10):
                    c = 'k'
                if (b == 11):
                    c = 'l'
                if (b == 12):
                    c = 'm'
                if (b == 13):
                    c = 'n'
                if (b == 14):
                    c = 'o'
                if (b == 15):
                    c = 'p'
                if (b == 16):
                    c = 'q'
                if (b == 17):
                    c = 'r'
                if (b == 18):
                    c = 's'
                if (b == 19):
                    c = 't'
                if (b == 20):
                    c = 'u'
                if (b == 21):
                    c = 'v'
                if (b == 22):
                    c = 'w'
                if (b == 23):
                    c = 'x'
                if (b == 24):
                    c = 'y'
                if (b == 25):
                    c = 'z'
                li.insert(tk.END, c)
            if (text[i] == 'o' or text[i] == 'O'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                if (b == 1):
                    c = 'b'
                if (b == 2):
                    c = 'c'
                if (b == 3):
                    c = 'd'
                if (b == 4):
                    c = 'e'
                if (b == 5):
                    c = 'f'
                if (b == 6):
                    c = 'g'
                if (b == 7):
                    c = 'h'
                if (b == 8):
                    c = 'i'
                if (b == 9):
                    c = 'j'
                if (b == 10):
                    c = 'k'
                if (b == 11):
                    c = 'l'
                if (b == 12):
                    c = 'm'
                if (b == 13):
                    c = 'n'
                if (b == 14):
                    c = 'o'
                if (b == 15):
                    c = 'p'
                if (b == 16):
                    c = 'q'
                if (b == 17):
                    c = 'r'
                if (b == 18):
                    c = 's'
                if (b == 19):
                    c = 't'
                if (b == 20):
                    c = 'u'
                if (b == 21):
                    c = 'v'
                if (b == 22):
                    c = 'w'
                if (b == 23):
                    c = 'x'
                if (b == 24):
                    c = 'y'
                if (b == 25):
                    c = 'z'
                li.insert(tk.END, c)
            if (text[i] == 'p' or text[i] == 'P'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                if (b == 1):
                    c = 'b'
                if (b == 2):
                    c = 'c'
                if (b == 3):
                    c = 'd'
                if (b == 4):
                    c = 'e'
                if (b == 5):
                    c = 'f'
                if (b == 6):
                    c = 'g'
                if (b == 7):
                    c = 'h'
                if (b == 8):
                    c = 'i'
                if (b == 9):
                    c = 'j'
                if (b == 10):
                    c = 'k'
                if (b == 11):
                    c = 'l'
                if (b == 12):
                    c = 'm'
                if (b == 13):
                    c = 'n'
                if (b == 14):
                    c = 'o'
                if (b == 15):
                    c = 'p'
                if (b == 16):
                    c = 'q'
                if (b == 17):
                    c = 'r'
                if (b == 18):
                    c = 's'
                if (b == 19):
                    c = 't'
                if (b == 20):
                    c = 'u'
                if (b == 21):
                    c = 'v'
                if (b == 22):
                    c = 'w'
                if (b == 23):
                    c = 'x'
                if (b == 24):
                    c = 'y'
                if (b == 25):
                    c = 'z'
                li.insert(tk.END, c)
            if (text[i] == 'q' or text[i] == 'Q'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                if (b == 1):
                    c = 'b'
                if (b == 2):
                    c = 'c'
                if (b == 3):
                    c = 'd'
                if (b == 4):
                    c = 'e'
                if (b == 5):
                    c = 'f'
                if (b == 6):
                    c = 'g'
                if (b == 7):
                    c = 'h'
                if (b == 8):
                    c = 'i'
                if (b == 9):
                    c = 'j'
                if (b == 10):
                    c = 'k'
                if (b == 11):
                    c = 'l'
                if (b == 12):
                    c = 'm'
                if (b == 13):
                    c = 'n'
                if (b == 14):
                    c = 'o'
                if (b == 15):
                    c = 'p'
                if (b == 16):
                    c = 'q'
                if (b == 17):
                    c = 'r'
                if (b == 18):
                    c = 's'
                if (b == 19):
                    c = 't'
                if (b == 20):
                    c = 'u'
                if (b == 21):
                    c = 'v'
                if (b == 22):
                    c = 'w'
                if (b == 23):
                    c = 'x'
                if (b == 24):
                    c = 'y'
                if (b == 25):
                    c = 'z'
                li.insert(tk.END, c)
            if (text[i] == 'r' or text[i] == 'R'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                if (b == 1):
                    c = 'b'
                if (b == 2):
                    c = 'c'
                if (b == 3):
                    c = 'd'
                if (b == 4):
                    c = 'e'
                if (b == 5):
                    c = 'f'
                if (b == 6):
                    c = 'g'
                if (b == 7):
                    c = 'h'
                if (b == 8):
                    c = 'i'
                if (b == 9):
                    c = 'j'
                if (b == 10):
                    c = 'k'
                if (b == 11):
                    c = 'l'
                if (b == 12):
                    c = 'm'
                if (b == 13):
                    c = 'n'
                if (b == 14):
                    c = 'o'
                if (b == 15):
                    c = 'p'
                if (b == 16):
                    c = 'q'
                if (b == 17):
                    c = 'r'
                if (b == 18):
                    c = 's'
                if (b == 19):
                    c = 't'
                if (b == 20):
                    c = 'u'
                if (b == 21):
                    c = 'v'
                if (b == 22):
                    c = 'w'
                if (b == 23):
                    c = 'x'
                if (b == 24):
                    c = 'y'
                if (b == 25):
                    c = 'z'
                li.insert(tk.END, c)
            if (text[i] == 's' or text[i] == 'S'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                if (b == 1):
                    c = 'b'
                if (b == 2):
                    c = 'c'
                if (b == 3):
                    c = 'd'
                if (b == 4):
                    c = 'e'
                if (b == 5):
                    c = 'f'
                if (b == 6):
                    c = 'g'
                if (b == 7):
                    c = 'h'
                if (b == 8):
                    c = 'i'
                if (b == 9):
                    c = 'j'
                if (b == 10):
                    c = 'k'
                if (b == 11):
                    c = 'l'
                if (b == 12):
                    c = 'm'
                if (b == 13):
                    c = 'n'
                if (b == 14):
                    c = 'o'
                if (b == 15):
                    c = 'p'
                if (b == 16):
                    c = 'q'
                if (b == 17):
                    c = 'r'
                if (b == 18):
                    c = 's'
                if (b == 19):
                    c = 't'
                if (b == 20):
                    c = 'u'
                if (b == 21):
                    c = 'v'
                if (b == 22):
                    c = 'w'
                if (b == 23):
                    c = 'x'
                if (b == 24):
                    c = 'y'
                if (b == 25):
                    c = 'z'
                li.insert(tk.END, c)
            if (text[i] == 't' or text[i] == 'T'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                if (b == 1):
                    c = 'b'
                if (b == 2):
                    c = 'c'
                if (b == 3):
                    c = 'd'
                if (b == 4):
                    c = 'e'
                if (b == 5):
                    c = 'f'
                if (b == 6):
                    c = 'g'
                if (b == 7):
                    c = 'h'
                if (b == 8):
                    c = 'i'
                if (b == 9):
                    c = 'j'
                if (b == 10):
                    c = 'k'
                if (b == 11):
                    c = 'l'
                if (b == 12):
                    c = 'm'
                if (b == 13):
                    c = 'n'
                if (b == 14):
                    c = 'o'
                if (b == 15):
                    c = 'p'
                if (b == 16):
                    c = 'q'
                if (b == 17):
                    c = 'r'
                if (b == 18):
                    c = 's'
                if (b == 19):
                    c = 't'
                if (b == 20):
                    c = 'u'
                if (b == 21):
                    c = 'v'
                if (b == 22):
                    c = 'w'
                if (b == 23):
                    c = 'x'
                if (b == 24):
                    c = 'y'
                if (b == 25):
                    c = 'z'
                li.insert(tk.END, c)
            if (text[i] == 'u' or text[i] == 'U'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                if (b == 1):
                    c = 'b'
                if (b == 2):
                    c = 'c'
                if (b == 3):
                    c = 'd'
                if (b == 4):
                    c = 'e'
                if (b == 5):
                    c = 'f'
                if (b == 6):
                    c = 'g'
                if (b == 7):
                    c = 'h'
                if (b == 8):
                    c = 'i'
                if (b == 9):
                    c = 'j'
                if (b == 10):
                    c = 'k'
                if (b == 11):
                    c = 'l'
                if (b == 12):
                    c = 'm'
                if (b == 13):
                    c = 'n'
                if (b == 14):
                    c = 'o'
                if (b == 15):
                    c = 'p'
                if (b == 16):
                    c = 'q'
                if (b == 17):
                    c = 'r'
                if (b == 18):
                    c = 's'
                if (b == 19):
                    c = 't'
                if (b == 20):
                    c = 'u'
                if (b == 21):
                    c = 'v'
                if (b == 22):
                    c = 'w'
                if (b == 23):
                    c = 'x'
                if (b == 24):
                    c = 'y'
                if (b == 25):
                    c = 'z'
                li.insert(tk.END, c)
            if (text[i] == 'v' or text[i] == 'V'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                if (b == 1):
                    c = 'b'
                if (b == 2):
                    c = 'c'
                if (b == 3):
                    c = 'd'
                if (b == 4):
                    c = 'e'
                if (b == 5):
                    c = 'f'
                if (b == 6):
                    c = 'g'
                if (b == 7):
                    c = 'h'
                if (b == 8):
                    c = 'i'
                if (b == 9):
                    c = 'j'
                if (b == 10):
                    c = 'k'
                if (b == 11):
                    c = 'l'
                if (b == 12):
                    c = 'm'
                if (b == 13):
                    c = 'n'
                if (b == 14):
                    c = 'o'
                if (b == 15):
                    c = 'p'
                if (b == 16):
                    c = 'q'
                if (b == 17):
                    c = 'r'
                if (b == 18):
                    c = 's'
                if (b == 19):
                    c = 't'
                if (b == 20):
                    c = 'u'
                if (b == 21):
                    c = 'v'
                if (b == 22):
                    c = 'w'
                if (b == 23):
                    c = 'x'
                if (b == 24):
                    c = 'y'
                if (b == 25):
                    c = 'z'
                li.insert(tk.END, c)
            if (text[i] == 'w' or text[i] == 'W'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                    li.insert(tk.END, c)
                if (b == 1):
                    c = 'b'
                    li.insert(tk.END, c)
                if (b == 2):
                    c = 'c'
                    li.insert(tk.END, c)
                if (b == 3):
                    c = 'd'
                    li.insert(tk.END, c)
                if (b == 4):
                    c = 'e'
                    li.insert(tk.END, c)
                if (b == 5):
                    c = 'f'
                    li.insert(tk.END, c)
                if (b == 6):
                    c = 'g'
                    li.insert(tk.END, c)
                if (b == 7):
                    c = 'h'
                    li.insert(tk.END, c)
                if (b == 8):
                    c = 'i'
                    li.insert(tk.END, c)
                if (b == 9):
                    c = 'j'
                    li.insert(tk.END, c)
                if (b == 10):
                    c = 'k'
                    li.insert(tk.END, c)
                if (b == 11):
                    c = 'l'
                    li.insert(tk.END, c)
                if (b == 12):
                    c = 'm'
                    li.insert(tk.END, c)
                if (b == 13):
                    c = 'n'
                    li.insert(tk.END, c)
                if (b == 14):
                    c = 'o'
                    li.insert(tk.END, c)
                if (b == 15):
                    c = 'p'
                    li.insert(tk.END, c)
                if (b == 16):
                    c = 'q'
                    li.insert(tk.END, c)
                if (b == 17):
                    c = 'r'
                    li.insert(tk.END, c)
                if (b == 18):
                    c = 's'
                    li.insert(tk.END, c)
                if (b == 19):
                    c = 't'
                    li.insert(tk.END, c)
                if (b == 20):
                    c = 'u'
                    li.insert(tk.END, c)
                if (b == 21):
                    c = 'v'
                    li.insert(tk.END, c)
                if (b == 22):
                    c = 'w'
                    li.insert(tk.END, c)
                if (b == 23):
                    c = 'x'
                    li.insert(tk.END, c)
                if (b == 24):
                    c = 'y'
                    li.insert(tk.END, c)
                if (b == 25):
                    c = 'z'
                    li.insert(tk.END, c)
                li.insert(tk.END, c)
            if (text[i] == 'x' or text[i] == 'X'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                if (b == 1):
                    c = 'b'
                if (b == 2):
                    c = 'c'
                if (b == 3):
                    c = 'd'
                if (b == 4):
                    c = 'e'
                if (b == 5):
                    c = 'f'
                if (b == 6):
                    c = 'g'
                if (b == 7):
                    c = 'h'
                if (b == 8):
                    c = 'i'
                if (b == 9):
                    c = 'j'
                if (b == 10):
                    c = 'k'
                if (b == 11):
                    c = 'l'
                if (b == 12):
                    c = 'm'
                if (b == 13):
                    c = 'n'
                if (b == 14):
                    c = 'o'
                if (b == 15):
                    c = 'p'
                if (b == 16):
                    c = 'q'
                if (b == 17):
                    c = 'r'
                if (b == 18):
                    c = 's'
                if (b == 19):
                    c = 't'
                if (b == 20):
                    c = 'u'
                if (b == 21):
                    c = 'v'
                if (b == 22):
                    c = 'w'
                if (b == 23):
                    c = 'x'
                if (b == 24):
                    c = 'y'
                if (b == 25):
                    c = 'z'
                li.insert(tk.END, c)
            if (text[i] == 'y' or text[i] == 'Y'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                if (b == 1):
                    c = 'b'
                if (b == 2):
                    c = 'c'
                if (b == 3):
                    c = 'd'
                if (b == 4):
                    c = 'e'
                if (b == 5):
                    c = 'f'
                if (b == 6):
                    c = 'g'
                if (b == 7):
                    c = 'h'
                if (b == 8):
                    c = 'i'
                if (b == 9):
                    c = 'j'
                if (b == 10):
                    c = 'k'
                if (b == 11):
                    c = 'l'
                if (b == 12):
                    c = 'm'
                if (b == 13):
                    c = 'n'
                if (b == 14):
                    c = 'o'
                if (b == 15):
                    c = 'p'
                if (b == 16):
                    c = 'q'
                if (b == 17):
                    c = 'r'
                if (b == 18):
                    c = 's'
                if (b == 19):
                    c = 't'
                if (b == 20):
                    c = 'u'
                if (b == 21):
                    c = 'v'
                if (b == 22):
                    c = 'w'
                if (b == 23):
                    c = 'x'
                if (b == 24):
                    c = 'y'
                if (b == 25):
                    c = 'z'
                li.insert(tk.END, c)
            if (text[i] == 'z' or text[i] == 'Z'):
                a = 0
                b = (a + 13) % 26
                if (b == 0):
                    c = 'a'
                if (b == 1):
                    c = 'b'
                if (b == 2):
                    c = 'c'
                if (b == 3):
                    c = 'd'
                if (b == 4):
                    c = 'e'
                if (b == 5):
                    c = 'f'
                if (b == 6):
                    c = 'g'
                if (b == 7):
                    c = 'h'
                if (b == 8):
                    c = 'i'
                if (b == 9):
                    c = 'j'
                if (b == 10):
                    c = 'k'
                if (b == 11):
                    c = 'l'
                if (b == 12):
                    c = 'm'
                if (b == 13):
                    c = 'n'
                if (b == 14):
                    c = 'o'
                if (b == 15):
                    c = 'p'
                if (b == 16):
                    c = 'q'
                if (b == 17):
                    c = 'r'
                if (b == 18):
                    c = 's'
                if (b == 19):
                    c = 't'
                if (b == 20):
                    c = 'u'
                if (b == 21):
                    c = 'v'
                if (b == 22):
                    c = 'w'
                if (b == 23):
                    c = 'x'
                if (b == 24):
                    c = 'y'
                if (b == 25):
                    c = 'z'
                li.insert(tk.END, c)

            i=i+1

def decrypt():
    pass

#style
s='arial 19 bold'


#canva
c=Canvas(bg='#E7E5E5').place(x=0,y=0,width=500,height=600)
c1=Canvas(bg='black').place(x=500,y=0,width=500,height=600)

#StringVar
tx=StringVar()
tx1=StringVar()

#Entry
E1=Entry(fen,font=s,bg='black',fg='white',textvariable=tx).place(x=50,y=50 ,width=400,height=60)
E2=Entry(fen,font=s,bg='white',fg='black',textvariable=tx1).place(x=550,y=50 ,width=400,height=60)

#listbox
li=Listbox(fen,font=s,bg='black',fg='white').place(x=50,y=250 ,width=400,height=300)
lis=Listbox(fen,font=s,bg='white',fg='black').place(x=550,y=250 ,width=400,height=300)

#button
b1=Button(fen,command=encrypt,fg='orange',bg='#9C9C9C',text="Encryption",font=s).place(x=150,y=150 ,width=200,height=50)
b2=Button(fen,command=decrypt,fg='orange',bg='#9C9C9C',text="Decryption",font=s).place(x=650,y=150 ,width=200,height=50)











fen.mainloop()
