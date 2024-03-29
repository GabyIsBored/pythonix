
unit_content1='''# Conditions If

## Introduction

Les conditions `if` en Python permettent d'exécuter des blocs de code uniquement si une certaine condition est vraie. Elles sont essentielles pour le contrôle de flux dans un programme.

## Syntaxe de base

La structure de base d'une instruction `if` en Python est la suivante :

'''
code_block1='''
```python
if condition:
    # Bloc de code à exécuter si la condition est vraie
```'''
unit_content2='''
L'indentation (décalage vers la droite) est cruciale en Python pour délimiter le bloc de code à exécuter.

La condition doit toujours renvoyer un booleen (Vrai ou Faux). Les comparaisons (vues dans le chapitre precedent) sont utilisées pour obtenir ce type de résultat. Elles permettent de réaliser une multitude de tests et de vérifications essentiels dans le bon déroulement d'un programme.

## Exemples

### Exemple 1 : Condition simple
'''
code_block2='''
```python
if 20 > 18:
    print("Condition validee")
```'''
unit_content3='''

Puisque 20 > 18 est vraie, le bloc de code contenu sous la condition s’execute, et donc la phrase `‘Condition validee”` s’affiche

### Exemple 2 : Condition simple avec variable

'''
code_block3='''```python
age = 18
if age >= 18:
    print("Vous êtes majeur.")
```
'''
unit_content4='''
Puisque 18 ≥ 18 est vraie, le bloc de code contenu sous la condition s’execute, et donc la phrase `‘Vous êtes majeur.”` s’affiche
'''
unit_content = [(unit_content1, 'text'), (code_block1, 'code'),
                 (unit_content2, 'text'), (code_block2, 'code'),
                 (unit_content3, 'text'), (code_block3, 'code'),
                 (unit_content4, 'text')]
unit_title = 'Conditions if'
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
        titleText = 'Affectation d’une variable'
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

        

        setTextWidget(textBlock1, unit_content1, 'p')
        setTextWidget(codeBlock1, code_block1, 'c')
        setTextWidget(textBlock2, unit_content2, 'p')
        setTextWidget(codeBlock1, code_block2, 'c')
        setTextWidget(textBlock1, unit_content3, 'p')
        setTextWidget(codeBlock1, code_block3, 'c')
        setTextWidget(textBlock2, unit_content4, 'p')


        textBlock1.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock1.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock2.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock2.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock3.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock3.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock4.pack(padx=45, pady=35, anchor=tk.NW)

        
        

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
