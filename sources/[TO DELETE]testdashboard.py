import tkinter as tkinter
from chapters import chapter2

root=tk.Tk()
root.title('el1')
root.geometry('1280x720')
root.resizable(False,False)

chapter2.SubchapterSelection_2(root)

root.mainloop()