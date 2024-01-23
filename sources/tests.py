from tkinter import *
from tkinter import font
import ttkbootstrap as tb
class Chapter(tb.Frame):
    def _init_(self,parent):
        super.__init__(parent)
        tb.Label(self,text='red').pack()
        self.place(x=0,y=0)

root = Tk()
root.title('Font Families')


root.mainloop()