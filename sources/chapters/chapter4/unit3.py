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
unit_content1='''# Operateurs logiques

### Combinaison de Conditions

Utilisation des opérateurs logiques `and`, `or`, et `not` pour combiner plusieurs conditions.

`and` : la condition est vraie que si toutes les conditions sont vraies

`or` : la condition est vraie si une des conditions est vraie

`not` : la condition est vraie que si l’inverse de la condition est vrai
'''
code_block1='''
```python
temperature = 25
time_of_day = "après-midi"

if temperature > 20 and time_of_day == "après-midi":
    print("Il fait chaud dans l'après-midi.")
```
'''
unit_content2='''
Explication :

1. **Déclaration de variables :**
    - `temperature` est définie à 25.
    - `time_of_day` est définie comme "après-midi".
2. **Condition `if` :**
    - La condition teste deux choses simultanément avec l'opérateur logique `and` :
        - Si la `temperature` est supérieure à 20.
        - Si `time_of_day` est égal à "après-midi".
    - Si les deux conditions sont vraies, le bloc de code indenté sous l'instruction `if` est exécuté.
3. **Bloc de code à exécuter :**
    - Si la condition est vraie, le programme imprime le message "Il fait chaud dans l'après-midi."

Dans ce cas, puisque `temperature` est effectivement supérieure à 20 et `time_of_day` est "après-midi", la condition est vraie, et le message sera affiché.

### Utilisation de "in" pour Vérifier l'Appartenance

- Vérifier si un élément est présent dans une liste, un tuple, ou une chaîne de caractères.'''
code_block2='''
```python
fruits = ['pomme', 'banane', 'orange']
if 'banane' in fruits:
    print("La banane est dans la liste de fruits.")
```
'''
unit_content3='''
**Explications :**

1. **Création de la liste de fruits :**
    - `fruits` est une liste qui contient les éléments 'pomme', 'banane', et 'orange'.
2. **Condition `if` :**
    - La condition utilise l'opérateur `in` pour vérifier si la chaîne de caractères 'banane' est présente dans la liste `fruits`.
    - Si cette condition est vraie, le bloc de code indenté sous l'instruction `if` est exécuté.
3. **Bloc de code à exécuter si la condition est vraie :**
    - Si 'banane' est dans la liste, le programme imprime le message "La banane est dans la liste de fruits."

Dans cet exemple, la condition est vraie car 'banane' est effectivement un élément de la liste `fruits`. Par conséquent, le message "La banane est dans la liste de fruits." sera affiché lors de l'exécution du programme.
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