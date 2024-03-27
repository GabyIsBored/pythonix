from markdown import setTextWidget
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


unit_content='''nom = 'Gabriel'
age = '16'
classe = '1ere'
print(nom)

Qu'affiche ce programme? 
'''

title=tk.Label(mainFrame, text='QUIZ',font=h1Font)
title.configure(bg='#D9D9D9')
<<<<<<< HEAD
title.pack()
widget = tk.Text(mainFrame,height='20')
setTextWidget(widget, unit_content, 'c')
widget.pack()

entry1 = tk.Entry(mainFrame, text="Click me!")
widget.window_create(1.0, window=entry1)
=======
title.pack(pady=10)
widget = Text(mainFrame,height='20')
setTextWidget(widget, unit_content, 'c')
widget.pack()

entry1 = Entry(mainFrame)
widget.window_create(6.33, window=entry1)
>>>>>>> ec2f90ef428dd5923958522ca4eba6d63bd17f26
def check():
    if "Gabriel" in entry1.get():
        completionStatus.set("Correct!")
        message.configure(fg='#00FF00')
        prochainButton.pack(padx=15)
    else:
<<<<<<< HEAD
        print('not validated')
valider=tk.PhotoImage(file='sources/assets/ElementDivers/Valider.png').subsample(2,2)
tk.Button(mainFrame,image=valider,command=check,background='#D9D9D9').pack()

=======
        completionStatus.set("Faux")
        message.configure(fg='#ff0000')
valider=PhotoImage(file='sources/assets/ElementDivers/Valider.png').subsample(2,2)
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
prochainButton=Button(bottomFrame,image=valider,command=nextPage)
>>>>>>> ec2f90ef428dd5923958522ca4eba6d63bd17f26

root.mainloop()