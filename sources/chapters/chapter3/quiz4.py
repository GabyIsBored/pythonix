
    
h1Font = ('Inter', 54, "bold")
h2Font = ('Inter', 20, "bold")
from markdown import setTextWidget
import tkinter as tk
import chapters.chapter3.megaquiz as nextFrame
import chapters.chapter3selector as previousFrame
unit_title = 'Quiz 4'

class Content(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__()

        # initialize mainframe
        self.root = master
        self.mainFrame = tk.Frame(master=self.root)
        self.mainFrame.configure(bg='#D9D9D9')
        self.mainFrame.pack(expand=True, fill='both')

        self.unit_content='''**Trouvez si le joueur1 a plus de points que le joueur 2, et si ce total est egal au maximum**

max=2000
joueur1=2500
joueur2=joueur1 * 2/3
print(joueur1  joueur2)
print( ==  + )'''

        self.title=tk.Label(self.mainFrame, text='QUIZ',font=h1Font)
        self.title.configure(bg='#D9D9D9')
        self.title.pack(pady=10)
        self.widget = tk.Text(self.mainFrame,height='20')
        setTextWidget(self.widget, self.unit_content, 'c')
        self.widget.pack()
        self.widget.window_create(6.14, window=self.entry1)
        self.entry1 = tk.Entry(master)
        self.widget.window_create(7.8, window=self.entry1)
        self.entry1 = tk.Entry(master)
        self.widget.window_create(6.12, window=self.entry1)

        self.valider=tk.PhotoImage(file='sources/assets/ElementDivers/valider.png').subsample(2,2)
        self.continuer=tk.PhotoImage(file='sources/assets/ElementDivers/continuer.png')
        self.retour=tk.PhotoImage(file='sources/assets/ElementDivers/retour.png')
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
        self.retourButton=tk.Button(self.bottomFrame,image=self.retour,command=self.back)
        self.retourButton.configure(bg="#D9D9D9")

    def check(self):
            if "15" in self.entry1.get():
                self.completionStatus.set("Correct!")
                self.message.configure(fg='#00FF00')
                self.retourButton.pack(padx=15)
                self.prochainButton.pack(padx=15)
                
            else:
                self.completionStatus.set("Faux")
                self.message.configure(fg='#ff0000')
    def nextPage(self):
            self.mainFrame.pack_forget()
            nextFrame.Content(self.root)
    def back(self):
        previousFrame.ChapterFrame(self.root)
        self.mainFrame.pack_forget()
        

