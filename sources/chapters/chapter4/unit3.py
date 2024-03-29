
mainFrame.configure(bg='#D9D9D9')

unit_content1='''# Operateurs logiques

### Combinaison de Conditions

Utilisation des opérateurs logiques `and`, `or`, et `not` pour combiner plusieurs conditions.

`and` : la condition est vraie que si toutes les conditions sont vraies

`or` : la condition est vraie si une des conditions est vraie

`not` : la condition est vraie que si l’inverse de la condition est vrai
'''
code_block1='''
```python
temperature = 25
time_of_day = "après-midi"

if temperature > 20 and time_of_day == "après-midi":
    print("Il fait chaud dans l'après-midi.")
```
'''
unit_content2='''
Explication :

1. **Déclaration de variables :**
    - `temperature` est définie à 25.
    - `time_of_day` est définie comme "après-midi".
2. **Condition `if` :**
    - La condition teste deux choses simultanément avec l'opérateur logique `and` :
        - Si la `temperature` est supérieure à 20.
        - Si `time_of_day` est égal à "après-midi".
    - Si les deux conditions sont vraies, le bloc de code indenté sous l'instruction `if` est exécuté.
3. **Bloc de code à exécuter :**
    - Si la condition est vraie, le programme imprime le message "Il fait chaud dans l'après-midi."

Dans ce cas, puisque `temperature` est effectivement supérieure à 20 et `time_of_day` est "après-midi", la condition est vraie, et le message sera affiché.

### Utilisation de "in" pour Vérifier l'Appartenance

- Vérifier si un élément est présent dans une liste, un tuple, ou une chaîne de caractères.'''
code_block2='''
```python
fruits = ['pomme', 'banane', 'orange']
if 'banane' in fruits:
    print("La banane est dans la liste de fruits.")
```
'''
unit_content3='''
**Explications :**

1. **Création de la liste de fruits :**
    - `fruits` est une liste qui contient les éléments 'pomme', 'banane', et 'orange'.
2. **Condition `if` :**
    - La condition utilise l'opérateur `in` pour vérifier si la chaîne de caractères 'banane' est présente dans la liste `fruits`.
    - Si cette condition est vraie, le bloc de code indenté sous l'instruction `if` est exécuté.
3. **Bloc de code à exécuter si la condition est vraie :**
    - Si 'banane' est dans la liste, le programme imprime le message "La banane est dans la liste de fruits."

Dans cet exemple, la condition est vraie car 'banane' est effectivement un élément de la liste `fruits`. Par conséquent, le message "La banane est dans la liste de fruits." sera affiché lors de l'exécution du programme.
'''

unit_content = [(unit_content1, 'text'), (code_block1, 'code'),
                 (unit_content2, 'text'), (code_block2, 'code'),
                 (unit_content3, 'text')]
unit_title = 'Operateurs Logiques'

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
