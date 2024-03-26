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
=======
unit_content1:'''
# Boucle while

Les boucles `while` sont des fonctions qui permettent d'exécuter un bloc de code tant qu'une condition spécifiée est vraie. Voici la syntaxe générale d'une boucle `while` en Python :
'''
code_block1:'''
```
while condition:
    # Bloc de code à exécuter tant que la condition est vraie

```
'''
unit_content2:'''
Explications des éléments clés :

- `condition` : Une expression booléenne. Tant que cette condition est évaluée à `True`, le bloc de code à l'intérieur de la boucle est exécuté. Si la condition devient `False`, la boucle s'arrête, et le programme passe à l'instruction suivante après la boucle `while`.
- Bloc de code : Les instructions à exécuter tant que la condition est vraie. Ces instructions sont indentées (décalées vers la droite) pour indiquer qu'elles font partie du corps de la boucle.

Exemple simple de boucle `while` :
'''
code_block2:'''
```
count = 0
while count < 5:
    print(count)
    count += 1
```
'''
unit_content3:'''
Dans cet exemple, la boucle `while` continue d'exécuter le bloc de code tant que la variable `count` est inférieure à 5. À chaque itération, la valeur de `count` est affichée, puis incrémentée de 1. Une fois que `count` atteint 5, la condition devient `False`, et la boucle se termine.

Il est important de faire attention à éviter les boucles infinies, où la condition reste toujours vraie, car cela peut entraîner un programme qui ne se termine jamais. Pour éviter cela, assurez-vous que la condition de la boucle `while` finit par devenir `False` à un moment donné.
'''

unit_content1Text = Text(mainFrame,height='20')
code_block1Text = Text(mainFrame,height='20')
unit_content2Text = Text(mainFrame,height='20')
code_block2Text = Text(mainFrame,height='20')
unit_content3Text = Text(mainFrame,height='20')


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
>>>>>>> 5e4795ad3db8bd44e219213fe62ebf5e5b4ef899
Button(mainFrame,text='Next Page >',).pack(side=RIGHT)#command=nextPage
Button(mainFrame,text='Back to dashboard',).pack(side=RIGHT)#command=back

root.mainloop()