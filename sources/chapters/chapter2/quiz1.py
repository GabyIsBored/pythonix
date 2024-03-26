from markdown import setTextWidget
from tkinter import *
import ttkbootstrap as tb
root=tb.Window()
root.title('Dashboard')
root.geometry('1280x720')
root.resizable(False,False)
mainFrame=Frame(root)
mainFrame.pack(expand=True, fill='both',padx=10,pady=10)
h1Font = ('Inter', 34, "bold")
mainFrame.configure(bg='#D9D9D9')



unit_content='''
'''

title=Label(mainFrame, text='QUIZ',font=h1Font)
title.configure(bg='#D9D9D9')
title.pack()
widget = Text(mainFrame,height='20')
setTextWidget(widget, unit_content, 'c')
widget.pack()

entry1 = Entry(mainFrame, text="Click me!")
widget.window_create(1.0, window=entry1)
def check():
    if "hi" in entry1.get():
        print('validated')
    else:
        print('not validated')
valider=PhotoImage(file='sources/assets/ElementDivers/Valider.png').subsample(2,2)
Button(mainFrame,image=valider,command=check,background='#D9D9D9').pack()


root.mainloop()