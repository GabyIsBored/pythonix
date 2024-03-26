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
root.mainloop()