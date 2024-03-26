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

unit_content1='''
# Lambda

En Python, une lambda est une fonction anonyme, c'est-à-dire une fonction sans nom. Elle est généralement utilisée dans des situations où une fonction simple est requise pour une opération ponctuelle, souvent dans des contextes où vous ne voulez pas définir une fonction formelle.

Voici la syntaxe générale d'une lambda en Python :
'''
code_block1='''
```
lambda arguments: expression
```
'''
unit_content2='''
Voici un exemple simple d'utilisation d'une lambda : '''
code_block2='''
```
addition = lambda x, y: x + y
print(addition(3, 4))  # Cela affichera 7

```
'''
unit_content3='''
Dans cet exemple, lambda x, y: x + y crée une fonction qui prend deux arguments x et y, et renvoie la somme de ces deux arguments. La lambda est ensuite assignée à la variable addition, et cette variable est utilisée comme une fonction normale pour effectuer l'addition de 3 et 4.'''

unit_content1Text = Text(mainFrame,height='20')
code_block1Text = Text(mainFrame,height='20')
unit_content2Text = Text(mainFrame,height='20')
code_block2Text = Text(mainFrame,height='20')
unit_content3Text = Text(mainFrame,height='20')
code_block3Text = Text(mainFrame,height='20')

setTextWidget(unit_content1Text,unit_content1, 'p')
setTextWidget(code_block1Text,code_block1, 'c')
setTextWidget(unit_content2Text,unit_content2, 'p')
setTextWidget(code_block2Text,code_block2, 'c')
setTextWidget(unit_content3Text,unit_content3, 'p')


unit_content1Text.pack(fill=X,side=LEFT)
code_block1Text.pack(fill=X,side=LEFT)
unit_content2Text.pack(fill=X,side=LEFT)
code_block2Text.pack(fill=X,side=LEFT)
unit_content3Text.pack(fill=X,side=LEFT)

Button(mainFrame,text='Next Page >',).pack(side=RIGHT)#command=nextPage
Button(mainFrame,text='Back to dashboard',).pack(side=RIGHT)#command=back
root.mainloop()