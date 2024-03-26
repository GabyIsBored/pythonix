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

unit_content1='''# Affectation d’une variable

### L’opérateur ‘=’

Le symbole ‘=’ permet d’assigner à une variable une certaine valeur :

`x = 1`

- x étant la variable crée (son ‘nom’)
- 1 étant sa valeur d’initialisation (sa ‘valeur’)

On appel ce symbole un *opérateur* et fait partie des opérateurs d’assignation. Il existe de nombreux opérateurs, parmis lequels figurent les opérateurs **d’assignations**, les opérateurs **arithmétiques**, les opérateurs **de comparaison** etc… Ils seront donc introduits dans un prochain chapitre.

### Autre propriété d’affectation

Une variable peut également être initialisée à partir de la valeur stockée dans une autre variable.

De cette manière on peut utiliser la valeur d’une variable et lui faire subir des modifications sans modifier la variable dont la valeur a été copié.

### Exemple 1'''
code_block1='''unit_content1=
defaultValue = 50           # defaultVaue est initialisé avec 50

testValue = defaultValue    # testValue est initialisé avec defaultValue (50)

testValue = 20              # defaultValue est toujours égale à 50'''
unit_content2='''
REMARQUE : Lors de la déclaration d’une variable, elle doit avoir une valeur d’initialisation ou le programme résultera en une erreur.

- Ligne 1: la variable `defaultValue` est crée, et initialisée avec le nombre entier 50.
- Ligne 2: la variable `testValue` est crée, et initialisée avec la valeur qui est stockée dans la variable `defaultValue` , 50 dans ce cas.
- Ligne 3: la variable `testValue` subit une modification, sa valeur précédente se fait ‘écraser’ et se  fait remplacer par 20.'''
unit_content1Text = Text(mainFrame,height='20')
code_block1Text = Text(mainFrame,height='20')
unit_content2Text = Text(mainFrame,height='20')
setTextWidget(unit_content1Text,unit_content1, 'p')
setTextWidget(code_block1Text,code_block1, 'c')
setTextWidget(unit_content2Text,unit_content2, 'p')
unit_content1Text.pack(fill=X,side=LEFT)
code_block1Text.pack(fill=X,side=LEFT)
unit_content2Text.pack(fill=X,side=LEFT)
Button(mainFrame,text='Next Page >',).pack(side=RIGHT)#command=nextPage
Button(mainFrame,text='Back to dashboard',).pack(side=RIGHT)#command=back

root.mainloop()