from markdown import setTextWidget
import tkinter as tk
import chapters.chapter2.megaquiz as nextFrame
App = tk.Tk()
App.title('Dashboard')
App.geometry('1280x720')
App.resizable(False,False)
h1Font = ('Inter', 50, "bold")
h3Font = ('Inter', 20, "bold")
h1Font = ('Inter', 54, "bold")
h2Font = ('Inter', 20, "bold")

unit_title = 'Quiz 2'
class Content(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__()

        # initialize mainframe
        self.App = master
        self.mainFrame = tk.Frame(master=self.App)
        self.mainFrame.pack(expand=True, fill='both')
        self.mainFrame.configure(background='#D9D9D9')

        self.unit_content='''
        nom = 'Gabriel'
        age = '16'
        classe = '1ere'
        print(nom)

        Qu'affiche ce programme? 
        '''

        self.title=tk.Label(self.mainFrame, text='QUIZ',font=h1Font)
        self.title.configure(bg='#D9D9D9')
        self.title.pack(pady=10)
        self.widget = tk.Text(self.mainFrame,height='20')
        setTextWidget(self.widget, self.unit_content, 'c')
        self.widget.pack()
        self.entry1 = tk.Entry(self.mainFrame)
        self.widget.window_create(7.33, window=self.entry1)
        self.valider=tk.PhotoImage(file='sources/assets/ElementDivers/valider.png').subsample(2,2)
        self.continuer=tk.PhotoImage(file='sources/assets/ElementDivers/continuer.png')
        self.bottomFrame=tk.Frame(self.mainFrame)
        self.bottomFrame.configure(bg="#D9D9D9")
        self.bottomFrame.pack(pady=15)
        self.completionStatus = tk.StringVar(self.bottomFrame)
        self.message=tk.Label(self.bottomFrame,textvariable=self.completionStatus,font=h3Font)
        self.message.configure(bg="#D9D9D9")
        self.message.pack(side=tk.LEFT)
        self.validerButton=tk.Button(self.bottomFrame,image=self.valider,command=self.check,bd=0)
        self.validerButton.configure(bg="#D9D9D9")
        self.validerButton.pack(side=tk.LEFT,padx=15)
        self.prochainButton=tk.Button(self.bottomFrame,image=self.continuer,bd=0)
        self.prochainButton.configure(bg="#D9D9D9")
        
    def check(self):
        if "Gabriel" in self.entry1.get():
            self.completionStatus.set("Correct!")
            self.message.configure(fg='#00FF00')
            self.prochainButton.pack(padx=15)
        else:
            self.completionStatus.set("Faux")
            self.message.configure(fg='#FF0000')
    def nextPage(self):
        nextFrame.Content(self.mainFrame)

a = Content(App)
App.mainloop()