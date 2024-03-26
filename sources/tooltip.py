from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledFrame
root=tb.Window(themename='solar')
root.title('Test')
root.geometry('1280x720')
root.resizable(False,False)
pFont = ('Inter', 9, "bold")

class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#002b36", relief=SOLID, borderwidth=1,
                      font=pFont)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()
def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


label = Label(root, text = 'print')
label.pack()
CreateToolTip(label, text = 'Hello World\n'
                 'This is how tip looks like.'
                 'Best part is, it\'s not a menu.\n'
                 'Purely tipbox.')
root.mainloop()
#https://stackoverflow.com/questions/3221956/how-do-i-display-tooltips-in-tkinter