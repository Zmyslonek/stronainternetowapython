from tkinter import *
from tkinter import ttk
import time
import random

window = Tk()

ilikepython = IntVar()

global password
global likepythonl

password = "🤔"

notebook = ttk.Notebook(window)

registertab = Frame(notebook)
sourcetab = Frame(notebook)
settings = Frame(notebook)

bgcolor = "green"

notebook.add(registertab,text="Rejestracja")
notebook.pack(expand=True,fill="both")

def submit(event):
    password = entry.get()
    notebook.add(sourcetab,text="Strona")
    labeltest.config(text="⌨Twoje hasło: " + password)
    notebook.add(settings,text="Ustawienia")

entry = Entry(registertab)
entry.config(relief=RAISED,bd=10,show="*")
entry.bind("<Return>",submit)

def ilikepythondef():
    if (ilikepython.get()==1):
        likepythonl.config(text="(:")
    else:
        likepythonl.config(text="):")

def bgcolorchange(event):
    bgcolor = colorentry.get()
    sourcetab.config(bg=bgcolor)
     

labelwp = Label(registertab,text="🎰Utwórz hasło:")

ypt = "Twoje hasło to:" + password
entry.pack()

labeltest = Label(sourcetab)
labeltest.place(x=1000,y=650)
labelwp.pack(side="top")

logopng = PhotoImage(file='C:\\Users\\Nikodem\\Desktop\\PythonGames\\logo.png')

checkbox = Checkbutton(sourcetab,
                       text="Lubie pythona!",
                       relief=RAISED,
                       bd=2,bg="gray",
                       activeforeground="green",
                       variable=ilikepython,onvalue=1,offvalue=0,command=ilikepythondef)
sourcetab.config(background=bgcolor)
checkbox.place(x=5,y=5)
logolabel = Label(sourcetab,image=logopng,compound="bottom",text="zmyślonkowo.pl")
logolabel.pack(side="top")
likepythonl = Label(sourcetab,relief=RAISED,bd=5,font=('Arial',30),bg="gray")
likepythonl.place(x=25,y=50)
label2 = Label(settings,text="Kolor tła np. yellow, '#HEX' itd.")
label2.config(relief=RAISED,bd=10)
label2.pack(side="left")
colorentry = Entry(settings)
colorentry.bind("<Return>",bgcolorchange)
colorentry.config(relief=RAISED,bd=10,fg="green",bg="yellow")
colorentry.pack(side="left")
window.mainloop()