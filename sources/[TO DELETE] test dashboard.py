import tkinter as tk
from chapters import chapter2

root=tk.Tk()
root.title('el1')
root.geometry('1280x720')
root.resizable(False,False)

root.withdraw()
new_window = tk.Toplevel()
chapter2.SubchapterSelection_2(new_window) 

root.mainloop()
