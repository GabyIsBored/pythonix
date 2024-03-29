
unit_content1='''
# Boucles: range()

La fonction `range()` en Python est utilisée pour générer une séquence d'entiers. Elle est couramment utilisée avec les boucles, en particulier avec les boucles `for`. Voici une explication détaillée de la fonction `range()` :

### Syntaxe :
'''
code_block1='''
```
range(stop)
range(start, stop)
range(start, stop, step)
```
'''
unit_content2='''
- **`start` (optionnel)** : La valeur de départ de la séquence. Si elle n'est pas spécifiée, elle est par défaut à 0.
- **`stop`** : La valeur de fin de la séquence. Elle est exclusive, ce qui signifie que la séquence s'arrête avant d'atteindre cette valeur.
- **`step` (optionnel)** : L'incrément (pas) entre les valeurs de la séquence. Si non spécifié, il est par défaut à 1.

### Exemples :

1. Utilisation de `range()` avec un seul argument (stop) :
'''
code_block2='''
```
for i in range(5):
    print(i)
```
'''
unit_content3='''
Output :
'''
code_block3='''
```
0
1
2
3
4
```
'''
unit_content4='''
- Utilisation de `range()` avec deux arguments (start, stop) :
'''
code_block4='''
```
for i in range(2, 8):
    print(i)
```
'''
unit_content5='''
Output :
'''
code_block5='''
```
2
3
4
5
6
7
```
'''
unit_content6='''
- Utilisation de `range()` avec trois arguments (start, stop, step) :
'''
code_block6='''
```
for i in range(1, 10, 2):
    print(i)
```
'''
unit_content7='''
Output :
'''
code_block7='''
```
1
3
5
7
9
```
'''
unit_content8='''
### Points clés :

- La fonction `range()` génère une séquence d'entiers, mais ne crée pas réellement une liste. Elle génère les valeurs au fur et à mesure des besoins, ce qui la rend plus efficace en termes de mémoire pour de grandes séquences.
- `start`, `stop`, et `step` peuvent être des entiers.
- Si `step` est négatif, `start` doit être plus grand que `stop`, sinon la séquence sera vide.
- `range()` est souvent utilisée dans les boucles `for` pour itérer sur une séquence d'entiers.

### Utilisation de `range()` avec les boucles `for` :

La fonction `range()` est fréquemment utilisée avec les boucles `for` pour créer des itérations sur une séquence d'entiers. L'objectif est de simplifier le processus d'itération en générant automatiquement une séquence d'entiers pour les valeurs de l'indice dans la boucle. Voici comment cela fonctionne en pratique :

1. **Itération sur une séquence de 0 à n-1 :**
'''
code_block8='''
```
n = 5
for i in range(n):
    print(i)
```
'''
unit_content9='''
Output :
'''
code_block9='''
```
0
1
2
3
4
```
'''
unit_content10='''
Dans cet exemple, la boucle `for` itère sur une séquence générée par `range(n)`, qui va de 0 à n-1. À chaque itération, la variable `i` prend la valeur de l'élément actuel de la séquence.

- **Itération avec une valeur de départ personnalisée :**
'''
code_block10='''
```
start = 2
stop = 8
for i in range(start, stop):
    print(i)
```
'''
unit_content11='''
Output :
'''
code_block11='''
```
2
3
4
5
6
7
```
'''
unit_content12='''
En spécifiant une valeur de départ (`start`) et une valeur de fin (`stop`), la boucle `for` itère sur la séquence générée par `range(start, stop)`.

- **Itération avec un pas personnalisé :**
'''
code_block12='''
```
start = 1
stop = 10
step = 2
for i in range(start, stop, step):
    print(i)


```
'''
unit_content13='''
Output :
'''
code_block13='''
1
3
5
7
9
```
'''
unit_content14='''
En ajoutant un troisième argument, `step`, on peut spécifier un pas personnalisé entre les valeurs de la séquence. Cela permet de sauter certaines valeurs pendant l'itération.

L'utilisation de `range()` avec les boucles `for` simplifie le processus d'itération sur une séquence d'entiers, ce qui est couramment utilisé dans de nombreux scénarios de programmation.
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
                 (unit_content14, 'text')]
unit_title = 'Boucles: range()'
import chapters.chapter1.unit2 as nextFrame
import chapters.chapter6selector as previousFrame
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
