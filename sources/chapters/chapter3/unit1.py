


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
unit_content = [(unit_content1, 'text'), (code_block1, 'code'),
                 (unit_content2, 'text')]
unit_title = 'Operateurs 1 (elementaires)'
import chapters.chapter3.quiz1 as nextFrame
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