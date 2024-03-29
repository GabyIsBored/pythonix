
unit_content1='''
# Boucles: break/continue

Les instructions `break` et `continue` sont utilisées dans les boucles (`for` ou `while`) pour contrôler le flux d'exécution du programme.

### `break` :

L'instruction `break` est utilisée pour sortir immédiatement d'une boucle, quel que soit l'état de la condition de la boucle. Cela permet de terminer prématurément l'exécution de la boucle.

### Exemple avec une boucle `for` :
'''
code_block1='''
```
for i in range(5):
    if i == 3:
        break
    print(i)
```
'''
unit_content2='''
Output :
'''
code_block2='''
```
0
1
2
```
'''
unit_content3='''
Dans cet exemple, la boucle `for` itère de 0 à 4. Lorsque `i` atteint la valeur 3, l'instruction `break` est rencontrée, et la boucle est immédiatement interrompue, sautant les itérations restantes.

### Exemple avec une boucle `while` :
'''
code_block3='''
```
count = 0
while count < 5:
    print(count)
    if count == 2:
        break
    count += 1

```
'''
unit_content4='''
Output :
'''
code_block4='''
```
0
1
2
```
'''
unit_content5='''
Ici, la boucle `while` s'exécute jusqu'à ce que `count` atteigne 5. Lorsque `count` atteint 2, l'instruction `break` est exécutée, interrompant la boucle prématurément.

### `continue` :

L'instruction `continue` est utilisée pour passer à l'itération suivante d'une boucle immédiatement, sautant le reste du bloc de code à l'intérieur de la boucle pour cette itération.

### Exemple avec une boucle `for` :
'''
code_block5='''
```
for i in range(5):
    if i == 2:
        continue
    print(i)
```
'''
unit_content6='''
Output :
'''
code_block6='''
```
0
1
3
4

```
'''
unit_content7='''
Ici, lorsque `i` atteint la valeur 2, l'instruction `continue` est exécutée. Cela provoque le saut du reste du bloc de code à l'intérieur de la boucle pour cette itération, passant immédiatement à l'itération suivante.

### Exemple avec une boucle `while` :
'''
code_block7='''
```
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)
```
'''
unit_content8='''
Output :
'''
code_block8='''
```
1
2
4
5
```
'''
unit_content9='''
Dans cet exemple, lorsque `count` atteint la valeur 3, l'instruction `continue` est exécutée, sautant l'impression de cette valeur et passant à l'itération suivante de la boucle `while`.

REMARQUE: Il est conseilé de n’utiliser ces fonctions que lorsque necessaire, car elle peuvent rendre le code plus compliqué et moins lisible dans la plupart des cas  simplifier le programme afin de ne plus necessiter leurs utilisation
'''
unit_content = [(unit_content1, 'text'), (code_block1, 'code'),
                 (unit_content2, 'text'), (code_block2, 'code'),
                 (unit_content3, 'text'), (code_block3, 'code'),
                 (unit_content4, 'text'), (code_block4, 'code'),
                 (unit_content5, 'text'), (code_block5, 'code'),
                (unit_content6, 'text'), (code_block6, 'code'),
                 (unit_content7, 'text'), (code_block7, 'code'),
                 (unit_content8, 'text'), (code_block8, 'code'),
                 (unit_content9, 'text')]
unit_title = 'Boucles: break/continue'
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
