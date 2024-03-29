import tkinter as tk
from chapters import chapter1selector,chapter2selector,chapter3selector#,chapter4selector,chapter5selector,chapter6selector,chapter7selector

root = tk.Tk()
root.title('Dashboard')
root.geometry('1280x720')
root.resizable(False,False)

mainFrame = tk.Frame(root)
mainFrame.configure(bg='#002b36')
mainFrame.pack(expand=True, fill='both')



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


i = 0
chapitres=['Introduction\n','Variables \net affectations','Arithmetique \net comparaisons','Conditions\n','Boucles\n','Fonctions\n','Listes et Dictionnaires']
chapitresFiles=['chapter1','chapter2','chapter3','chapter4','chapter5','chapter6','chapter7']
chapitresFilesTransform={'chapter1':chapter1selector,'chapter2':chapter2selector,'chapter3':chapter3selector,
						 #'chapter4':chapter4selector,'chapter5':chapter5selector,'chapter6':chapter6selector,'chapter7':chapter7selector
                         }
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
	mainFrame.pack_forget()
	chapter=chapitresFilesTransform[pageName]
	chapter.ChapterFrame(root)


# CONTENT

dashboard = tk.Canvas(mainFrame, width=dashboardImg.width(), height=dashboardImg.height(),highlightthickness=0)
dashboard.create_image(0, 0, anchor=tk.NW, image=dashboardImg)
dashboard.configure(bg="#002b36")
dashboard.grid(row=0,column=0,columnspan=7,sticky='ns',pady=(50,0))  

# LOGIQUE FLECHE 

def move(n):
	global i
	i+=n
	if i<=len(chapitres)-3 and i>=0:
		Chapter(mainFrame,1,1,chapitres[i],progressions[i],chapitresFiles[i])
		Chapter(mainFrame,3,1,chapitres[i+1],progressions[i+1],chapitresFiles[i+1])
		Chapter(mainFrame,5,1,chapitres[i+2],progressions[i+2],chapitresFiles[i+2])
	else:
		i-=n

# FLECHE GAUCHE
fleche_g=tk.Button(mainFrame, relief='flat', activebackground='#002b36', background='#002b36', image=fleche_gImg,command=lambda:move(-1))
fleche_g.configure(bg="#002b36")
fleche_g.grid(row=1,column=0) 

# FLECHE DROITE

fleche_d=tk.Button(mainFrame, relief='flat', activebackground='#002b36', background='#002b36', image=fleche_dImg,command=lambda:move(1))
fleche_d.configure(bg= "#002b36")
fleche_d.grid(row=1,column=6) 

# CHAPITRE
class Chapter(tk.Frame):
	def __init__(self, parent,columnNum,rowNum,chapName,prog,fileName):
		super().__init__(master = parent)
		rectangle_chapitre = tk.Canvas(mainFrame, width=rectangle_chapitreImg.width(), height=rectangle_chapitreImg.height(),highlightthickness=0)
		rectangle_chapitre.configure(bg="#002b36")
		rectangle_chapitre.create_image(0, 0, anchor=tk.NW, image=rectangle_chapitreImg)
		rectangle_chapitre.grid(row=rowNum,column=columnNum) 
		
		chapitreFrame=tk.Frame(mainFrame, width=rectangle_chapitreImg.width(), height=rectangle_chapitreImg.height(),highlightthickness=0)
		chapitreFrame.configure(bg="white")
		chapitreFrame.grid(row=rowNum,column=columnNum)
		
		tk.Label(chapitreFrame,text=chapName,font=h3Font,background ='white',foreground='#002b36',justify="center",highlightthickness=0).pack(pady = (0, 30))
		
		pourcentage = tk.Canvas(chapitreFrame, width=pourcentageImg.width(), height=pourcentageImg.height(),highlightthickness=0)
		pourcentage.configure(bg= "white")
		pourcentage.create_image(0, 0, anchor=tk.NW, image=pourcentageImg)
		pourcentage.create_image(0, 220-(prog*2.2), anchor=tk.NW, image=pourcentage_reverseImg)
		pourcentage.pack(fill='y')
	


		tk.Label(chapitreFrame,text=str(prog)+'%',font=h3Font,background ='white',foreground='#002b36',justify="center").pack()
		
		chapitreButton=tk.Button(chapitreFrame)
		if prog==0: 
			chapitreButton.configure(bg= "white",bd=0,image=commencerImg,command=lambda:change_page(fileName))
		else:
			chapitreButton.configure(bg= "white",image=continuerImg,command=lambda:change_page(fileName))
		chapitreButton.pack(pady = (30, 0))	
			
Chapter(mainFrame,1,1,chapitres[0],progressions[0],chapitresFiles[0])
Chapter(mainFrame,3,1,chapitres[1],progressions[1],chapitresFiles[1])
Chapter(mainFrame,5,1,chapitres[2],progressions[2],chapitresFiles[2])


root.mainloop()
