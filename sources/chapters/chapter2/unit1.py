unit_content1='''# Variables

### Introduction aux variables

En programmation, une variable est un espace de stockage qui porte **un nom**, et a **une valeur.** 

Cette valeur peut etre un nombre fit un int, ou une chaine de caractere dite une string, qu’on mets entre guillemets 

Une variable peut être représentée comme un tiroir portant une étiquette dans lequel on peut ranger des données. Les variables permettent de conserver et de manipuler des données au cours de l’exécution d’un programme.

### Exemple 1
'''
code_block1='''
python
nom = “John”
age = 32
'''
unit_content2='''

Dans ce block de code, le tiroir **nom** a pour valeur “John” et le tiroir **âge** a pour valeur 32.

Dans cet exemple, on utilise des guillemets pour indiquer que **John** n’est pas une variable mais bien du texte, aussi appelé chaîne de caractères en programmation.

### Exemple 2

Maintenant qu’on a nos variables, on peut les afficher à l’aide de la fonction **print()**

- **print** est le nom de la fonction que l’on va *appeler*
- **print** est une fonction *native* qui permet d’afficher dans la console les *arguments* qui ont été passés
- ce qu’il y a à l’intérieur des () correspond aux *paramètres* (ou *arguments*) de la fonction **print**.
'''
code_block2='''
python
nom = “John”
print(nom)
'''
unit_content3='''
Après l’exécution de ce programme, on voit dans la console le contenu (les données) stockées dans la variable nom.

Nommer des variables
Quand on crée une variable, il est important que son nom corresponde à son usage ou à sa fonction dans le programme
Le nom d’une variable ne peut pas contenir d’espace
Le nom d’une variable ne peut pas être un nombre
Crée deux variables ayant le même nom résultera en une erreur
Il est préférable d’éviter les noms de variables trop long
Il est préférable de ne pas utiliser d’accent dans le nom d’une variable

La casse significative
La notion de "casse significative" se réfère à l'utilisation intentionnelle de majuscules ou de minuscules dans les noms de variables pour transmettre des informations sur leur rôle ou leur nature. En spécifiant une seule casse significative vous améliorez la lisibilité de votre code et facilitez la compréhension des variables par d'autres développeurs.

La casse significative contribue ainsi à rendre le code plus clair et cohérent.

Vous pouvez retenir ces deux conventions courantes :

La camelCase
  Les mots commencent par des majuscules, sauf le premier.
  Exemple : nomDeVariable

La snake_case
  Les mots sont séparés par des underscores (tirets du 8) et sont généralement en minuscules.
Exemple : nom_de_variable'''

unit_content = [(unit_content1, 'text'), (code_block1, 'code'),
                 (unit_content2, 'text'), (code_block2, 'code'),
                   (unit_content3, 'text')]
unit_title = 'Variables'


import chapters.chapter2.quiz1 as nextFrame
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
        self.mainFrame.pack_forget()
        nextFrame.Content(self.root)
    def getHeight(self, targetText: str):
        coef = 1.37
        newlines = len(targetText.splitlines())
        return round(coef * newlines)
