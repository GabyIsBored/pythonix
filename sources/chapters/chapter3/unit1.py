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


unit_content1='''# Operateurs 1 (elementaires)

### Effectuer des operations avec Python

Afin de communiquer avec la machine, le language python passe par un **‘interprete Python’**, qui traduit les commandes en **language machine** pour l’ordinateur
Mais on peut directement communiquer avec l’interprete a travers la console Python sans avoir a ecrire un programme

Grace a cet interprete on peut performer des operations Python sans avoir a ecrire un programme.

Python peut performer des operations d’arithmetiques comme une calculatrice.
'''
code_block1='''
>>> 10 * 3 + 5 * 5

65
'''
unit_content2='''
### Liste d’operateurs elementaires

L’addition est notee par le symbole: `+`

La soustraction est notee par le symbole: `-`

La multiplication est notee par le symbole: `*`

La division est notee par le symbole: `/`

REMARQUE: Les nombres a virgule sont notes avec un point et non pas une virgule. Dans Python la virgule sert a separer deux valeurs differentes. 

On peut aussi performer une division euclidienne avec `//` et `%`

Afin d’obtenir le quotient, on utilise: `//` 

Afin d’obtenir le reste, on utilise: `%`

Et enfin, on utilise l’operateur `**` afin d’effectuer une **exponentiation**
'''
<<<<<<< HEAD
<<<<<<< HEAD
rwidget = Text(mainFrame,height='10')
setTextWidget(rwidget, remarques, 'r')
widget = Text(mainFrame,height='10')
setTextWidget(widget, unit_content, 'p')
widget.pack(fill=X)
rwidget.pack(fill=X)
Button(mainFrame,text='Next Page >',).pack(side=RIGHT)#command=nextPage
Button(mainFrame,text='Back to dashboard',).pack(side=RIGHT)#command=back
=======
class UnitContent(Frame):
    def __init__(self, master: Tk):
        super().__init__()
        self.rwidget = Text(master, height='20')
        setTextWidget(self.rwidget, remarques, 'p')
        self.widget = Text(master, height='20')
        setTextWidget(self.widget, unit_content_text, 'r')
        self.widget.pack(fill=X)
        self.rwidget.pack(fill=X)
        Button(master, text='Next Page >').pack(side=RIGHT)  # command=nextPage
        Button(master, text='Back to dashboard').pack(side=RIGHT)  # command=back
        
>>>>>>> 39902c5e36bec554f3cef693d4febeb3e264594f
=======
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

root.mainloop()