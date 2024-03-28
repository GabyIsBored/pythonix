import tkinter as tk
from chapters.chapter2 import SubchapterSelection_2

root=tk.Tk()
root.title('el1')
root.geometry('1280x720')
root.resizable(False,False)

myFrame = SubchapterSelection_2(root)

root.mainloop()
