
unit_content1='''
# Lambda

En Python, une lambda est une fonction anonyme, c'est-à-dire une fonction sans nom. Elle est généralement utilisée dans des situations où une fonction simple est requise pour une opération ponctuelle, souvent dans des contextes où vous ne voulez pas définir une fonction formelle.

Voici la syntaxe générale d'une lambda en Python :
'''
code_block1='''
```
lambda arguments: expression
```
'''
unit_content2='''
Voici un exemple simple d'utilisation d'une lambda : '''
code_block2='''
```
addition = lambda x, y: x + y
print(addition(3, 4))  # Cela affichera 7

```
'''
unit_content3='''
Dans cet exemple, lambda x, y: x + y crée une fonction qui prend deux arguments x et y, et renvoie la somme de ces deux arguments. La lambda est ensuite assignée à la variable addition, et cette variable est utilisée comme une fonction normale pour effectuer l'addition de 3 et 4.'''

unit_content = [(unit_content1, 'text'), (code_block1, 'code'),
                 (unit_content2, 'text'), (code_block2, 'code'),
                 (unit_content3, 'text')]
unit_title = 'Lambda'
import chapters.chapter1.unit2 as nextFrame
import chapters.chapter7selector as previousFrame

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
        titleText = 'Fonctions'
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
        self.retour=tk.PhotoImage(file='sources/assets/ElementDivers/retour.png')
        self.retourButton=tk.Button(self.mainFrame, image=self.retour, bd=0,command=self.back)
        self.retourButton.configure(bg="#D9D9D9", activebackground="#D9D9D9")
        self.retourButton.pack(pady=20)
    def back(self):
        previousFrame.ChapterFrame(self.root)
        self.mainFrame.pack_forget()
    def nextPage(self):
        nextFrame.Content(self.root)
        self.mainFrame.pack_forget()
    def getHeight(self, targetText: str):
        coef = 1.37
        newlines = len(targetText.splitlines())
        return round(coef * newlines)
