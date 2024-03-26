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

unit_content1='''# Boucles for

Les boucles for sont un fonction qui nous permet de repeter une ou plusieurs fois l’execution d’un blocs de code selon la valeur d’un parametre nommé “iterable” .
'''code_block1='''
```python
for var in itérable :
    # instructions
```
'''unit_content2='''
Ici, `itérable` est une collection d'objets comme des listes, des tuples. Le bloc de code indenté à l'intérieur des boucles for sont exécutées une fois pour chaque élément d'un itérable.

 La variable `var` prend la valeur de **l'élément suivant** de `itérable`à chaque passage dans la boucle

## Boucle Python For dans une liste
'''code_block2='''
```python
chiffres = [1, 2, 3, 4, 5]

for chiffre in chiffres:
    print(chiffre)
```
'''unit_content3='''
1. **`chiffres = [1, 2, 3, 4, 5]`**: Cette ligne crée une liste appelée **`chiffres`** qui contient les chiffres de 1 à 5.
2. **`for chiffre in chiffres:`**: Cette ligne commence une boucle "for". Elle dit essentiellement : "pour chaque élément dans la liste **`chiffres`**, exécute le bloc de code suivant".
3. **`print(chiffre)`**: À l'intérieur de la boucle, cette ligne imprime la valeur de chaque élément de la liste **`chiffres`**. À chaque itération de la boucle, la variable **`chiffre`** prend la valeur de l'élément actuel de la liste, et cette valeur est imprimée.

Ainsi, lorsque la boucle est exécutée, le programme imprime chaque chiffre de la liste **`chiffres`** sur une nouvelle ligne, résultant en l'affichage :
'''code_block3='''
```python
>>> 1
>>> 2
>>> 3
>>> 4
>>> 5
```
'''unit_content4='''
## Boucle Python For dans une string

Ce code utilise une boucle for pour parcourir une **[chaîne](https://www.geeksforgeeks.org/python-string/)** et imprimer chaque caractère sur une nouvelle ligne. La boucle attribue chaque caractère à la variable i et continue jusqu'à ce que tous les caractères de la chaîne aient été traités.
'''code_block4='''
```python
string = "Pythonix"

for charactere in string:
	print(charactere)
```
'''unit_content5='''
- **`string = "Pythonix"`** : Cette ligne initialise une variable de chaîne appelée **`string`** avec la valeur "Pythonix".
- **`for character in string:`** : Cette ligne démarre une boucle **`for`** qui itère sur chaque caractère de la chaîne **`string`**. À chaque itération, la variable **`character`** prend la valeur du caractère actuel.
- **`print(character)`** : À l'intérieur de la boucle, l'instruction **`print`** est utilisée pour afficher la valeur de la variable **`character`**. Cela imprime chaque caractère de la chaîne sur une nouvelle ligne.

Ainsi, lorsque ce code est exécuté, il produira la sortie suivante :
'''
code_block5='''
>>> P
>>> y
>>> t
>>> h
>>> o
>>> n
>>> i
>>> x
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
setTextWidget(code_block3Text,code_block4, 'c')
setTextWidget(unit_content4Text,unit_content5, 'p')
setTextWidget(code_block3Text,code_block5, 'c')

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