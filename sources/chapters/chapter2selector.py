import tkinter as tk
from ttkbootstrap.scrolled import ScrolledFrame
from chapters.chapter2 import unit1 
from chapters.chapter2 import quiz1 
from chapters.chapter2 import unit2 
from chapters.chapter2 import quiz2 
'''from chapter2 import unit3 
from chapter2 import quiz3 
from chapter2 import unit4 
from chapter2 import quiz4 
from chapter2 import unit5 
from chapter2 import quiz5 '''
from chapters.chapter2 import megaquiz


files={'unit1':unit1,'quiz1':quiz1,'unit2':unit2,'quiz2':quiz2,'megaquiz':megaquiz}


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
        self.canvas.tag_bind(n1Img, "<Button-1>", self.loadSummary('unit1'))
        self.canvas.tag_bind(q1Img, "<Button-1>", self.loadSummary('quiz1'))
        self.canvas.tag_bind(n2Img, "<Button-1>", self.loadSummary('unit2'))
        self.canvas.tag_bind(q2Img, "<Button-1>", self.loadSummary('unit2'))
        self.canvas.tag_bind(mImg, "<Button-1>", self.loadSummary('megaquiz'))
        self.canvas.pack()

    def loadAssets(self):
        self.background=tk.PhotoImage(file='sources/assets/ChapterSelectionBackgrounds/Variables et Affectations.png')
        self.n1=tk.PhotoImage(file='sources/assets/ChapterSelectionIcons/Niveau1.png')
        self.n2=tk.PhotoImage(file='sources/assets/ChapterSelectionIcons/Niveau2.png')
        self.n3=tk.PhotoImage(file='sources/assets/ChapterSelectionIcons/Niveau3.png')
        self.n4=tk.PhotoImage(file='sources/assets/ChapterSelectionIcons/Niveau4.png')
        self.n5=tk.PhotoImage(file='sources/assets/ChapterSelectionIcons/Niveau5.png')
        self.quiz=tk.PhotoImage(file='sources/assets/ChapterSelectionIcons/quiz.png')
        self.megaQuiz=tk.PhotoImage(file='sources/assets/ChapterSelectionIcons/Mega quiz.png')

    def loadUnit(self, unitName):
        unitName.Content(self.root)
    
    def loadSummary(self, unitName):
        unitFile=files[unitName]
        summaryFrame = tk.Frame(self.canvas, width=300, height=75)
        summaryFrame.place(x=733, y=378)
        importedUnit_title = unitFile.unit_title
        tk.Label(summaryFrame,text=importedUnit_title).pack()
        tk.Button(summaryFrame,text='Demarrer',command=lambda: self.loadUnit(unitFile)).pack()