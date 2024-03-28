
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
        n1Img = self.canvas.create_image(374, 227, image=self.n1, anchor="nw")
        q1Img = self.canvas.create_image(242, 536, image=self.quiz, anchor="nw")
        n2Img = self.canvas.create_image(428, 908, image=self.n2, anchor="nw")
        q2Img = self.canvas.create_image(186, 1186, image=self.quiz, anchor="nw")

        n3Img = self.canvas.create_image(423, 1503, image=self.n3, anchor="nw")
        q3Img = self.canvas.create_image(69, 1793, image=self.quiz, anchor="nw")
        n4Img = self.canvas.create_image(209, 2169, image=self.n4, anchor="nw")
        q4Img = self.canvas.create_image(487, 2064, image=self.quiz, anchor="nw")
        mImg = self.canvas.create_image(640, 1715, image=self.megaQuiz, anchor="nw")

        # add bindings
        self.canvas.tag_bind(n1Img, "<Button-1>", self.loadSummary('unit1'))
        self.canvas.tag_bind(q1Img, "<Button-1>", self.loadSummary('quiz1'))
        self.canvas.tag_bind(n2Img, "<Button-1>", self.loadSummary('unit2'))
        self.canvas.tag_bind(q2Img, "<Button-1>", self.loadSummary('quiz2'))
        self.canvas.tag_bind(n3Img, "<Button-1>", self.loadSummary('unit3'))
        self.canvas.tag_bind(q3Img, "<Button-1>", self.loadSummary('quiz3'))
        self.canvas.tag_bind(n4Img, "<Button-1>", self.loadSummary('unit4'))
        self.canvas.tag_bind(q4Img, "<Button-1>", self.loadSummary('quiz4'))
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
        self.mainFrame.pack_forget()
        unitName.Content(self.root)
    
    def loadSummary(self, unitName):
        self.unitFile=files[unitName]
        self.importedUnit_title = self.unitFile.unit_title


#https://stackoverflow.com/questions/23876447/tkinter-overlay-foreground-image-on-top-of-a-background-image-with-transparency