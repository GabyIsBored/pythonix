from markdown import setTextWidget
import tkinter as tk
root=tk.Tk()
root.title('Dashboard')
root.geometry('1280x720')
root.resizable(False,False)
mainFrame=tk.Frame(root)
mainFrame.pack(expand=True, fill='both',padx=10,pady=10)
h1Font = ('Inter', 34, "bold")
mainFrame.configure(bg='#D9D9D9')

unit_content1='''
# Dictionnaires

Un dictionnaire Python est une collection d'éléments non ordonnés. Chaque élément est une paire clé-valeur, où chaque valeur a une clé unique qui nous permet de l’acceder.

Syntaxe : défini avec des accolades **`{}`**, les paires clé-valeur sont séparées par des virgules et les clés et les valeurs par **`:`**:
'''
code_block1='''
```
mon_dictionnaire = {'clé1': valeur1, 'clé2': valeur2, ...}
```
'''
unit_content2='''
### **Accès aux Valeurs**

Les valeurs dans un dictionnaire sont accessibles en utilisant la notation d'indexation avec la clé correspondante.
'''
code_block2='''
```
eleves = {'premier': 'Jean', 'second': 'Paul', 'troisieme': 'Lea'}
secondEleve= eleves['second']
print(secondEleve) # Affiche 'Lea'
```
'''
unit_content3='''
### **Modification des Valeurs**

Les valeurs dans un dictionnaire peuvent être modifiées en accédant à la clé et en lui attribuant une nouvelle valeur.
'''
code_block3='''
```
eleves = {'premier': 'Jean', 'second': 'Paul', 'troisieme': 'Lea'}
eleves['second'] = 'Elias'
print(secondEleve) # Affiche 'Elias'
```
'''
unit_content4='''
### **Ajout et Suppression d'Éléments**

Vous pouvez ajouter de nouvelles paires clé-valeur à un dictionnaire en assignant une valeur à une nouvelle clé. De même, vous pouvez supprimer des éléments en utilisant l'instruction **`del`** ou la méthode **`pop()`**.
'''
code_block4='''
```
eleves = {'premier': Jean, 'second': Paul, 'troisieme': 'Lea'}
del mon_dictionnaire["troisieme"]
valeur_supprimée = eleves.pop("second")
print(eleves) # Affiche {'premier': 'Jean'}
print(valeur_supprimée) # Affiche 'Lea'
```
'''
unit_content5='''
### **Parcours**

Vous pouvez parcourir un dictionnaire à l'aide de boucles **`for`**, généralement en itérant sur les clés, les valeurs ou les items (paires clé-valeur).
'''
code_block5='''
```
for clé in mon_dictionnaire:
    print(clé, "->", mon_dictionnaire[clé])

for valeur in mon_dictionnaire.values():
    print(valeur)

for clé, valeur in mon_dictionnaire.items():
    print(clé, "->", valeur)
```
'''
unit_content = [(unit_content1, 'text'), (code_block1, 'code'),
                 (unit_content2, 'text'), (code_block2, 'code'),
                 (unit_content3, 'text'), (code_block3, 'code'),
                 (unit_content4, 'text'), (code_block4, 'code'),
                   (unit_content5, 'text'), (code_block5, 'code')]
unit_title = 'Dictionnaires'

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
