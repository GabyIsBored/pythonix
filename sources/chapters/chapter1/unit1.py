
unit_content1='''
# Premiers pas

Prêts à commencer? Tout d'abord, nous apprendrons comment afficher une chaîne de caractères. Pour cela, nous étudierons le programme ci-dessous. Le premier programme aura pour but d'afficher la phrase **'Hello World!'** grâce à la fonction **print**. Cette fonction affiche ce qu'elle prend en **argument** dans le **Terminal**. Dans ce cas, cet **argument** est la phrase **'Hello World!'**
'''
code_block1='''
print('Hello World!')
>>> Hello World!
'''
unit_content2='''
Cela nous donne bien un **output** de **Hello World!**

La fonction **print** prends en paramètre la phrase **‘Hello World!’**, mise en cotations afin de signaler que cette phrase ne fait pas partie des **commandes** Python, elle doit être purement interprétée en tant que phrase que le programme devra manipuler et/ou afficher dans notre **Terminal**

Pour programmer, il faut être très vigilant sur l’orthographe des commandes, car si il y a une faute sur l’orthographe, notre interpréteur, dans ce cas le langage Python, ne pourra pas les identifier comme étant des commandes et le programme ne fonctionnera pas

Et si notre programme contient plusieurs lignes de code, dites **statements**?

Certains langages de programmation, dits **langages compilés** traduisent tout le code en langage machine avant l'exécution, créant un fichier exécutable distinct, tandis que les **langages interprétés** traduisent et exécutent le code ligne par ligne à la volée. 

Python est considéré comme un langage interprété donc les commandes sont exécutées ligne par ligne.

La fonction activée en premier et affichée avant la fonction activée après (cela veut dire qu’on ne peut pas utiliser une variable  ou une fonction avant de l’avoir déclarée
'''
unit_content = [(unit_content1, 'text'), (code_block1, 'code'),
                 (unit_content2, 'text')]
unit_title = 'Premiers Pas'

import chapters.chapter1.unit2 as nextFrame
import chapters.chapter1selector as previousFrame
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
        titleText = 'Introduction'
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
