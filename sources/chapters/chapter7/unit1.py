from markdown import setTextWidget
import tkinter as tk
root=tk.Tk()
root.title('Dashboard')
root.geometry('1280x720')
root.resizable(False,False)
mainFrame=tk.Frame(root)
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
code_block1='''
```
def nom_de_la_fonction():
    # Bloc de code à exécuter si la fonction est apellee
    
nom_de_la_fonction() # Execution de la fonction
```
'''
unit_content2='''
- `def` : Mot-clé utilisé pour déclarer une fonction.
- `nom_de_la_fonction` : Nom de la fonction, suivi de parenthèses. Pour l’instant les parentheses restent vide

## Ou utiliser une fonction?
'''
code_block2='''
```
def nom_de_la_fonction():
    # Bloc de code à exécuter si la fonction est apellee
    
nom_de_la_fonction() # Execution de la fonction
```
'''
unit_content = [(unit_content1, 'text'), (code_block1, 'code'),
                 (unit_content2, 'text'), (code_block2, 'code')]
unit_title = 'Declarer une fonction'