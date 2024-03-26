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

widget = Text(mainFrame,height='20')
setTextWidget(widget, unit_content, 'p')
rwidget = Text(mainFrame,height='20')
setTextWidget(rwidget, remarques, 'r')
widget.pack(fill=X,side=LEFT)
rwidget.pack(fill=X,side=RIGHT)
Button(mainFrame,text='Next Page >',).pack(side=RIGHT)#command=nextPage
Button(mainFrame,text='Back to dashboard',).pack(side=RIGHT)#command=back

root.mainloop()