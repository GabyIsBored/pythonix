from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledFrame

root=tb.Window(themename='solar')
root.title('Dashboard')
root.geometry('1280x720')
root.resizable(False,False)


# widgets
loadingBarFrame = tb.Frame(root)
wineImage = PhotoImage(master=loadingBarFrame, file="sources\\icons\\menu-burger.png").subsample(2, 2)
wineLabel = tb.Label(loadingBarFrame, image=wineImage)
wineLabel.pack()

# Create a transparent canvas on top of the label
canvas = Canvas(wineLabel, width=25, height=23)
# canvas.config(height=24)
canvas.pack()


loadingBarFrame.pack(expand=True, fill='both')

root.mainloop()