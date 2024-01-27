from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledFrame
root=tb.Window(themename='solar')
root.title('Dashboard')
root.geometry('1280x720')
root.resizable(False,False)



root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainFrame=tb.Frame(root)
mainFrame.grid(column=0, row=0, sticky=("nsew"))

# Assets
menuIcon=PhotoImage(file='sources/icons/menu-burger.png').subsample(12, 12)
rocketIcon=PhotoImage(file='sources/icons/rocket-lunch.png').subsample(11, 11)

font=('Yu Gothic Ui Light', 12)
titleFont=('Yu Gothic Ui Bold', 24)
titleFont2=('Yu Gothic Ui Bold', 12)

#backgroundColor=mainFrame['background']


# Creating grid
mainFrame.columnconfigure(0,weight=1)
mainFrame.columnconfigure(1,weight=5)
mainFrame.rowconfigure(0,weight=1)
mainFrame.rowconfigure(1,weight=15)

# SIDE MENU

# All side menu components
menuFrame=tb.Frame(mainFrame,bootstyle='info')
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

def change_page(pageName):
      frame = __import__(pageName, globals(), locals(), 0).mainFrame
      frame.grid(row=1,column=0,columnspan=2,sticky='nsew')
      contentFrame.grid_forget()
      










# NAVBAR

navbar=tb.Frame(mainFrame)
navbar.grid(row=0, column=0,columnspan=2,sticky='nsew')

navbar.columnconfigure(0,weight=1) #unecessary
navbar.rowconfigure(0,weight=1) #unecessary

open_menu_button = tb.Button(mainFrame, image=menuIcon, command=open_side_menu, bootstyle='info',takefocus=False,text='Commencer')
open_menu_button.place(x=15,y=15)

title=tb.Label(navbar,text='Dashboard',font=titleFont)
title.grid(row=0, column=0,sticky='ns')

days = tb.Label(mainFrame,text='0',font=titleFont)
days.place(x=1170,y=15)

rocket = tb.Label(mainFrame, image=rocketIcon, style='info.TLabel')
rocketstyle = tb.Style()
rocketstyle.configure('info.TLabel',foreground='#3F98D7')
rocket.place(x=1200,y=15)


# CONTENT
s = tb.Style()
s.configure('My.TFrame')

contentFrame=tb.Frame(mainFrame,style='My.TFrame')
contentFrame.grid(row=1,column=0,columnspan=2,sticky='nsew')

contentFrame.columnconfigure(0,weight=2) 
contentFrame.columnconfigure(1,weight=1) 
contentFrame.columnconfigure(2,weight=2) 
contentFrame.columnconfigure(3,weight=1) 
contentFrame.columnconfigure(4,weight=2) 
contentFrame.columnconfigure(5,weight=1) 
contentFrame.columnconfigure(6,weight=2) 

contentFrame.rowconfigure(0,weight=1)
contentFrame.rowconfigure(1,weight=2)
contentFrame.rowconfigure(2,weight=4)



# CHAPITRE
class Chapter(tb.Frame):
	def __init__(self, parent,rowNum,columnNum,title,progressNum,chapterName):
		super().__init__(master = parent)
		tb.Label(self,text=title,font=titleFont2).pack(fill=Y)         
		tb.Meter(self,amountused=progressNum,amounttotal=100,subtext="Progres",meterthickness=20).pack(pady=5)       
		tb.Button(self,command=lambda: change_page(chapterName), bootstyle='info',takefocus=False).pack(pady=5)    
		self.grid(row=rowNum,column=columnNum,sticky='nsew')

Chapter(contentFrame,1,1,'Variables et affectations',20,'chap1')
Chapter(contentFrame,1,3,'Variables et affectations',90,'chap2')
Chapter(contentFrame,1,5,'Variables et affectations',50,'chap3')



root.mainloop()