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

unit_content1='''# Conditions elif/else

### Condition avec `else`

L'opérateur `else` en Python est utilisé dans le contexte des structures conditionnelles (généralement avec l'instruction `if`). Il permet d'indiquer un bloc de code à exécuter lorsque la condition associée à l'instruction `if` est évaluée comme fausse.

## Exemple'''

code_block1='''
```python
age = 15
if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")
```'''
unit_content2='''
Explication :

1. **Déclaration de la variable :**
    - `age` est déclarée et initialisée avec la valeur 15.
2. **Condition `if` :**
    - La condition teste si la valeur de `age` est supérieure ou égale à 18.
    - Si cette condition est vraie, le bloc de code indenté sous l'instruction `if` est exécuté.
3. **Bloc de code à exécuter si la condition est vraie :**
    - Si l'âge est effectivement supérieur ou égal à 18, le programme imprime le message "Vous êtes majeur."
4. **Instruction `else` :**
    - Si la condition de l'instruction `if` est fausse, le bloc de code indenté sous l'instruction `else` est exécuté.
5. **Bloc de code à exécuter si la condition est fausse :**
    - Si l'âge est inférieur à 18, le programme imprime le message "Vous êtes mineur."

### Conditions multiples avec `elif`

L'opérateur `elif` en Python est une contraction de "else if", et il est utilisé dans le contexte des structures conditionnelles pour gérer plusieurs conditions dans une séquence. Cela permet de tester plusieurs conditions l'une après l'autre jusqu'à ce qu'une condition soit vraie, auquel cas le bloc de code associé à cette condition est exécuté. Voici un exemple pour illustrer son utilisation :
'''
code_block2='''
```python
score = 85
if score >= 90:
    print("Excellent!")
elif 80 <= score < 90:
    print("Très bien.")
else:
    print("À améliorer.")
```
'''
unit_content3='''
Dans cet exemple :

- La première condition, `score >= 90`, est évaluée. Si elle est vraie, le bloc de code sous `if` est exécuté, et le programme sort de la structure conditionnelle.
- Si la première condition est fausse, le programme passe à la condition suivante, `80 <= score < 90` avec `elif`. Si cette condition est vraie, le bloc de code sous `elif` est exécuté.
- Si aucune des conditions précédentes n'est vraie, le bloc de code sous `else` est exécuté.

L'utilisation de `elif` est utile lorsque vous avez plusieurs conditions à tester séquentiellement. Cela évite l'imbrication excessive de `if` et `else` et rend le code plus lisible.
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

Button(mainFrame,text='Next Page >',).pack(side=RIGHT)#command=nextPage
Button(mainFrame,text='Back to dashboard',).pack(side=RIGHT)#command=back

root.mainloop()