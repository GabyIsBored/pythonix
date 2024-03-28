from markdown import setTextWidget
from tkinter import tk
import ttkbootstrap as tb
root=tb.Window()
root.title('Dashboard')
root.geometry('1280x720')
root.resizable(False,False)
mainFrame=tk.Frame(root)
mainFrame.pack(expand=True, fill='both',padx=10,pady=10)
h1Font = ('Inter', 54, "bold")
h2Font = ('Inter', 20, "bold")
mainFrame.configure(bg='#D9D9D9')
def nextPage():
    print('y')


unit_content='''**Afficher le nombre de bus necessaires pour transporter tout les joueurs sachant qu'il y a **
**deux fois plus de joueurs de rugby que de basket:**

placesDeBus = 24
joueursDeBasket = 75
print(( +  2) // + 1)
'''

title=Label(mainFrame, text='QUIZ',font=h1Font)
title.configure(bg='#D9D9D9')
title.pack(pady=10)
widget = Text(mainFrame,height='20')
setTextWidget(widget, unit_content, 'c')
widget.pack()

entry1 = Entry(mainFrame)
widget.window_create(6.7, window=entry1)
entry2 = Entry(mainFrame)
widget.window_create(6.11, window=entry2)
entry3 = Entry(mainFrame)
widget.window_create(6.15, window=entry3)


def check():
    if "joueursDeBasket" in entry1.get() and "joueursDeBasket" in entry2.get() and "placesDeBus" in entry3.get() :
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
message.pack(side=tk.LEFT)
validerButton=Button(bottomFrame,image=valider,command=check)
validerButton.configure(bg="#D9D9D9")
validerButton.pack(side=tk.LEFT,padx=15)
prochainButton=Button(bottomFrame,image=continuer,command=nextPage)
prochainButton.configure(bg="#D9D9D9")

root.mainloop()