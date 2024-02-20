from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledFrame
root=tb.Window(themename='solar')
root.title('Dashboard')
root.geometry('1280x720')
root.resizable(False,False)




mainFrame=tb.Frame(root)
mainFrame.pack(expand=True, fill='both')

# Assets
menuIcon=PhotoImage(file='sources/icons/menu-burger.png').subsample(12, 12)
rocketIcon=PhotoImage(file='sources/icons/rocket-lunch.png').subsample(11, 11)

commencerImg=PhotoImage(file='sources/assets/Dashboard/commencer.png')
continuerImg=PhotoImage(file='sources/assets/Dashboard/continuer.png')
dashboardImg=PhotoImage(file='sources/assets/Dashboard/dashboard.png')
fleche_dImg=PhotoImage(file='sources/assets/Dashboard/fleche_d.png')
fleche_gImg=PhotoImage(file='sources/assets/Dashboard/fleche_g.png')
fondImg=PhotoImage(file='sources/assets/Dashboard/fond.png')
pourcentageImg=PhotoImage(file='sources/assets/Dashboard/pourcentage.png')
rectangle_chapitreImg=PhotoImage(file='sources/assets/Dashboard/rectangle_chapitre.png')
serpent_haut_gImg=PhotoImage(file='sources/assets/Dashboard/serpent_haut_g.png')

font = ('Yu Gothic Ui Light', 12)
h1Font = ('Inter', 34, "bold")
h3Font = ('Inter', 20, "bold")
pFont = ('Inter', 9, "bold")

s = tb.Style()
s.configure('My.TFrame', background='white')

i=0
chapitres=['Introduction\n','Variables \net affectations','Arithmetique \net comparaisons','Conditions\n','Boucles\n',
		   'Boucles avancees\n','Fonctions\n','Tableaux\n','Dictionnaires \net Tuples','‘Import’ \net Modules']
progressions=[0,0,0,0,0,0,0,0,0,0]




# Creating grid
mainFrame.columnconfigure(0,weight=10)
mainFrame.columnconfigure(1,weight=23)
mainFrame.columnconfigure(2,weight=5)
mainFrame.columnconfigure(3,weight=23)
mainFrame.columnconfigure(4,weight=5)
mainFrame.columnconfigure(5,weight=23)
mainFrame.columnconfigure(6,weight=10)


mainFrame.rowconfigure(0,weight=23)
mainFrame.rowconfigure(1,weight=70)
mainFrame.rowconfigure(2,weight=7)
'''
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
'''
def change_page(pageName):
      frame = __import__(pageName, globals(), locals(), 0).mainFrame
      frame.grid(row=1,column=0,columnspan=2,sticky='nsew')
      mainFrame.grid_forget() 

# NAVBAR
'''
days = tb.Label(mainFrame,text='0',font=titleFont)
days.place(x=1170,y=15)

rocket = tb.Label(mainFrame, image=rocketIcon)
rocket.place(x=1200,y=15)'''


# CONTENT

dashboard = tb.Canvas(mainFrame, width=dashboardImg.width(), height=dashboardImg.height())
dashboard.create_image(0, 0, anchor=NW, image=dashboardImg)
dashboard.grid(row=0,column=0,columnspan=7,sticky='ns',pady=(50,0))  

# LOGIQUE FLECHE 

def move(n):
	global i
	i=i+n
	if i<=len(chapitres)-3 and i>=0:
		Chapter(mainFrame,1,1,chapitres[i],progressions[i])
		Chapter(mainFrame,3,1,chapitres[i+1],progressions[i+1])
		Chapter(mainFrame,5,1,chapitres[i+2],progressions[i+2])
	else:
		i=i-n

# FLECHE GAUCHE
fleche_g=Button(mainFrame,bg="#002b36",image=fleche_gImg,command=lambda:move(-1))
fleche_g.configure(bg= "#002b36")
fleche_g.grid(row=1,column=0) 

# FLECHE DROITE

fleche_d=Button(mainFrame,bg="#002b36",image=fleche_dImg,command=lambda:move(1))
fleche_d.configure(bg= "#002b36")
fleche_d.grid(row=1,column=6) 

# CHAPITRE
class Chapter(tb.Frame):
	def __init__(self, parent,columnNum,rowNum,chapName,prog):
		super().__init__(master = parent)
		rectangle_chapitre = tb.Canvas(mainFrame, width=rectangle_chapitreImg.width(), height=rectangle_chapitreImg.height())
		rectangle_chapitre.create_image(0, 0, anchor=NW, image=rectangle_chapitreImg)
		rectangle_chapitre.grid(row=rowNum,column=columnNum) 
		
		chapitreFrame=tb.Frame(mainFrame, width=rectangle_chapitreImg.width(), height=rectangle_chapitreImg.height(),style='My.TFrame')
		chapitreFrame.grid(row=rowNum,column=columnNum)
		
		tb.Label(chapitreFrame,text=chapName,font=h3Font,background ='white',foreground='#002b36',justify="center").pack(pady = (0, 30))
		
		pourcentage = tb.Canvas(chapitreFrame, width=pourcentageImg.width(), height=pourcentageImg.height())
		pourcentage.configure(bg= "white")
		pourcentage.create_image(0, 0, anchor=NW, image=pourcentageImg)
		pourcentage.pack(fill='y')
		
		tb.Label(chapitreFrame,text=str(prog)+'%',font=h3Font,background ='white',foreground='#002b36',justify="center").pack()
		
		chapitreButton=Button(chapitreFrame)
		if prog==0: 
			chapitreButton.configure(bg= "white",image=commencerImg)
		else:
			chapitreButton.configure(bg= "white",image=continuerImg)
		chapitreButton.pack(pady = (30, 0))	
			
Chapter(mainFrame,1,1,chapitres[0],progressions[0])
Chapter(mainFrame,3,1,chapitres[1],progressions[1])
Chapter(mainFrame,5,1,chapitres[2],progressions[2])


root.mainloop()
