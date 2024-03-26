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

unit_content1='''# Comparaisons

Python est capable d'effectuer toute une série de comparaisons entre le contenu de deux variables,

en renvoyant un **booleen** `True` ou `False` si la comparaisons est verifiee ou pas.

### Egalite et inegalites

Pour tester l’égalité de contenu entre deux valeurs, on utilise l’operateur `==` :'''
code_block1='''

>>> 2 == 3  

False 

>>> 3 == 3  

True'''
unit_content2='''
Pour tester l’inégalité de contenu entre deux valeurs, on utilise l’operateur `!=` :'''
code_block2='''
>>> 2 != 3  

False 
'''
unit_content3='''
### **Infériorité et supériorité, stricts ou larges**

Pour savoir si un objet est:

- **Strictement inférieur/superieur** à un autre, on utilise les operateurs `<` et `>` respectivement
- **Inférieur ou egal/superieur ou egal** à un autre, on utilise les operateurs `<=` et `>=` respectivement
'''
code_block3='''
>>> 120 > 5 

False      

>>> 3 <= 3     

True'''

unit_content1Text = Text(mainFrame,height='20')
code_block1Text = Text(mainFrame,height='20')
unit_content2Text = Text(mainFrame,height='20')
code_block2Text = Text(mainFrame,height='20')
unit_content3Text = Text(mainFrame,height='20')
code_block3Text = Text(mainFrame,height='20')
setTextWidget(unit_content1Text,unit_content1, 'p')
setTextWidget(code_block1Text,code_block1, 'c')
setTextWidget(unit_content2Text,unit_content2, 'p')
setTextWidget(code_block1Text,code_block2, 'c')
setTextWidget(unit_content2Text,unit_content3, 'p')
setTextWidget(code_block1Text,code_block3, 'c')
unit_content1Text.pack(fill=X,side=LEFT)
code_block1Text.pack(fill=X,side=LEFT)
unit_content2Text.pack(fill=X,side=LEFT)
code_block2Text.pack(fill=X,side=LEFT)
unit_content3Text.pack(fill=X,side=LEFT)
code_block3Text.pack(fill=X,side=LEFT)
Button(mainFrame,text='Next Page >',).pack(side=RIGHT)#command=nextPage
Button(mainFrame,text='Back to dashboard',).pack(side=RIGHT)#command=back

<<<<<<< HEAD
### Exercice

x=250, y=120. Faire un programme qui donne `True, True, False` avec les operateurs `==, <, >=`'''
=======
root.mainloop()
>>>>>>> 5e4795ad3db8bd44e219213fe62ebf5e5b4ef899
