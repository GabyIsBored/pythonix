
unit_content1='''
# Listes

Une liste est une structure de données qui permet de stocker une collection ordonnée d'éléments.

Pour déclarer une liste en Python, vous pouvez utiliser les crochets `[]` et séparer les éléments de la liste par des virgules. Voici quelques exemples de déclaration de listes :

- Liste vide : `ma_liste_vide = []`
- Liste avec des éléments : `fruits = ['pomme', 'banane', 'orange']`
- Liste avec différents types de données :`mixte = [1, 'deux', 3.0, True]`

On peut aussi faire des listes contenant des listes, nommées matrices, ou liste multidimensionnelle:

`matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`

Et enfin on peux utiliser la fonction `list()` afin d’arranger des éléments dans une listes de façon dynamique:`jours_semaine = list(('lundi', 'mardi', 'mercredi','jeudi', 'vendredi'))`

### Indexation des éléments :

Pour faire reference a un element particulier de la liste, on mets :
'''
code_block1='''
```
element = liste[indice]
```
'''
unit_content2='''
Un indice est un un nombre entier utilisé pour identifier un élément en indiquant la position relative de l'élément à l'intérieur de la séquence.

En Python, les indices commencent généralement à 0. Ainsi, le premier élément d'une séquence a l'indice 0, le deuxième a l'indice 1, et ainsi de suite. Vous pouvez également utiliser des indices négatifs pour accéder aux éléments depuis la fin de la séquence, où -1 représente le dernier élément, -2 le deuxième en partant de la fin, et ainsi de suite.
'''
code_block2='''
```
premier_element = liste[0]  # Accès au premier élément
dernier_element = liste[-1]  # Accès au dernier élément
```
'''
unit_content3='''
### Modification des éléments :

Vous pouvez modifier les éléments d'une liste en utilisant leur indice.
'''
code_block3='''
```
fruits = ['pomme', 'banane', 'orange']
fruits[1] = 'kiwi'
print(fruits)  # Affiche ['pomme', 'kiwi', 'orange']
```
'''

unit_content4='''
### Ajout d'éléments :

Vous pouvez ajouter des éléments à une liste en utilisant la méthode `append()` ou avec l'opérateur
'''
code_block4='''
```
fruits = ['pomme', 'banane', 'orange']

fruits.append('fraise')
print(fruits)  # Affiche ['pomme', 'banane', 'orange', 'fraise']

legumes = ['carotte', 'brocoli']
nourriture = fruits + legumes
print(nourriture)  # Affiche ['pomme', 'banane', 'orange', 'fraise', 'carotte', 'brocoli']
```
'''
unit_content5='''
# Methodes

Voici quelques methodes qui nous permettent de manipuler les listes:

- La fonction `len()` renvoie la longueur d'une liste, c'est-à-dire le nombre d'éléments qu'elle contient.
'''
code_block5='''
```
fruits = ['pomme', 'banane', 'orange']

nombre_elements = len(fruits)
print(nombre_elements)  # Affiche 3
```
'''
unit_content6='''
extend(iterable) : Ajoute tous les éléments d'un itérable (tel qu'une autre liste) à la fin de la liste.
'''
code_block6='''
```
my_list = [1, 2, 3]
other_list = [4, 5, 6]
my_list.extend(other_list)
print(my_list)  # Affichage : [1, 2, 3, 4, 5, 6]


```
'''
unit_content7='''
insert(index, item) : Insère un élément à un index spécifié.
'''
code_block7='''
```
my_list = [1, 2, 3]
my_list.insert(1, 10)
print(my_list)  # Affichage : [1, 10, 2, 3]


```
'''
unit_content8='''
remove(item) : Supprime la première occurrence d'un élément spécifié dans la liste.
'''
code_block8='''
```
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Affichage : [1, 3, 2]


```
'''
unit_content9='''
pop([index]) : Supprime et retourne l'élément à l'index spécifié. Si aucun index n'est spécifié, supprime et retourne le dernier élément de la liste.
'''
code_block9='''
```
my_list = [1, 2, 3]
popped_item = my_list.pop()
print(popped_item)  # Affichage : 3
print(my_list)      # Affichage : [1, 2]


```
'''
unit_content10='''
index(item) : Retourne l'index de la première occurrence d'un élément spécifié dans la liste.
'''
code_block10='''
```
my_list = [1, 2, 3, 2]
index = my_list.index(2)
print(index)  # Affichage : 1

```
'''
unit_content11='''
count(item) : Retourne le nombre d'occurrences d'un élément spécifié dans la liste.
'''
code_block11='''
```
my_list = [1, 2, 3, 2]
count = my_list.count(2)
print(count)  # Affichage : 2


```
'''
unit_content12='''
sort(key=None, reverse=False) : Trie les éléments de la liste. Le paramètre key permet un tri personnalisé basé sur une fonction, et le paramètre reverse spécifie s'il faut trier par ordre décroissant.
'''
code_block12='''
```
my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # Affichage : [1, 2, 3]

# Avec reverse=True
my_list.sort(reverse=True)
print(my_list)  # Affichage : [3, 2, 1]


```
'''
unit_content13='''
reverse() : Inverse l'ordre des éléments dans la liste.
'''
code_block13='''
```
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Affichage : [3, 2, 1]


```
'''
unit_content14='''
clear() : Supprime tous les éléments de la liste.
'''
code_block14='''
```
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Affichage : []


```
'''
unit_content = [(unit_content1, 'text'), (code_block1, 'code'),
                 (unit_content2, 'text'), (code_block2, 'code'),
                 (unit_content3, 'text'), (code_block3, 'code'),
                 (unit_content4, 'text'), (code_block4, 'code'),
                 (unit_content5, 'text'), (code_block5, 'code'),
                (unit_content6, 'text'), (code_block6, 'code'),
                 (unit_content7, 'text'), (code_block7, 'code'),
                 (unit_content8, 'text'), (code_block8, 'code'),
                 (unit_content9, 'text'), (code_block9, 'code'),
                (unit_content10, 'text'), (code_block10, 'code'),
                (unit_content11, 'text'), (code_block11, 'code'),
                 (unit_content12, 'text'), (code_block12, 'code'),
                 (unit_content13, 'text'), (code_block13, 'code'),
                 (unit_content14, 'text'), (code_block14, 'code')]
