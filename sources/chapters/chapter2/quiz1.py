#from markdown import setTextWidget
import tkinter as tk
root=tk.Tk()
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


unit_content='''nombreEleves = 15
participants = nombreEleves
nombreEleves = 16
nombreEleves = participants
print(nombreEleves)

Qu'affiche ce programme? 
'''

title=tk.Label(mainFrame, text='QUIZ',font=h1Font)
title.configure(bg='#D9D9D9')
title.pack(pady=10)
widget = tk.Text(mainFrame,height='20')
#setTextWidget(widget, unit_content, 'c')
widget.pack()

entry1 = tk.Entry(mainFrame)
widget.window_create(6.33, window=entry1)
def check():
    if "15" in entry1.get():
        completionStatus.set("Correct!")
        message.configure(fg='#00FF00')
        prochainButton.pack(padx=15)
    else:
        completionStatus.set("Faux")
        message.configure(fg='#ff0000')
valider=tk.PhotoImage(file='sources/assets/ElementDivers/Valider.png').subsample(2,2)
tk.Button(mainFrame,image=valider,command=check,background='#D9D9D9').pack()

        
valider=tk.PhotoImage(file='sources/assets/ElementDivers/valider.png').subsample(2,2)
continuer=tk.PhotoImage(file='sources/assets/ElementDivers/continuer.png').subsample(2,2)
bottomFrame=tk.Frame(mainFrame)
bottomFrame.configure(bg="#D9D9D9")
bottomFrame.pack(pady=15)
completionStatus = tk.StringVar(bottomFrame)
message=tk.Label(bottomFrame,textvariable=completionStatus,font=h2Font)
message.configure(bg="#D9D9D9")
message.pack(side=tk.LEFT)
validerButton=tk.Button(bottomFrame,image=valider,command=check)
validerButton.configure(bg="#D9D9D9")
validerButton.pack(side=tk.LEFT,padx=15)

prochainButton=tk.Button(bottomFrame,image=continuer,command=nextPage)
prochainButton.configure(bg="#D9D9D9")



root.mainloop()