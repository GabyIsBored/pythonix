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


unit_content1='''# Operateurs 2: Variables

### Stocker les résultats d'opérations aux variables

Les résultats calcules peuvent êtres sauvegarder dans l’interprète en leur assignant en nom
'''
code_block1='''
>>> a = 1+1                     
'''
unit_content2='''
Dans ce cas, le résultat de `1+1` est stocke dans la variable `a` .

(Il est recommande de nommer les variables de manière intuitive au lieu qu’avec des lettres)

On peut accéder a la variable dans la console en utilisant le nom `a`:'''
code_block2='''
>>> a          

2          
'''
unit_content3='''
On peut donc créer un programme qui effectue des calculs grâces a ces variables

Les variables ne sont pas seulement des façons de stocker des résultats, on peut aussi performer des opérations avec elles:'''
code_block3='''
>>> a = 2             

>>> b = a*2               

>>> b                

4             
'''
unit_content4='''
Dans cette exemple, on multiplie la valeur de a, qui a été précédemment assignée par `a = 2`

donc `b = a*2` est équivalent a `b= 2*2`**. b est donc égal a 4**

### Faire un programme effectuant nos opérations

Jusque la nous avons vu les opérations d’arithmétique en communiquant directement avec l’interprète python, mais on peut aussi faire un programme qui performe et affiche ces opérations directement

### Exemple:

Voici un programme qui mets la variable `x` au cube et affiche le résultat:'''

code_block4='''
x = 3

print(x*x*x) # Ce programme affiche 27'''

unit_content1Text = Text(mainFrame,height='20')
code_block1Text = Text(mainFrame,height='20')
unit_content2Text = Text(mainFrame,height='20')
code_block2Text = Text(mainFrame,height='20')
unit_content3Text = Text(mainFrame,height='20')
code_block3Text = Text(mainFrame,height='20')
unit_content4Text = Text(mainFrame,height='20')
code_block4Text = Text(mainFrame,height='20')

setTextWidget(unit_content1Text,unit_content1, 'p')
setTextWidget(code_block1Text,code_block1, 'c')
setTextWidget(unit_content2Text,unit_content2, 'p')
setTextWidget(code_block2Text,code_block2, 'c')
setTextWidget(unit_content3Text,unit_content3, 'p')
setTextWidget(code_block3Text,code_block3, 'c')
setTextWidget(unit_content4Text,unit_content4, 'p')
setTextWidget(code_block4Text,code_block4, 'c')

unit_content1Text.pack(fill=X,side=LEFT)
code_block1Text.pack(fill=X,side=LEFT)
unit_content2Text.pack(fill=X,side=LEFT)
code_block2Text.pack(fill=X,side=LEFT)
unit_content3Text.pack(fill=X,side=LEFT)
code_block3Text.pack(fill=X,side=LEFT)
unit_content4Text.pack(fill=X,side=LEFT)
code_block4Text.pack(fill=X,side=LEFT)
Button(mainFrame,text='Next Page >',).pack(side=RIGHT)#command=nextPage
Button(mainFrame,text='Back to dashboard',).pack(side=RIGHT)#command=back


root.mainloop()