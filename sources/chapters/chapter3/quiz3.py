h1Font = ('Inter', 54, "bold")
h2Font = ('Inter', 20, "bold")
from markdown import setTextWidget
import tkinter as tk
import chapters.chapter3.unit3 as nextFrame
class Content(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__()
        self.root = master

        self.unit_content='''**Construisez un algortihme permettant d'ajouter 500 a la valuer de depart puis la multiplier **
        **par 7:**

        depart=1200
        depart  500
        depart  7
        print(depart)
        '''

        self.title=tk.Label(master, text='QUIZ',font=h1Font)
        self.title.configure(bg='#D9D9D9')
        self.title.pack(pady=10)
        self.widget = tk.Text(master,height='20')
        setTextWidget(self.widget, self.unit_content, 'c')
        self.widget.pack()
        self.entry1 = tk.Entry(master)
        self.widget.window_create(6.33, window=self.entry1)
        valider=tk.PhotoImage(file='sources/assets/ElementDivers/valider.png').subsample(2,2)
        continuer=tk.PhotoImage(file='sources/assets/ElementDivers/continuer.png').subsample(2,2)
        self.bottomFrame=tk.Frame(master)
        self.bottomFrame.configure(bg="#D9D9D9")
        self.bottomFrame.pack(pady=15)
        self.completionStatus = tk.StringVar(self.bottomFrame)
        self.message=tk.Label(self.bottomFrame,textvariable=self.completionStatus,font=h2Font)
        self.message.configure(bg="#D9D9D9")
        self.message.pack(side=tk.LEFT)
        self.validerButton=tk.Button(self.bottomFrame,image=valider,command=check)
        self.validerButton.configure(bg="#D9D9D9")
        self.validerButton.pack(side=tk.LEFT,padx=15)
        self.prochainButton=tk.Button(self.bottomFrame,image=continuer,command=nextPage)
        self.prochainButton.configure(bg="#D9D9D9")

        def check():
            if "+=" in self.entry1.get() and "*=" in self.entry2.get() :
                self.completionStatus.set("Correct!")
                self.message.configure(fg='#00FF00')
                self.prochainButton.pack(padx=15)
            else:
                self.completionStatus.set("Faux")
                self.message.configure(fg='#ff0000')
        def nextPage():
            nextFrame.Content(master)
