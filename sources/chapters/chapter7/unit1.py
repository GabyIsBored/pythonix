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
Button(mainFrame,text='Next Page >',).pack(side=RIGHT)#command=nextPage
Button(mainFrame,text='Back to dashboard',).pack(side=RIGHT)#command=back

=======
unit_content1='''
# Declarer une fonction

En Python, les fonctions sont comme des boîtes qui contiennent **des morceaux de code réutilisables.** 

Plutôt que de répéter le même code, elles vous permettent d’appeler une fonction chaque fois que vous avez besoin d'effectuer une tâche particulière. 

La réutilisation du code et rend votre programme plus structuré.

## Déclaration d'une fonction :

La syntaxe de base pour déclarer une fonction est la suivante :
'''
code_block1:'''
```
def nom_de_la_fonction():
    # Bloc de code à exécuter si la fonction est apellee
    
nom_de_la_fonction() # Execution de la fonction
```
'''
unit_content2:'''
- `def` : Mot-clé utilisé pour déclarer une fonction.
- `nom_de_la_fonction` : Nom de la fonction, suivi de parenthèses. Pour l’instant les parentheses restent vide

## Ou utiliser une fonction?
'''
code_block2:'''
```
def nom_de_la_fonction():
    # Bloc de code à exécuter si la fonction est apellee
    
nom_de_la_fonction() # Execution de la fonction
```
'''
unit_content1Text = Text(mainFrame,height='20')
code_block1Text = Text(mainFrame,height='20')
unit_content2Text = Text(mainFrame,height='20')
code_block2Text = Text(mainFrame,height='20')
setTextWidget(unit_content1Text,unit_content1, 'p')
setTextWidget(code_block1Text,code_block1, 'c')
setTextWidget(unit_content2Text,unit_content2, 'p')
setTextWidget(code_block2Text,code_block1, 'c')
unit_content1Text.pack(fill=X,side=LEFT)
code_block1Text.pack(fill=X,side=LEFT)
unit_content2Text.pack(fill=X,side=LEFT)
code_block2Text.pack(fill=X,side=LEFT)
Button(mainFrame,text='Next Page >',).pack(side=RIGHT)#command=nextPage
Button(mainFrame,text='Back to dashboard',).pack(side=RIGHT)#command=back
>>>>>>> 5e4795ad3db8bd44e219213fe62ebf5e5b4ef899
root.mainloop()