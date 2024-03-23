from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledFrame

root=tb.Window(themename='solar')
root.title('Dashboard')
root.geometry('1280x720')
root.resizable(False,False)
mainFrame=ScrolledFrame(root)
mainFrame.autohide_scrollbar()
mainFrame.pack(expand=True, fill='both')


f1=PhotoImage(file='sources/assets/Fonds+serpents/Serpent_3_niveaux/Frame1.png')
f2=PhotoImage(file='sources/assets/Fonds+serpents/Serpent_3_niveaux/Frame2.png')
f3=PhotoImage(file='sources/assets/Fonds+serpents/Serpent_3_niveaux/Frame3.png')
f1L = tb.Label(mainFrame,image=f1)
f1L.pack()
f2L = tb.Label(mainFrame,image=f2)
f2L.pack()
f3L = tb.Label(mainFrame,image=f3)
f3L.pack()

root.mainloop()
