<<<<<<< HEAD
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

root.mainloop()
=======
unit_content1:'''
# Declarer un dictionnaire

Un dictionnaire Python est une collection d'éléments non ordonnés. Chaque élément est une paire clé-valeur, où chaque valeur a une clé unique qui nous permet de l’acceder.

Syntaxe : défini avec des accolades **`{}`**, les paires clé-valeur sont séparées par des virgules et les clés et les valeurs par **`:`**:
'''
code_block1:'''
```
mon_dictionnaire = {'clé1': valeur1, 'clé2': valeur2, ...}
```
'''
unit_content2:'''
### **Accès aux Valeurs**

Les valeurs dans un dictionnaire sont accessibles en utilisant la notation d'indexation avec la clé correspondante.
'''
code_block2:'''
```
eleves = {'premier': 'Jean', 'second': 'Paul', 'troisieme': 'Lea'}
secondEleve= eleves['second']
print(secondEleve) # Affiche 'Lea'
```
'''
unit_content3:'''
### **Modification des Valeurs**

Les valeurs dans un dictionnaire peuvent être modifiées en accédant à la clé et en lui attribuant une nouvelle valeur.
'''
code_block3:'''
```
eleves = {'premier': 'Jean', 'second': 'Paul', 'troisieme': 'Lea'}
eleves['second'] = 'Elias'
print(secondEleve) # Affiche 'Elias'
```
'''
unit_content4:'''
### **Ajout et Suppression d'Éléments**

Vous pouvez ajouter de nouvelles paires clé-valeur à un dictionnaire en assignant une valeur à une nouvelle clé. De même, vous pouvez supprimer des éléments en utilisant l'instruction **`del`** ou la méthode **`pop()`**.
'''
code_block4:'''
```
eleves = {'premier': Jean, 'second': Paul, 'troisieme': 'Lea'}
del mon_dictionnaire["troisieme"]
valeur_supprimée = eleves.pop("second")
print(eleves) # Affiche {'premier': 'Jean'}
print(valeur_supprimée) # Affiche 'Lea'
```
'''
unit_content5:'''
### **Parcours**

Vous pouvez parcourir un dictionnaire à l'aide de boucles **`for`**, généralement en itérant sur les clés, les valeurs ou les items (paires clé-valeur).
'''
code_block5:'''
```
for clé in mon_dictionnaire:
    print(clé, "->", mon_dictionnaire[clé])

for valeur in mon_dictionnaire.values():
    print(valeur)

for clé, valeur in mon_dictionnaire.items():
    print(clé, "->", valeur)
```
'''
>>>>>>> 5e4795ad3db8bd44e219213fe62ebf5e5b4ef899
