
from markdown import setTextWidget
import tkinter as tk
import chapters.chapter3.unit2 as nextFrame
h1Font = ('Inter', 54, "bold")
h2Font = ('Inter', 20, "bold")

unit_title = 'Quiz 3'
class Content(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__()

        # initialize mainframe
        self.root = master
        self.mainFrame = tk.Frame(master=self.root)
        self.mainFrame.configure(bg='#D9D9D9')
        self.mainFrame.pack(expand=True, fill='both')

        self.unit_content='''**Affichez 'Succes!' si la chaine de characteres 'message' contient le mot 'validee' et le **
**booleen 'pret' est egal a True, sinon affichez 'Echec'**

if 'validee'  message  pret   True:
    print("L'eleve a une moyenne inferieure a la moyenne")
:
    print("Echec")


'''
        self.title=tk.Label(self.mainFrame, text='QUIZ',font=h1Font)
        self.title.configure(bg='#D9D9D9')
        self.title.pack(pady=10)
        self.widget = tk.Text(self.mainFrame,height='20')
        setTextWidget(self.widget, self.unit_content, 'c')
        self.widget.pack()

        self.entry1 = tk.Entry(self.mainFrame)
        self.widget.window_create(4.13, window=self.entry1)
        self.entry2 = tk.Entry(self.mainFrame)
        self.widget.window_create(4.23, window=self.entry2)
        self.entry3 = tk.Entry(self.mainFrame)
        self.widget.window_create(4.31, window=self.entry3)
        self.entry4 = tk.Entry(self.mainFrame)
        self.widget.window_create(6.0, window=self.entry4)

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
        if "in" in self.entry1.get() and "and" in self.entry2.get() and "==" in self.entry3.get() and 'else' in self.entry4.get() :
            self.completionStatus.set("Correct!")
            self.message.configure(fg='#00FF00')
            self.prochainButton.pack(padx=15)
        else:
            self.completionStatus.set("Faux")
            self.message.configure(fg='#FF0000')
    def nextPage(self):
        self.mainFrame.pack_forget()
        nextFrame.Content(self.root)
        

