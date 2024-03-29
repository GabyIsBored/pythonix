
from markdown import setTextWidget
import tkinter as tk
import chapters.chapter3.unit2 as nextFrame
h1Font = ('Inter', 54, "bold")
h2Font = ('Inter', 20, "bold")

unit_title = 'Quiz 2'
class Content(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__()

        # initialize mainframe
        self.root = master
        self.mainFrame = tk.Frame(master=self.root)
        self.mainFrame.configure(bg='#D9D9D9')
        self.mainFrame.pack(expand=True, fill='both')

        self.unit_content='''**Creez une fonction lambda qui prend en parametre 'nombre' et retourne ca valeur**

resultat = lambda:
'''
        self.title=tk.Label(self.mainFrame, text='QUIZ',font=h1Font)
        self.title.configure(bg='#D9D9D9')
        self.title.pack(pady=10)
        self.widget = tk.Text(self.mainFrame,height='20')
        setTextWidget(self.widget, self.unit_content, 'c')
        self.widget.pack()

        self.entry1 = tk.Entry(self.mainFrame)
        self.widget.window_create(3.17, window=self.entry1)
        self.entry2 = tk.Entry(self.mainFrame)
        self.widget.window_create(3.18, window=self.entry2)

        
        self.valider=tk.PhotoImage(file='sources/assets/ElementDivers/valider.png').subsample(2,2)
        self.continuer=tk.PhotoImage(file='sources/assets/ElementDivers/continuer.png')
        self.bottomFrame=tk.Frame(self.mainFrame)
        self.bottomFrame.configure(bg="#D9D9D9")
        self.bottomFrame.pack(pady=15)
        self.completionStatus = tk.StringVar(self.bottomFrame)
        self.message=tk.Label(self.bottomFrame,textvariable=self.completionStatus,font=h2Font)
        self.message.configure(bg="#D9D9D9")
        self.message.pack(side=tk.LEFT)
        self.validerButton=tk.Button(self.bottomFrame,image=self.valider,command=self.check,bd=0)
        self.validerButton.configure(bg="#D9D9D9")
        self.validerButton.pack(side=tk.LEFT,padx=15)
        self.prochainButton=tk.Button(self.bottomFrame,image=self.continuer,command=self.nextPage,bd=0)
        self.prochainButton.configure(bg="#D9D9D9")
        
    def check(self):
        if "nombre" in self.entry1.get() and "nombre)" in self.entry2.get() :
            self.completionStatus.set("Correct!")
            self.message.configure(fg='#00FF00')
            self.prochainButton.pack(padx=15)
        else:
            self.completionStatus.set("Faux")
            self.message.configure(fg='#FF0000')
    def nextPage(self):
        self.mainFrame.pack_forget()
        nextFrame.Content(self.root)
        

