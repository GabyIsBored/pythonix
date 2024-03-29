
unit_content1='''# Boucles for

Les boucles for sont un fonction qui nous permet de repeter une ou plusieurs fois l’execution d’un blocs de code selon la valeur d’un parametre nommé “iterable” .
'''
code_block1='''
```python
for var in itérable :
    # instructions
```
'''
unit_content2='''
Ici, `itérable` est une collection d'objets comme des listes, des tuples. Le bloc de code indenté à l'intérieur des boucles for sont exécutées une fois pour chaque élément d'un itérable.

 La variable `var` prend la valeur de **l'élément suivant** de `itérable`à chaque passage dans la boucle

## Boucle Python For dans une liste
'''
code_block2='''
```python
chiffres = [1, 2, 3, 4, 5]

for chiffre in chiffres:
    print(chiffre)
```
'''
unit_content3='''
1. **`chiffres = [1, 2, 3, 4, 5]`**: Cette ligne crée une liste appelée **`chiffres`** qui contient les chiffres de 1 à 5.
2. **`for chiffre in chiffres:`**: Cette ligne commence une boucle "for". Elle dit essentiellement : "pour chaque élément dans la liste **`chiffres`**, exécute le bloc de code suivant".
3. **`print(chiffre)`**: À l'intérieur de la boucle, cette ligne imprime la valeur de chaque élément de la liste **`chiffres`**. À chaque itération de la boucle, la variable **`chiffre`** prend la valeur de l'élément actuel de la liste, et cette valeur est imprimée.

Ainsi, lorsque la boucle est exécutée, le programme imprime chaque chiffre de la liste **`chiffres`** sur une nouvelle ligne, résultant en l'affichage :
'''
code_block3='''
```python
>>> 1
>>> 2
>>> 3
>>> 4
>>> 5
```
'''
unit_content4='''
## Boucle Python For dans une string

Ce code utilise une boucle for pour parcourir une **[chaîne](https://www.geeksforgeeks.org/python-string/)** et imprimer chaque caractère sur une nouvelle ligne. La boucle attribue chaque caractère à la variable i et continue jusqu'à ce que tous les caractères de la chaîne aient été traités.
'''
code_block4='''
```python
string = "Pythonix"

for charactere in string:
	print(charactere)
```
'''
unit_content5='''
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

unit_content = [(unit_content1, 'text'), (code_block1, 'code'),
                 (unit_content2, 'text'), (code_block2, 'code'),
                 (unit_content3, 'text'), (code_block3, 'code'),
                 (unit_content4, 'text'), (code_block4, 'code'),
                   (unit_content5, 'text'), (code_block5, 'code')]
unit_title = 'Boucles for'

import chapters.chapter1.unit2 as nextFrame
import customtkinter as ctk
from markdown import setTextWidget
import tkinter as tk

class Content(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__()

        # initialize mainframe
        self.root = master
        self.mainFrame = ctk.CTkScrollableFrame(master=self.root, fg_color='#D9D9D9', bg_color='#D9D9D9')
        self.mainFrame.pack(expand=True, fill='both')

        # set title
        titleText = 'Boucles'
        titleWidget = ctk.CTkButton(
            master=self.mainFrame, 
            text=titleText, 
            text_color='black', 
            text_color_disabled='black',
            font=('inter', 40, 'bold'), 
            border_color='black', 
            border_width=2, 
            corner_radius=10, 
            fg_color='#D9D9D9', 
            bg_color='#D9D9D9', 
            hover=False,
            state='disabled')
        titleWidget.pack()

        # ------- CONTENT HERE -------
        textBlock1 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(unit_content1), width=100)
        codeBlock1 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(code_block1), width=50)
        textBlock2 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(unit_content2), width=100)
        codeBlock2 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(code_block2), width=50)
        textBlock3 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(unit_content3), width=100)
        codeBlock3 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(code_block3), width=50)
        textBlock4 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(unit_content4), width=100)
        codeBlock4 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(code_block4), width=50)
        textBlock5 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(unit_content5), width=100)
        codeBlock5 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(code_block5), width=50)

        

        setTextWidget(textBlock1, unit_content1, 'p')
        setTextWidget(codeBlock1, code_block1, 'c')
        setTextWidget(textBlock2, unit_content2, 'p')
        setTextWidget(codeBlock1, code_block2, 'c')
        setTextWidget(textBlock1, unit_content3, 'p')
        setTextWidget(codeBlock1, code_block3, 'c')
        setTextWidget(textBlock2, unit_content4, 'p')
        setTextWidget(codeBlock1, code_block4, 'c')
        setTextWidget(textBlock1, unit_content5, 'p')
        setTextWidget(codeBlock1, code_block5, 'c')


        textBlock1.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock1.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock2.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock2.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock3.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock3.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock4.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock4.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock5.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock5.pack(padx=55, pady=10, anchor=tk.NW)

        
        

        # ------- Next page button -------
        self.continuer=tk.PhotoImage(file='sources/assets/ElementDivers/continuer.png')
        self.prochainButton=tk.Button(self.mainFrame, image=self.continuer, bd=0,command=self.nextPage)
        self.prochainButton.configure(bg="#D9D9D9", activebackground="#D9D9D9")
        self.prochainButton.pack(pady=20)

    def nextPage(self):
        nextFrame.Content(self.root)
        self.mainFrame.pack_forget()
    def getHeight(self, targetText: str):
        coef = 1.37
        newlines = len(targetText.splitlines())
        return round(coef * newlines)
