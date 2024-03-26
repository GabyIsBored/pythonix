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


unit_content='''# Operateurs 1 (elementaires)

### Effectuer des operations avec Python

Afin de communiquer avec la machine, le language python passe par un **‘interprete Python’**, qui traduit les commandes en **language machine** pour l’ordinateur
Mais on peut directement communiquer avec l’interprete a travers la console Python sans avoir a ecrire un programme

Grace a cet interprete on peut performer des operations Python sans avoir a ecrire un programme.

Python peut performer des operations d’arithmetiques comme une calculatrice.

### Liste d’operateurs elementaires

L’addition est notee par le symbole: `+`

La soustraction est notee par le symbole: `-`

La multiplication est notee par le symbole: `*`

La division est notee par le symbole: `/`

REMARQUE: Les nombres a virgule sont notes avec un point et non pas une virgule. Dans Python la virgule sert a separer deux valeurs. 

On peut aussi performer une division euclidienne avec `//` ****et `%`

Afin d’obtenir le quotient, on utilise: `//` 

Afin d’obtenir le reste, on utilise: `%`


Et enfin, on utilise l’operateur `**` afind d’effectuer une **exponentiation**

`>>> 2**3`

`>>> 8`'''
remarques='''

'''
rwidget = Text(mainFrame,height='10')
setTextWidget(rwidget, remarques, 'r')
widget = Text(mainFrame,height='10')
setTextWidget(widget, unit_content, 'p')
widget.pack(fill=X)
rwidget.pack(fill=X)
=======
unit_content1='''# Conditions If

## Introduction

Les conditions `if` en Python permettent d'exécuter des blocs de code uniquement si une certaine condition est vraie. Elles sont essentielles pour le contrôle de flux dans un programme.

## Syntaxe de base

La structure de base d'une instruction `if` en Python est la suivante :

'''
code_block1='''
```python
if condition:
    # Bloc de code à exécuter si la condition est vraie
```'''
unit_content2='''
L'indentation (décalage vers la droite) est cruciale en Python pour délimiter le bloc de code à exécuter.

La condition doit toujours renvoyer un booleen (Vrai ou Faux). Les comparaisons (vues dans le chapitre precedent) sont utilisées pour obtenir ce type de résultat. Elles permettent de réaliser une multitude de tests et de vérifications essentiels dans le bon déroulement d'un programme.

## Exemples

### Exemple 1 : Condition simple
'''
code_block2='''
```python
if 20 > 18:
    print("Condition validee")
```'''
unit_content3='''

Puisque 20 > 18 est vraie, le bloc de code contenu sous la condition s’execute, et donc la phrase `‘Condition validee”` s’affiche

### Exemple 2 : Condition simple avec variable

'''
code_block3='''```python
age = 18
if age >= 18:
    print("Vous êtes majeur.")
```
'''
unit_content4='''
Puisque 18 ≥ 18 est vraie, le bloc de code contenu sous la condition s’execute, et donc la phrase `‘Vous êtes majeur.”` s’affiche
'''

unit_content1Text = Text(mainFrame,height='20')
code_block1Text = Text(mainFrame,height='20')
unit_content2Text = Text(mainFrame,height='20')
code_block2Text = Text(mainFrame,height='20')
unit_content3Text = Text(mainFrame,height='20')
code_block3Text = Text(mainFrame,height='20')
unit_content4Text = Text(mainFrame,height='20')
setTextWidget(unit_content1Text,unit_content1, 'p')
setTextWidget(code_block1Text,code_block1, 'c')
setTextWidget(unit_content2Text,unit_content2, 'p')
setTextWidget(code_block2Text,code_block2, 'c')
setTextWidget(unit_content3Text,unit_content3, 'p')
setTextWidget(code_block3Text,code_block3, 'c')
setTextWidget(unit_content4Text,unit_content4, 'p')

unit_content1Text.pack(fill=X,side=LEFT)
code_block1Text.pack(fill=X,side=LEFT)
unit_content2Text.pack(fill=X,side=LEFT)
code_block2Text.pack(fill=X,side=LEFT)
unit_content3Text.pack(fill=X,side=LEFT)
code_block3Text.pack(fill=X,side=LEFT)
unit_content4Text.pack(fill=X,side=LEFT)
>>>>>>> 5e4795ad3db8bd44e219213fe62ebf5e5b4ef899
Button(mainFrame,text='Next Page >',).pack(side=RIGHT)#command=nextPage
Button(mainFrame,text='Back to dashboard',).pack(side=RIGHT)#command=back

root.mainloop()