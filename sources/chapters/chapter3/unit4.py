from markdown import setTextWidget
from tkinter import *
import ttkbootstrap as tb
root=tb.Window()
root.title('Dashboard')
root.geometry('1280x720')
root.resizable(False,False)
mainFrame=Frame(root)
mainFrame.pack(expand=True, fill='both',padx=10,pady=10)
h1Font = ('Inter', 34, "bold")
mainFrame.configure(bg='#D9D9D9')

unit_content='''# Comparaisons

Python est capable d'effectuer toute une série de comparaisons entre le contenu de deux variables,

en renvoyant un **booleen** `True` ou `False` si la comparaisons est verifiee ou pas.

### Egalite et inegalites

Pour tester l’égalité de contenu entre deux valeurs, on utilise l’operateur `==` :

`>>> 2 == 3`  

`>>> False` 

`>>> 3 == 3`  

`>>> True`    

Pour tester l’inégalité de contenu entre deux valeurs, on utilise l’operateur `!=` :

`>>> 2 != 3`  

`>>> False` 

### **Infériorité et supériorité, stricts ou larges**

Pour savoir si un objet est:

- **Strictement inférieur/superieur** à un autre, on utilise les operateurs `<` et `>` respectivement
- **Inférieur ou egal/superieur ou egal** à un autre, on utilise les operateurs `<=` et `>=` respectivement

`>>> 120 > 5` 

`>>> False`      

`>>> 3 <= 3`     

`>>> True`      

### Exercice

x=250, y=120. Faire un programme qui donne `True, True, False` avec les operateurs `==, <, >=`'''

widget = Text(mainFrame,height='20')
setTextWidget(widget, unit_content, 'p')
widget.pack(fill=X,side=LEFT)
Button(mainFrame,text='Next Page >',).pack(side=RIGHT)#command=nextPage
Button(mainFrame,text='Back to dashboard',).pack(side=RIGHT)#command=back

root.mainloop()