unit_title = 'Listes'

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
        titleText = 'Listes et Dicitionnaires'
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
        textBlock6 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(unit_content6), width=100)
        codeBlock6 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(code_block6), width=50)
        textBlock7 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(unit_content7), width=100)
        codeBlock7 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(code_block7), width=50)
        textBlock8 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(unit_content8), width=100)
        codeBlock8 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(code_block8), width=50)
        textBlock9 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(unit_content9), width=100)
        codeBlock9 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(code_block9), width=50)
        textBlock10 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(unit_content10), width=100)
        codeBlock10 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(code_block10), width=50)
        textBlock11 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(unit_content11), width=100)
        codeBlock11 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(code_block11), width=50)
        textBlock12 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(unit_content12), width=100)
        codeBlock12 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(code_block12), width=50)
        textBlock13 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(unit_content13), width=100)
        codeBlock13 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(code_block13), width=50)
        textBlock14 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(unit_content14), width=100)
        codeBlock14 = tk.Text(master=self.mainFrame, relief='flat', height=self.getHeight(code_block14), width=50)
        

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
        setTextWidget(textBlock2, unit_content6, 'p')
        setTextWidget(codeBlock1, code_block6, 'c')
        setTextWidget(textBlock1, unit_content7, 'p')
        setTextWidget(codeBlock1, code_block7, 'c')
        setTextWidget(textBlock2, unit_content8, 'p')
        setTextWidget(codeBlock1, code_block8, 'c')
        setTextWidget(textBlock1, unit_content9, 'p')
        setTextWidget(codeBlock1, code_block9, 'c')
        setTextWidget(textBlock2, unit_content10, 'p')
        setTextWidget(codeBlock1, code_block10, 'c')
        setTextWidget(textBlock1, unit_content11, 'p')
        setTextWidget(codeBlock1, code_block11, 'c')
        setTextWidget(textBlock2, unit_content12, 'p')
        setTextWidget(codeBlock1, code_block12, 'c')
        setTextWidget(textBlock1, unit_content13, 'p')
        setTextWidget(codeBlock1, code_block13, 'c')
        setTextWidget(textBlock2, unit_content14, 'p')
        setTextWidget(codeBlock1, code_block14, 'c')

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
        textBlock6.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock6.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock7.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock7.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock8.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock8.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock9.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock9.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock10.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock10.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock11.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock11.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock12.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock12.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock13.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock13.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock14.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock14.pack(padx=55, pady=10, anchor=tk.NW)
        
        

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
