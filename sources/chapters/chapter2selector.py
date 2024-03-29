

import tkinter as tk
from ttkbootstrap.scrolled import ScrolledFrame
from chapters.chapter2 import unit1 
from chapters.chapter2 import quiz1 
from chapters.chapter2 import unit2 
from chapters.chapter2 import quiz2
from chapters.chapter2 import megaquiz
files={'unit1':unit1,'quiz1':quiz1,'unit2':unit2,'quiz2':quiz2,'megaquiz':megaquiz}

font = ('Yu Gothic Ui Light', 12)
h1Font = ('Inter', 50, "bold")
h3Font = ('Inter', 20, "bold")
pFont = ('Inter', 9, "bold")

class ChapterFrame(tk.Frame):
    """Before making a new instance of this class, make sure to unpack previous frame"""
    def __init__(self, master: tk.Tk):
        super().__init__()
        
        # main frame initialization
        self.root = master
        self.mainFrame = ScrolledFrame(master=self.root)
        self.mainFrame.autohide_scrollbar()
        self.mainFrame.pack(expand=True, fill='both')

        # set images
        self.loadAssets()
        self.canvas = tk.Canvas(master=self.mainFrame, width=self.background.width(), height=self.background.height(), highlightthickness=0, bd=0)
        backgroundImg = self.canvas.create_image(0, 0, image=self.background, anchor="nw")
        
        n1Img = self.canvas.create_image(233, 378, image=self.n1, anchor="nw")
        q1Img = self.canvas.create_image(141, 720, image=self.quiz, anchor="nw")
        n2Img = self.canvas.create_image(415, 871, image=self.n2, anchor="nw")
        q2Img = self.canvas.create_image(497, 1099, image=self.quiz, anchor="nw")
        mImg = self.canvas.create_image(640, 1715, image=self.megaQuiz, anchor="nw")

        # add bindings
        self.canvas.tag_bind(n1Img, "<Button-1>", lambda event:self.loadSummary(event,'unit1'))
        self.canvas.tag_bind(q1Img, "<Button-1>", lambda event:self.loadSummary(event,'quiz1'))
        self.canvas.tag_bind(n2Img, "<Button-1>", lambda event:self.loadSummary(event,'unit2'))
        self.canvas.tag_bind(q2Img, "<Button-1>", lambda event:self.loadSummary(event,'unit2'))
        self.canvas.tag_bind(mImg, "<Button-1>", lambda event:self.loadSummary(event,'megaquiz'))
        self.canvas.pack()

    def loadSummary(self,event,unitName):
        self.coordonnees=[]
        if unitName=='unit1':
            self.coordonnees=[(840-70, 250+60),(810, 310+120),(650, 250)]
        elif unitName=='unit2':
            self.coordonnees=[(810-65, 974+60),(800, 1034+120),(630, 974)]
        elif unitName=='unit3':
            self.coordonnees=[(290-75, 1475+60),(300, 1525+120),(130, 1475)]
        
        self.unitFile=files[unitName]
        self.importedUnit_title = self.unitFile.unit_title
        titleText=self.canvas.create_text(self.coordonnees[0][0],self.coordonnees[0][1], text=self.importedUnit_title, anchor="nw",font=h1Font)
        commencerBtn=self.canvas.create_image(self.coordonnees[1][0],self.coordonnees[1][1], image=self.commencer, anchor="nw")
        self.canvas.create_image(self.coordonnees[2][0],self.coordonnees[2][1], image=self.fond, anchor="nw")
        self.canvas.tag_raise(titleText)
        self.canvas.tag_raise(commencerBtn)
        self.canvas.tag_bind(commencerBtn, "<Button-1>", lambda event: self.loadUnit(event, self.unitFile))

    def loadAssets(self):
        self.background=tk.PhotoImage(file='sources/assets/ChapterSelectionBackgrounds/Variables et affectations.png')
        self.n1=tk.PhotoImage(file='sources/assets/ChapterSelectionIcons/Niveau1.png')
        self.n2=tk.PhotoImage(file='sources/assets/ChapterSelectionIcons/Niveau2.png')
        self.n3=tk.PhotoImage(file='sources/assets/ChapterSelectionIcons/Niveau3.png')
        self.n4=tk.PhotoImage(file='sources/assets/ChapterSelectionIcons/Niveau4.png')
        self.n5=tk.PhotoImage(file='sources/assets/ChapterSelectionIcons/Niveau5.png')
        self.quiz=tk.PhotoImage(file='sources/assets/ChapterSelectionIcons/quiz.png')
        self.megaQuiz=tk.PhotoImage(file='sources/assets/ChapterSelectionIcons/Mega quiz.png')
        self.commencer=tk.PhotoImage(file='sources/assets/Dashboard/commencer.png')
        self.fond=tk.PhotoImage(file='sources/assets/Lecon_exemple/fond_exemple.png')

    def loadUnit(self,event, unitName):
        print('x')
        self.mainFrame.pack_forget()
        unitName.Content(self.root)