
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
from markdown import setTextWidget
import tkinter as tk
class Content(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__()
        self.root = master
        for block in unit_content:
            self.widget=tk.Text(master)
            setTextWidget(self.widget,block[0],block[1]) 
            self.widget.pack()   
        continuerImg=tk.PhotoImage(file='sources\assets\ElementDivers\continuer.png')
        self.nextButton = tk.Button(master,image=continuerImg,command=nextPage)
        def nextPage():
            nextFrame.Content(master)
