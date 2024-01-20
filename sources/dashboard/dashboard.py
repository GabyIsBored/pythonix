from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledFrame

root=tb.Window(themename='solar')
root.title('Dashboard')
root.geometry('1280x720')
root.resizable(False,False)

# Assets
menuIcon=PhotoImage(file='sources/icons/menu-burger.png').subsample(12, 12)
rocketIcon=PhotoImage(file='sources/icons/rocket-lunch.png').subsample(11, 11)

font=('Yu Gothic Ui Light', 12)
titleFont=('Yu Gothic Ui Bold', 24)
backgroundColor=root['background']


# Creating grid
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=5)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=15)

# SIDE MENU

# All side menu components
menuFrame=tb.Frame(root,bootstyle='info')
menucounter=0

chapitresLabel=tb.Label(menuFrame,text='Chapitres',font=font,bootstyle='inverse info')
chapitresLabel.place(relx=0.5, rely=0.15, anchor="c")

languesLabel=tb.Label(menuFrame,text='Langues',font=font,bootstyle='inverse info')
languesLabel.place(relx=0.5, rely=0.25, anchor="c")

jeanClaudeLabel=tb.Label(menuFrame,text='Jean Claude',font=font,bootstyle='inverse info')
jeanClaudeLabel.place(relx=0.5, rely=0.35, anchor="c")

#Open and close menu
def open_side_menu(): 
    global menucounter
    if menucounter%2==0:
        menuFrame.grid(row=0, column=0,rowspan=2,sticky='nsew')

        navbar.grid_forget()
        navbar.grid(row=0, column=1,sticky='nsew')
        contentFrame.grid_forget()
        contentFrame.grid(row=1, column=1,sticky='nsew')
    else:
        menuFrame.grid_forget()
        navbar.grid(row=0, column=0,columnspan=2,sticky='nsew')
        contentFrame.grid(row=1, column=0,columnspan=2,sticky='nsew')
    menucounter+=1
        
# NAVBAR

navbar=tb.Frame(root)
navbar.grid(row=0, column=0,columnspan=2,sticky='nsew')

navbar.columnconfigure(0,weight=1)
navbar.rowconfigure(0,weight=1)

open_menu_button = tb.Button(root, image=menuIcon, command=open_side_menu, bootstyle='info',takefocus=False)
open_menu_button.place(x=15,y=15)

title=tb.Label(navbar,text='Dashboard',font=titleFont)
title.grid(row=0, column=0,sticky='ns')

days = tb.Label(root,text='0',font=titleFont)
days.place(x=1170,y=15)

rocket = tb.Label(root, image=rocketIcon, style='info.TLabel')
rocketstyle = tb.Style()
rocketstyle.configure('info.TLabel',foreground='#3F98D7')
rocket.place(x=1200,y=15)


# CONTENT

contentFrame=ScrolledFrame(root,autohide=False)
contentFrame.grid(row=1,column=0,columnspan=2,sticky='nsew')


for i in range(21):
    tb.Label(contentFrame,text='filler').pack(pady=10)



root.mainloop()