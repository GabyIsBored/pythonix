

unit_content1='''
# Boucle while

Les boucles `while` sont des fonctions qui permettent d'exécuter un bloc de code tant qu'une condition spécifiée est vraie. Voici la syntaxe générale d'une boucle `while` en Python :
'''
code_block1='''
```
while condition:
    # Bloc de code à exécuter tant que la condition est vraie

```
'''
unit_content2='''
Explications des éléments clés :

- `condition` : Une expression booléenne. Tant que cette condition est évaluée à `True`, le bloc de code à l'intérieur de la boucle est exécuté. Si la condition devient `False`, la boucle s'arrête, et le programme passe à l'instruction suivante après la boucle `while`.
- Bloc de code : Les instructions à exécuter tant que la condition est vraie. Ces instructions sont indentées (décalées vers la droite) pour indiquer qu'elles font partie du corps de la boucle.

Exemple simple de boucle `while` :
'''
code_block2='''
```
count = 0
while count < 5:
    print(count)
    count += 1
```
'''
unit_content3='''
Dans cet exemple, la boucle `while` continue d'exécuter le bloc de code tant que la variable `count` est inférieure à 5. À chaque itération, la valeur de `count` est affichée, puis incrémentée de 1. Une fois que `count` atteint 5, la condition devient `False`, et la boucle se termine.

Il est important de faire attention à éviter les boucles infinies, où la condition reste toujours vraie, car cela peut entraîner un programme qui ne se termine jamais. Pour éviter cela, assurez-vous que la condition de la boucle `while` finit par devenir `False` à un moment donné.
'''
unit_content = [(unit_content1, 'text'), (code_block1, 'code'),
                 (unit_content2, 'text'), (code_block2, 'code'),
                 (unit_content3, 'text')]
unit_title = 'Boucle while'

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
