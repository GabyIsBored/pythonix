
unit_content1='''
# Boucles imbriquees

Les boucles imbriquées en Python sont des boucles placées à l'intérieur d'une autre boucle. Cela signifie qu'il y a une boucle principale (extérieure) et une ou plusieurs boucles secondaires (intérieures) à l'intérieur de celle-ci. Les boucles imbriquées sont souvent utilisées pour parcourir et manipuler des structures de données bidimensionnelles, comme des listes de listes, des matrices ou des tableaux.

La structure générale d'un ensemble de boucles imbriquées ressemble à ceci :
'''
code_block1='''
```
for variable_externe in sequence_externe:
    # Instructions de la boucle externe

    for variable_interne in sequence_interne:
        # Instructions de la boucle interne

```
'''
unit_content2='''
Là où `sequence_externe` est la séquence parcourue par la boucle externe, et `sequence_interne` est la séquence parcourue par la boucle interne.

## Exemple
'''
code_block2='''
```
n = 3

# Boucle externe pour chaque ligne
for i in range(n):
    # Boucle interne pour chaque colonne dans une ligne
    for j in range(n):
        print("*", end=" ")
    print()
```
'''
unit_content3='''
Dans cet exemple, la boucle externe parcourt chaque ligne, et la boucle interne parcourt chaque colonne à l'intérieur de chaque ligne. Le résultat serait :
'''
code_block3='''
```
* * *
* * *
* * *
```
'''
unit_content4='''
Chaque ligne contient trois étoiles, et cela est généré en utilisant des boucles imbriquées pour itérer sur les lignes et les colonnes du motif.
'''
unit_content = [(unit_content1, 'text'), (code_block1, 'code'),
                 (unit_content2, 'text'), (code_block2, 'code'),
                 (unit_content3, 'text'), (code_block3, 'code'),
                 (unit_content4, 'text')]
unit_title = 'Boucles imbriquees'

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
