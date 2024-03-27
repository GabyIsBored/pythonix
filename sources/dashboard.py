import tkinter as tk


App = tk.Tk()
App.title('Dashboard')
App.geometry('1280x720')
App.resizable(False,False)

mainFrame = tk.Frame(App, background='#002b36')
mainFrame.pack(expand=True, fill='both')

# Assets
menuIcon = tk.PhotoImage(file='sources/icons/menu-burger.png').subsample(12, 12)
rocketIcon = tk.PhotoImage(file='sources/icons/rocket-lunch.png').subsample(11, 11)

commencerImg = tk.PhotoImage(file='sources/assets/Dashboard/commencer.png')
continuerImg = tk.PhotoImage(file='sources/assets/Dashboard/continuer.png')
dashboardImg = tk.PhotoImage(file='sources/assets/Dashboard/dashboard.png')
fleche_dImg = tk.PhotoImage(file='sources/assets/Dashboard/fleche_d.png')
fleche_gImg = tk.PhotoImage(file='sources/assets/Dashboard/fleche_g.png')
fondImg = tk.PhotoImage(file='sources/assets/Dashboard/fond.png')
pourcentageImg= tk.PhotoImage(file='sources/assets/Dashboard/pourcentage.png')
pourcentage_reverseImg = tk.PhotoImage(file='sources/assets/Dashboard/pourcentage_reverse.png')
rectangle_chapitreImg = tk.PhotoImage(file='sources/assets/Dashboard/rectangle_chapitre.png')
serpent_haut_gImg = tk.PhotoImage(file='sources/assets/Dashboard/serpent_haut_g.png')

font = ('Yu Gothic Ui Light', 12)
h1Font = ('Inter', 34, "bold")
h3Font = ('Inter', 20, "bold")
pFont = ('Inter', 9, "bold")

# s = tb.Style()
# s.configure('My.TFrame', background='white')

i = 0
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


def change_page(pageName):
	global mainFrame
	for widget in mainFrame.winfo_children():
		widget.destroy()
	page_module = import_module(pageName)
	new_mainFrame = getattr(page_module, 'mainFrame', None)
	if new_mainFrame:
        # Update mainFrame
		mainFrame = new_mainFrame(App)
        # Re-pack the mainFrame with the new content
		mainFrame.pack()
# NAVBAR

days = tk.Label(mainFrame,text='0',font=h3Font)
days.place(x=1170,y=15)

rocket = tk.Label(mainFrame, image=rocketIcon)
rocket.place(x=1200,y=15)


# CONTENT

dashboard = tk.Canvas(mainFrame, width=dashboardImg.width(), height=dashboardImg.height())
dashboard.create_image(0, 0, anchor=tk.NW, image=dashboardImg)
dashboard.grid(row=0,column=0,columnspan=7,sticky='ns',pady=(50,0))  

# LOGIQUE FLECHE 

def move(n):
	global i
	i+=n
	if i<=len(chapitres)-3 and i>=0:
		Chapter(mainFrame,1,1,chapitres[i],progressions[i])
		Chapter(mainFrame,3,1,chapitres[i+1],progressions[i+1])
		Chapter(mainFrame,5,1,chapitres[i+2],progressions[i+2])
	else:
		i-=n

# FLECHE GAUCHE
fleche_g=tk.Button(mainFrame, relief='flat', activebackground='#002b36', background='#002b36', image=fleche_gImg,command=lambda:move(-1))
fleche_g.configure(bg= "#002b36")
fleche_g.grid(row=1,column=0) 

# FLECHE DROITE

fleche_d=tk.Button(mainFrame, relief='flat', activebackground='#002b36', background='#002b36', image=fleche_dImg,command=lambda:move(1))
fleche_d.configure(bg= "#002b36")
fleche_d.grid(row=1,column=6) 

# CHAPITRE
class Chapter(tk.Frame):
	def __init__(self, parent,columnNum,rowNum,chapName,prog):
		super().__init__(master = parent)
		rectangle_chapitre = tk.Canvas(mainFrame, width=rectangle_chapitreImg.width(), height=rectangle_chapitreImg.height())
		rectangle_chapitre.create_image(0, 0, anchor=tk.NW, image=rectangle_chapitreImg)
		rectangle_chapitre.grid(row=rowNum,column=columnNum) 
		
		chapitreFrame=tk.Frame(mainFrame, width=rectangle_chapitreImg.width(), height=rectangle_chapitreImg.height())
		chapitreFrame.grid(row=rowNum,column=columnNum)
		
		tk.Label(chapitreFrame,text=chapName,font=h3Font,background ='white',foreground='#002b36',justify="center").pack(pady = (0, 30))
		
		pourcentage = tk.Canvas(chapitreFrame, width=pourcentageImg.width(), height=pourcentageImg.height())
		pourcentage.configure(bg= "white")
		pourcentage.create_image(0, 0, anchor=tk.NW, image=pourcentageImg)
		pourcentage.create_image(0, 220-(prog*2.2), anchor=tk.NW, image=pourcentage_reverseImg)
		pourcentage.pack(fill='y')
	


		tk.Label(chapitreFrame,text=str(prog)+'%',font=h3Font,background ='white',foreground='#002b36',justify="center").pack()
		
		chapitreButton=tk.Button(chapitreFrame)
		if prog==0: 
			chapitreButton.configure(bg= "white",image=commencerImg,command=lambda:change_page('test'))
		else:
			chapitreButton.configure(bg= "white",image=continuerImg,command=lambda:change_page('test'))
		chapitreButton.pack(pady = (30, 0))	
			
Chapter(mainFrame,1,1,chapitres[0],progressions[0])
Chapter(mainFrame,3,1,chapitres[1],progressions[1])
Chapter(mainFrame,5,1,chapitres[2],progressions[2])


App.mainloop()
