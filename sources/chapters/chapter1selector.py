import tkinter as tk
from ttkbootstrap.scrolled import ScrolledFrame
from chapters.chapter1 import unit1 
from chapters.chapter1 import unit2 
from chapters.chapter1 import unit3



files={'unit1':unit1,'unit2':unit2,'unit3':unit3}


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
        self.canvas.create_image(0, 0, image=self.background, anchor="nw")
        n1Img = self.canvas.create_image(981, 536, image=self.n1, anchor="nw")
        n2Img = self.canvas.create_image(390, 974, image=self.n2, anchor="nw")
        n3Img = self.canvas.create_image(778, 1475, image=self.n3, anchor="nw")
        self.canvas.tag_bind(n1Img, "<Button-1>", self.loadSummary('unit1'))
        self.canvas.tag_bind(n2Img, "<Button-1>", self.loadSummary('unit2'))
        self.canvas.tag_bind(n3Img, "<Button-1>", self.loadSummary('unit3'))
        self.canvas.pack()

    def loadAssets(self):
        self.background=tk.PhotoImage(file='sources/assets/ChapterSelectionBackgrounds/Introduction.png')
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
        
        self.canvas.create_image()