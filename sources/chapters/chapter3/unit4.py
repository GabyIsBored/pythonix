from markdown import setTextWidget
import tkinter as tk
root=tk.Tk()
root.title('Dashboard')
root.geometry('1280x720')
root.resizable(False,False)
mainFrame=tk.Frame(root)
mainFrame.pack(expand=True, fill='both',padx=10,pady=10)
h1Font = ('Inter', 34, "bold")
mainFrame.configure(bg='#D9D9D9')

unit_content1='''# Comparaisons

Python est capable d'effectuer toute une série de comparaisons entre le contenu de deux variables,

en renvoyant un **booleen** `True` ou `False` si la comparaisons est verifiee ou pas.

### Egalite et inegalites

Pour tester l’égalité de contenu entre deux valeurs, on utilise l’operateur `==` :'''
code_block1='''

>>> 2 == 3  

False 

>>> 3 == 3  

True'''
unit_content2='''
Pour tester l’inégalité de contenu entre deux valeurs, on utilise l’operateur `!=` :'''
code_block2='''
>>> 2 != 3  

False 
'''
unit_content3='''
### **Infériorité et supériorité, stricts ou larges**

Pour savoir si un objet est:

- **Strictement inférieur/superieur** à un autre, on utilise les operateurs `<` et `>` respectivement
- **Inférieur ou egal/superieur ou egal** à un autre, on utilise les operateurs `<=` et `>=` respectivement
'''
code_block3='''
>>> 120 > 5 

False      

>>> 3 <= 3     

True'''
unit_content = [(unit_content1, 'text'), (code_block1, 'code'),
                 (unit_content2, 'text'), (code_block2, 'code'),
                 (unit_content3, 'text'), (code_block3, 'code')]
unit_title = 'Comparaisons'
import chapters.chapter3.quiz4 as nextFrame
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