from markdown import setTextWidget
from tkinter import *
import ttkbootstrap as tb
root=tb.Window()
root.title('Dashboard')
root.geometry('1280x720')
root.resizable(False,False)
mainFrame=Frame(root)
mainFrame.pack(expand=True, fill='both',padx=10,pady=10)
h1Font = ('Inter', 54, "bold")
h2Font = ('Inter', 20, "bold")
mainFrame.configure(bg='#D9D9D9')
def nextPage():
    print('y')


unit_content='''**Reparez ce programme permettant de definir le type d'un triangle selon les valeurs de ses cotes**

if a + b > c and a + c > b   b + c > a:
     a == b == c:
        print("Le triangle est équilatéral.")
     a == b   a == c   b == c:
        print("Le triangle est isocèle.")
    else:
        print("Le triangle est quelconque.")
:
    print("Ces longueurs ne peuvent pas former un triangle.")


'''

title=Label(mainFrame, text='QUIZ',font=h1Font)
title.configure(bg='#D9D9D9')
title.pack(pady=10)
widget = Text(mainFrame,height='20')
setTextWidget(widget, unit_content, 'c')
widget.pack()

entry1 = Entry(mainFrame)
widget.window_create(3.28, window=entry1)
entry2 = Entry(mainFrame)
widget.window_create(4.4, window=entry2)
entry3 = Entry(mainFrame)
widget.window_create(6.4, window=entry3)
entry4 = Entry(mainFrame)
widget.window_create(6.13, window=entry4)
entry5 = Entry(mainFrame)
widget.window_create(6.24, window=entry5)
entry6 = Entry(mainFrame)
widget.window_create(10.0, window=entry6)



def check():
    if "and" in entry1.get() and "if" in entry2.get() and "elif" in entry3.get() and "or" in entry4.get() and "or" in entry5.get() and "else" in entry6.get():
        completionStatus.set("Correct!")
        message.configure(fg='#00FF00')
        prochainButton.pack(padx=15)
    else:
        completionStatus.set("Faux")
        message.configure(fg='#ff0000')
valider=PhotoImage(file='sources/assets/ElementDivers/valider.png').subsample(2,2)
continuer=PhotoImage(file='sources/assets/ElementDivers/continuer.png')
bottomFrame=Frame(mainFrame)
bottomFrame.configure(bg="#D9D9D9")
bottomFrame.pack(pady=15)
completionStatus = StringVar(bottomFrame)
message=Label(bottomFrame,textvariable=completionStatus,font=h2Font)
message.configure(bg="#D9D9D9")
message.pack(side=LEFT)
validerButton=Button(bottomFrame,image=valider,command=check)
validerButton.configure(bg="#D9D9D9")
validerButton.pack(side=LEFT,padx=15)
prochainButton=Button(bottomFrame,image=continuer,command=nextPage)
prochainButton.configure(bg="#D9D9D9")

root.mainloop()