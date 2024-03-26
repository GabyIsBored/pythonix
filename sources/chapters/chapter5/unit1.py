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
# Declarer un dictionnaire

Un dictionnaire Python est une collection d'éléments non ordonnés. Chaque élément est une paire clé-valeur, où chaque valeur a une clé unique qui nous permet de l’acceder.

Syntaxe : défini avec des accolades **`{}`**, les paires clé-valeur sont séparées par des virgules et les clés et les valeurs par **`:`**:
'''
code_block1='''
```
mon_dictionnaire = {'clé1': valeur1, 'clé2': valeur2, ...}
```
'''
unit_content2='''
### **Accès aux Valeurs**

Les valeurs dans un dictionnaire sont accessibles en utilisant la notation d'indexation avec la clé correspondante.
'''
code_block2='''
```
eleves = {'premier': 'Jean', 'second': 'Paul', 'troisieme': 'Lea'}
secondEleve= eleves['second']
print(secondEleve) # Affiche 'Lea'
```
'''
unit_content3='''
### **Modification des Valeurs**

Les valeurs dans un dictionnaire peuvent être modifiées en accédant à la clé et en lui attribuant une nouvelle valeur.
'''
code_block3='''
```
eleves = {'premier': 'Jean', 'second': 'Paul', 'troisieme': 'Lea'}
eleves['second'] = 'Elias'
print(secondEleve) # Affiche 'Elias'
```
'''
unit_content4='''
### **Ajout et Suppression d'Éléments**

Vous pouvez ajouter de nouvelles paires clé-valeur à un dictionnaire en assignant une valeur à une nouvelle clé. De même, vous pouvez supprimer des éléments en utilisant l'instruction **`del`** ou la méthode **`pop()`**.
'''
code_block4='''
```
eleves = {'premier': Jean, 'second': Paul, 'troisieme': 'Lea'}
del mon_dictionnaire["troisieme"]
valeur_supprimée = eleves.pop("second")
print(eleves) # Affiche {'premier': 'Jean'}
print(valeur_supprimée) # Affiche 'Lea'
```
'''
unit_content5='''
### **Parcours**

Vous pouvez parcourir un dictionnaire à l'aide de boucles **`for`**, généralement en itérant sur les clés, les valeurs ou les items (paires clé-valeur).
'''
code_block5='''
```
for clé in mon_dictionnaire:
    print(clé, "->", mon_dictionnaire[clé])

for valeur in mon_dictionnaire.values():
    print(valeur)

for clé, valeur in mon_dictionnaire.items():
    print(clé, "->", valeur)
```
'''
unit_content1Text = Text(mainFrame,height='20')
code_block1Text = Text(mainFrame,height='20')
unit_content2Text = Text(mainFrame,height='20')
code_block2Text = Text(mainFrame,height='20')
unit_content3Text = Text(mainFrame,height='20')
code_block3Text = Text(mainFrame,height='20')
unit_content4Text = Text(mainFrame,height='20')
code_block4Text = Text(mainFrame,height='20')
unit_content5Text = Text(mainFrame,height='20')
code_block5Text = Text(mainFrame,height='20')



setTextWidget(unit_content1Text,unit_content1, 'p')
setTextWidget(code_block1Text,code_block1, 'c')
setTextWidget(unit_content2Text,unit_content2, 'p')
setTextWidget(code_block2Text,code_block2, 'c')
setTextWidget(unit_content3Text,unit_content3, 'p')
setTextWidget(code_block3Text,code_block3, 'c')
setTextWidget(unit_content4Text,unit_content4, 'p')
setTextWidget(code_block4Text,code_block4, 'c')
setTextWidget(unit_content5Text,unit_content5, 'p')
setTextWidget(code_block5Text,code_block5, 'c')


unit_content1Text.pack(fill=X,side=LEFT)
code_block1Text.pack(fill=X,side=LEFT)
unit_content2Text.pack(fill=X,side=LEFT)
code_block2Text.pack(fill=X,side=LEFT)
unit_content3Text.pack(fill=X,side=LEFT)
code_block3Text.pack(fill=X,side=LEFT)
unit_content4Text.pack(fill=X,side=LEFT)
code_block4Text.pack(fill=X,side=LEFT)
unit_content5Text.pack(fill=X,side=LEFT)
code_block5Text.pack(fill=X,side=LEFT)
Button(mainFrame,text='Next Page >',).pack(side=RIGHT)#command=nextPage
Button(mainFrame,text='Back to dashboard',).pack(side=RIGHT)#command=back

root.mainloop()
