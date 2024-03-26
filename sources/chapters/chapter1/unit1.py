from markdown import setTextWidget
from tkinter import *
import ttkbootstrap as tb
root=tb.Window()
root.title('Dashboard')
root.geometry('1280x720')
root.resizable(False,False)
mainFrame=Frame(root)
mainFrame.pack(expand=True, fill='both',padx=10,pady=10)
h1Font = ('Inter', 34, "bold")
mainFrame.configure(bg='#D9D9D9')

unit_content='''
# Premiers pas

Prêts à commencer? Tout d'abord, nous apprendrons comment afficher une chaîne de caractères. Pour cela, nous étudierons le programme ci-dessous. Le premier programme aura pour but d'afficher la phrase **'Hello World!'** grâce à la fonction **print**. Cette fonction affiche ce qu'elle prend en **argument** dans le **Terminal**. Dans ce cas, cet **argument** est la phrase **'Hello World!'**

Cela nous donne bien un **output** de **Hello World!**

La fonction **print** prends en paramètre la phrase **‘Hello World!’**, mise en cotations afin de signaler que cette phrase ne fait pas partie des **commandes** Python, elle doit être purement interprétée en tant que phrase que le programme devra manipuler et/ou afficher dans notre **Terminal**

Pour programmer, il faut être très vigilant sur l’orthographe des commandes, car si il y a une faute sur l’orthographe, notre interpréteur, dans ce cas le langage Python, ne pourra pas les identifier comme étant des commandes et le programme ne fonctionnera pas

Et si notre programme contient plusieurs **statements**?

Certains languages de programmation, dits **langages compilés** traduisent tout le code en langage machine avant l'exécution, créant un fichier exécutable distinct, tandis que les **langages interprétés** traduisent et exécutent le code ligne par ligne à la volée. 

Python est considéré comme un langage interprété donc les commandes sont executees ligne par ligne.

La fonction activee en premier et affichee avant la fonction activee apres (cela veutdir qu’on ne peut pas utiliser une variable  ou une fonction avant de l’avoir declaree
'''
widget = Text(mainFrame,height='10')
setTextWidget(widget, unit_content, 'p')
widget.pack(fill=X)
Button(mainFrame,text='Next Page >',).pack(side=RIGHT)#command=nextPage
Button(mainFrame,text='Back to dashboard',).pack(side=RIGHT)#command=back

root.mainloop()