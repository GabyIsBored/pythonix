
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
unit_content = [(unit_content1, 'text'), (code_block1, 'code'),
                 (unit_content2, 'text'), (code_block2, 'code'),
                 (unit_content3, 'text')]
unit_title = 'Conditions elif/else'

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
        titleText = 'Conditions'
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

        

        setTextWidget(textBlock1, unit_content1, 'p')
        setTextWidget(codeBlock1, code_block1, 'c')
        setTextWidget(textBlock2, unit_content2, 'p')
        setTextWidget(codeBlock1, code_block2, 'c')
        setTextWidget(textBlock1, unit_content3, 'p')
        

        textBlock1.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock1.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock2.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock2.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock3.pack(padx=45, pady=35, anchor=tk.NW)
        

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
