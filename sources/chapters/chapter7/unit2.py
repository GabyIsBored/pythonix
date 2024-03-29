

unit_content1='''
# Parametres et la fonction return
Paramètres positionnels : Ce sont les paramètres les plus courants. Vous les utilisez en spécifiant les valeurs dans l'ordre où les paramètres sont définis dans la fonction.
Exemple :
'''
code_block1='''
```
def addition(a, b):
    return a + b
result = addition(3, 5)  # a = 3, b = 5
```
'''
unit_content2='''
**Définition de la fonction :**

- **`def addition(a, b):`** : Cette ligne crée une fonction appelée **`addition`** qui prend deux nombres comme entrées (**`a`** et **`b`**).

**Appel de la fonction :**

- **`result = addition(3, 5)`** : Cette ligne appelle la fonction **`addition`** avec les nombres **`3`** et **`5`** comme arguments.

**Calcul dans la fonction :**

- Dans la fonction **`addition`**, **`a`** est **`3`** et **`b`** est **`5`**.
- La fonction ajoute ces deux nombres ensemble : **`3 + 5`**, ce qui donne **`8`**.

**Affectation du résultat :**

- Le résultat de l'addition, **`8`**, est stocké dans la variable **`result`**.

**Paramètres par mots-clés :** Vous pouvez spécifier le nom des paramètres lors de l'appel de la fonction. Cela vous permet de ne pas vous soucier de l'ordre des paramètres.
2. **Paramètres par mots-clés :** Vous pouvez spécifier le nom des paramètres lors de l'appel de la fonction. Cela vous permet de ne pas vous soucier de l'ordre des paramètres.
    
    Exemple :
'''
code_block2='''
```
def addition(a, b):
    return a + b

result = addition(b=5, a=3)  # a = 3, b = 5 (ordre différent)
```
'''
unit_content3='''
3. **Paramètres par défaut :** Vous pouvez définir des valeurs par défaut pour les paramètres de fonction. Si vous n'en fournissez pas lors de l'appel de la fonction, les valeurs par défaut sont utilisées.
    
    Exemple :
'''
code_block3='''
```
def saluer(nom='Mon ami'):
    return 'Bonjour, ' + nom

print(saluer())  # "Bonjour, Mon ami"
print(saluer('Alice'))  # "Bonjour, Alice"
```
'''
unit_content4='''
4. **Paramètres variables :** Vous pouvez accepter un nombre variable d'arguments en utilisant **`args`** pour les positionnels et **`*kwargs`** pour les arguments par mots-clés.
    
    Exemple :
'''
code_block4='''
```
def fonction_var_pos(*args):
    for arg in args:
        print(arg)

fonction_var_pos(1, 2, 3, 4)

def fonction_var_kw(**kwargs):
    for cle, valeur in kwargs.items():
        print(f"{cle}: {valeur}")

fonction_var_kw(a=1, b=2, c=3)
```
'''
unit_content5='''
En utilisant ces différentes techniques, vous pouvez rendre vos fonctions plus flexibles et plus faciles à utiliser dans différentes situations.
'''
unit_content = [(unit_content1, 'text'), (code_block1, 'code'),
                 (unit_content2, 'text'), (code_block2, 'code'),
                 (unit_content3, 'text'), (code_block3, 'code'),
                 (unit_content4, 'text'), (code_block4, 'code'),
                 (unit_content5, 'text')]
unit_title = 'Parametres et la fonction return'

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
        codeBlock3 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(code_block3), width=50)
        textBlock4 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(unit_content4), width=100)
        codeBlock4 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(code_block4), width=50)
        textBlock5 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(unit_content5), width=100)


        setTextWidget(textBlock1, unit_content1, 'p')
        setTextWidget(codeBlock1, code_block1, 'c')
        setTextWidget(textBlock2, unit_content2, 'p')
        setTextWidget(codeBlock1, code_block2, 'c')
        setTextWidget(textBlock1, unit_content3, 'p')
        setTextWidget(codeBlock1, code_block3, 'c')
        setTextWidget(textBlock2, unit_content4, 'p')
        setTextWidget(codeBlock1, code_block4, 'c')
        setTextWidget(textBlock1, unit_content5, 'p')


        textBlock1.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock1.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock2.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock2.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock3.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock3.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock4.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock4.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock5.pack(padx=45, pady=35, anchor=tk.NW)
        
        

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
