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

unit_content1='''# Indentation

Python n’est pas seulement sensible sur l’ortographe, mais aussi l’indentation des lignes: 
<<<<<<< HEAD
'''
code1='''
if x>0:
    print('x est plus grand que 0)
'''
unit_content2='''
Dans ce cas, la **commande print(’x is a positive number’)** est sous une **condition**, **x>0** (VOIR CHAPITRE ‘CONDITIONS’)

Pour differencier entre les commandes qui sont sous cette condition on avance la commande **print(’x is a positive number’)** en laissant un espace derriere elle

Cet espace doit correspondre au autres commandes qui sont aussi sous la condition **x>0**

Pour montrer que la commande **print(End of program)** s’active independamment de cette condition, elle est situee au meme niveau d’indentation que le **if statement**

Quelques autres exemples:
'''
code2='''
for i in range(10):
    if i==5:
        print('i est 5)
    print(i n'est pas 5)
print('Fin du programme)
'''
unit_contentText = Text(mainFrame,height='10')
setTextWidget(unit_contentText, unit_content1, 'p')
cwidget1Text = Text(mainFrame,height='10')
setTextWidget(cwidget1Text, code1, 'c')
unit_content2Text = Text(mainFrame,height='10')
setTextWidget(unit_content2Text, unit_content2, 'p')
cwidget2Text = Text(mainFrame,height='10')
setTextWidget(cwidget2Text, code2, 'c')


unit_contentText.pack(fill=X)
cwidget1Text.pack(fill=X)
unit_content2Text.pack(fill=X)
cwidget2Text.pack(fill=X)
Button(mainFrame,text='Next Page >',).pack(side=RIGHT)#command=nextPage
Button(mainFrame,text='Back to dashboard',).pack(side=RIGHT)#command=back
=======

'''
code_block1='''
if x>0:
    print(x est un nombre positif')
    print(x est un nombre positif')
print('End of progam')
'''
unit_content2='''
Dans ce cas, la commande `print(’x is a positive number’)` est sous une **condition**, **x>0** (voir le chapitre sur les conditions)

Pour différencier entre les commandes qui sont sous cette condition on avance la commande `print(’x is a positive number’)` en laissant un espace derrière elle

Cet espace doit correspondre au autres commandes qui sont aussi sous la condition **x>0**

Pour montrer que la commande **`**print(End of program)` s’active indépendamment de cette condition, elle est située au même niveau d’indentation que le `if` statetment'''
unit_content1Text = Text(mainFrame,height='20')
code_block1Text = Text(mainFrame,height='20')
unit_content2Text = Text(mainFrame,height='20')
setTextWidget(unit_content1Text,unit_content1, 'p')
setTextWidget(code_block1Text,code_block1, 'c')
setTextWidget(unit_content2Text,unit_content2, 'p')
unit_content1Text.pack(fill=X,side=LEFT)
code_block1Text.pack(fill=X,side=LEFT)
unit_content2Text.pack(fill=X,side=LEFT)
Button(mainFrame,text='Next Page >',).pack(side=RIGHT)#command=nextPage
Button(mainFrame,text='Back to dashboard',).pack(side=RIGHT)#command=back
>>>>>>> 5e4795ad3db8bd44e219213fe62ebf5e5b4ef899
