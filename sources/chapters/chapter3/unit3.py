

unit_content1='''# Operateurs 3: Operateurs d’assignation

### **Opérations d'affectation**

Dans **Operateurs 2** on a vu comment stocker des resultats dans des variables, et comment performer des operations sur celles ci
Par consequences, on peut stocker les resultats des operations que l’on performe dans une variable **dans la meme variable:**
'''
code_block1='''
x=1

x=x+1

print(x)
'''
unit_content2='''
Dans cette exemple, on obtient 2, car `x = 1`, donc on subsititue x par 1 dans  `x = x + 1` ce qui nous donne `x = 1 + 1 = 2`

Un autre exemple:'''
code_block2='''

a = 3

a = a * (2 + a)

print(a)
'''
unit_content3='''
Le programme affiche 15 car en substituant a pour 3, on obtient `a = 3 * (2 + 3) = 3 * 5 = 15`

### **Opérateurs d'affectation**

Ce type d’operations est utilise tres frequemment dans Python afin de mettre a jour des variables, au point que Python comporte un operateurs dit **d’assignations** pour chaque une des 7 operations basiques qui permettent **d’effectuer l’operation sur la variable qu’on assigne sans avoir a la referencier 2 fois:**
'''
code_block3='''
x = 1

x += 1

print(x)
'''
unit_content4='''
Ce programme effectue la meme operation que l’**Exemple 1.**

L’operateur `+=` est l’operateur d’assignation qui permet d’ajouter une valeur a la valeur stockee dans la variable.

Le reste des operateurs d’assignations sont:

`-=`: **Soustrait** une valeur a la valeur stockee dans la variable.

`*=`: **Multiplie** une valeur par la valeur stockee dans la variable.

`/=`: **Divise** une valeur par la valeur stockee dans la variable.

`//=`: Obtient le **quotient** de la division une d’valeur par la valeur stockee dans la variable.

`%=`: Obtient le **reste** de la division d’une valeur par la valeur stockee dans la variable.

`**=`: Mets la valeur stockee dans la variable **a la puissance** d’une valeur'''
unit_content = [(unit_content1, 'text'), (code_block1, 'code'),
                 (unit_content2, 'text'), (code_block2, 'code'),
                 (unit_content3, 'text'), (code_block3, 'code'),
                 (unit_content4, 'text')]
unit_title = "Operateurs 3 (operateurs d'assignations)"
import chapters.chapter3.quiz3 as nextFrame
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
