from markdown import setTextWidget
from tkinter import *
import ttkbootstrap as tb
root=tb.Window()
root.title('Dashboard')
root.geometry('1280x720')
root.resizable(False,False)
mainFrame=Frame(root)
mainFrame.pack(expand=True, fill='both',padx=10,pady=10)
h1Font = ('Inter', 54, "bold")
h2Font = ('Inter', 20, "bold")
mainFrame.configure(bg='#D9D9D9')
def nextPage():
    print('y')


unit_content='''**Trouvez si le joueur1 a plus de points que le joueur 2, et si ce total est egal au maximum**
**par 7:**

max=2000
joueur1=2500
joueur2=joueur1 * 2/3
print(joueur1  joueur2)
print( ==  + )
'''

title=Label(mainFrame, text='QUIZ',font=h1Font)
title.configure(bg='#D9D9D9')
title.pack(pady=10)
widget = Text(mainFrame,height='20')
setTextWidget(widget, unit_content, 'c')
widget.pack()

entry1 = Entry(mainFrame)
widget.window_create(7.14, window=entry1)
entry2 = Entry(mainFrame)
widget.window_create(8.6, window=entry2)
entry3 = Entry(mainFrame)
widget.window_create(8.11, window=entry3)
entry4 = Entry(mainFrame)
widget.window_create(8.15, window=entry4)



def check():
    if ">" in entry1.get() and "max" in entry2.get() and "joueur1" or 'joueur2' in entry3.get() and "joueur1" or 'joueur2' in entry3.get() :
        completionStatus.set("Correct!")
        message.configure(fg='#00FF00')
        prochainButton.pack(padx=15)
    else:
        completionStatus.set("Faux")
        message.configure(fg='#ff0000')
valider=PhotoImage(file='sources/assets/ElementDivers/valider.png').subsample(2,2)
continuer=PhotoImage(file='sources/assets/ElementDivers/continuer.png')
bottomFrame=Frame(mainFrame)
bottomFrame.configure(bg="#D9D9D9")
bottomFrame.pack(pady=15)
completionStatus = StringVar(bottomFrame)
message=Label(bottomFrame,textvariable=completionStatus,font=h2Font)
message.configure(bg="#D9D9D9")
message.pack(side=LEFT)
validerButton=Button(bottomFrame,image=valider,command=check)
validerButton.configure(bg="#D9D9D9")
validerButton.pack(side=LEFT,padx=15)
prochainButton=Button(bottomFrame,image=continuer,command=nextPage)
prochainButton.configure(bg="#D9D9D9")

root.mainloop()