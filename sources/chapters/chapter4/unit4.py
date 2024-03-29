

unit_content1='''# Conditions imbriquees

Les conditions imbriquées, également appelées structures conditionnelles imbriquées, se produisent lorsque vous placez une structure conditionnelle à l'intérieur d'une autre. Cela permet de gérer des scénarios plus complexes en évaluant plusieurs conditions de manière hiérarchique. Voici un exemple d'utilisation de conditions imbriquées en Python :
'''
code_block1='''
```python
age = 25
sexe = "homme"

if age >= 18:
    print("Vous êtes majeur.")

    if sexe == "homme":
        print("Bienvenue, Monsieur!")
    else:
        print("Bienvenue, Madame!")

else:
    print("Vous êtes mineur.")
```
'''
unit_content2='''
Explication :
Explications :

1. La première condition (`if age >= 18:`) vérifie si l'âge est supérieur ou égal à 18.
    - Si cette condition est vraie, le bloc de code indenté sous cet `if` est exécuté.
    - À l'intérieur de ce bloc, une autre condition est évaluée.
2. La deuxième condition (`if sexe == "homme":`) vérifie si le sexe est égal à "homme".
    - Si cette condition est vraie, le bloc de code indenté sous cette deuxième `if` est exécuté et affiche "Bienvenue, Monsieur!".
    - Si la condition est fausse, le bloc de code indenté sous le `else` de la deuxième `if` est exécuté, affichant "Bienvenue, Madame!".
3. Si la première condition (`if age >= 18:`) est fausse, le bloc de code indenté sous le `else` de la première `if` est exécuté, affichant "Vous êtes mineur.".'''

unit_content = [(unit_content1, 'text'), (code_block1, 'code'),
                 (unit_content2, 'text')]
unit_title = 'Conditions imbriquees'
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

        

        setTextWidget(textBlock1, unit_content1, 'p')
        setTextWidget(codeBlock1, code_block1, 'c')
        setTextWidget(textBlock2, unit_content2, 'p')


        textBlock1.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock1.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock2.pack(padx=45, pady=35, anchor=tk.NW)

        
        

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

