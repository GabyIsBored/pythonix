import tkinter as tk
from ttkbootstrap.scrolled import ScrolledFrame

# from chapter2.unit1 import unit1_contentD
import chapter2.unit1 as unit1
class SubchapterSelection_2(tk.Frame):
    """Before making a new instance of this class, make sure to unpack previous frame"""
    def __init__(self, master: tk.Tk):
        super().__init__()
        
        # main frame initialization
        self.root2 = master
        self.mainFrame = ScrolledFrame(master=master)
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
        self.canvas.tag_bind(n1Img, "<Button-1>", lambda event: print('BUTTON CLICKED'))
        self.canvas.tag_bind(q1Img, "<Button-1>", lambda event: print('BUTTON CLICKED'))
        self.canvas.tag_bind(n2Img, "<Button-1>", lambda event: print('BUTTON CLICKED'))
        self.canvas.tag_bind(q2Img, "<Button-1>", lambda event: print('BUTTON CLICKED'))
        self.canvas.tag_bind(mImg, "<Button-1>", lambda event: print('BUTTON CLICKED'))
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
        
#https://stackoverflow.com/questions/23876447/tkinter-overlay-foreground-image-on-top-of-a-background-image-with-transparency'''
#https://stackoverflow.com/questions/62929953/how-to-import-the-another-tkinter-python-class-code-to-open-the-new-tkinter-wind