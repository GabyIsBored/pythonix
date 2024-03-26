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

<<<<<<< HEAD
unit_content='''# Operateurs 3: Operateurs d’assignation

### **Opérations d'affectation**

Dans **Operateurs 2** on a vu comment stocker des resultats dans des variables, et comment performer des operations sur celles ci
Par consequences, on peut stocker les resultats des operations que l’on performe dans une variable **dans la meme variable:**

Dans cette exemple, on obtient 2, car `x = 1`, donc on subsititue x par 1 dans  `x = x + 1` ce qui nous donne `x = 1 + 1 = 2`

Un autre exemple:

Le programme affiche 15 car en substituant a pour 3, on obtient `a = 3 * (2 + 3) = 3 * 5 = 15`

### **Opérateurs d'affectation**

Ce type d’operations est utilise tres frequemment dans Python afin de mettre a jour des variables, au point que Python comporte un operateurs dit **d’assignations** pour chaque une des 7 operations basiques qui permettent **d’effectuer l’operation sur la variable qu’on assigne sans avoir a la referencier 2 fois:**


Ce programme effectue la meme operation que l’**Exemple 1.**

 ****L’operateur `+=` est l’operateur d’assignation qui permet d’ajouter une valeur a la valeur stockee dans la variable.

Le reste des operateurs d’assignations sont:

`-=`: **Soustrait** une valeur a la valeur stockee dans la variable.

`*=`: **Multiplie** une valeur par la valeur stockee dans la variable.

`/=`: **Divise** une valeur par la valeur stockee dans la variable.

`//=`: Obtient le **quotient** de la division une d’valeur par la valeur stockee dans la variable.

`%=`: Obtient le **reste** de la division d’une valeur par la valeur stockee dans la variable.

`**=`: Mets la valeur stockee dans la variable **a la puissance** d’une valeur

## Exercice

x=3. y=10. x est egal a sa valeur + 5. y est egal a sa valeur - x, x est egale au reste de la divison entre lui meme et y'''
remarques='''
yo oy yoyoyo oy yo
'''
widget = Text(mainFrame,height='20')
setTextWidget(widget, unit_content, 'p')
rwidget = Text(mainFrame,height='20')
setTextWidget(rwidget, remarques, 'r')
widget.pack(fill=X,side=LEFT)
rwidget.pack(fill=X,side=RIGHT)
Button(mainFrame,text='Next Page >',).pack(side=RIGHT)#command=nextPage
Button(mainFrame,text='Back to dashboard',).pack(side=RIGHT)#command=back

=======
unit_content1='''
# Lambda

En Python, une lambda est une fonction anonyme, c'est-à-dire une fonction sans nom. Elle est généralement utilisée dans des situations où une fonction simple est requise pour une opération ponctuelle, souvent dans des contextes où vous ne voulez pas définir une fonction formelle.

Voici la syntaxe générale d'une lambda en Python :
'''
code_block1:'''
```
lambda arguments: expression
```
'''
unit_content2:'''
Voici un exemple simple d'utilisation d'une lambda : '''
code_block2:'''
```
addition = lambda x, y: x + y
print(addition(3, 4))  # Cela affichera 7

```
'''
unit_content3:'''
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
setTextWidget(code_block3Text,code_block3, 'c')

unit_content1Text.pack(fill=X,side=LEFT)
code_block1Text.pack(fill=X,side=LEFT)
unit_content2Text.pack(fill=X,side=LEFT)
code_block2Text.pack(fill=X,side=LEFT)
unit_content3Text.pack(fill=X,side=LEFT)

Button(mainFrame,text='Next Page >',).pack(side=RIGHT)#command=nextPage
Button(mainFrame,text='Back to dashboard',).pack(side=RIGHT)#command=back
>>>>>>> 5e4795ad3db8bd44e219213fe62ebf5e5b4ef899
root.mainloop()