


unit_content1='''# Operateurs 2: Variables

### Stocker les résultats d'opérations aux variables

Les résultats calcules peuvent êtres sauvegarder dans l’interprète en leur assignant en nom
'''
code_block1='''
>>> a = 1+1                     
'''
unit_content2='''
Dans ce cas, le résultat de `1+1` est stocke dans la variable `a` .

(Il est recommande de nommer les variables de manière intuitive au lieu qu’avec des lettres)

On peut accéder a la variable dans la console en utilisant le nom `a`:'''
code_block2='''
>>> a          

2          
'''
unit_content3='''
On peut donc créer un programme qui effectue des calculs grâces a ces variables

Les variables ne sont pas seulement des façons de stocker des résultats, on peut aussi performer des opérations avec elles:'''
code_block3='''
>>> a = 2             

>>> b = a*2               

>>> b                

4             
'''
unit_content4='''
Dans cette exemple, on multiplie la valeur de a, qui a été précédemment assignée par `a = 2`

donc `b = a*2` est équivalent a `b= 2*2`**. b est donc égal a 4**

### Faire un programme effectuant nos opérations

Jusque la nous avons vu les opérations d’arithmétique en communiquant directement avec l’interprète python, mais on peut aussi faire un programme qui performe et affiche ces opérations directement

### Exemple:

Voici un programme qui mets la variable `x` au cube et affiche le résultat:'''

code_block4='''
x = 3

print(x*x*x) # Ce programme affiche 27'''

unit_content = [(unit_content1, 'text'), (code_block1, 'code'),
                 (unit_content2, 'text'), (code_block2, 'code'),
                 (unit_content3, 'text'), (code_block3, 'code'),
                 (unit_content4, 'text'), (code_block4, 'code')]
unit_title = 'Operateur 2 (variables)'
import chapters.chapter3.quiz2 as nextFrame
import chapters.chapter3selector as previousFrame
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
        titleText = 'Arithmetique et Comparaisons'
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

        

        setTextWidget(textBlock1, unit_content1, 'p')
        setTextWidget(codeBlock1, code_block1, 'c')
        setTextWidget(textBlock2, unit_content2, 'p')
        setTextWidget(codeBlock1, code_block2, 'c')
        setTextWidget(textBlock1, unit_content3, 'p')
        setTextWidget(codeBlock1, code_block3, 'c')
        setTextWidget(textBlock2, unit_content4, 'p')
        setTextWidget(codeBlock1, code_block4, 'c')


        textBlock1.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock1.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock2.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock2.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock3.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock3.pack(padx=55, pady=10, anchor=tk.NW)
        textBlock4.pack(padx=45, pady=35, anchor=tk.NW)
        codeBlock4.pack(padx=55, pady=10, anchor=tk.NW)

        
        

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
