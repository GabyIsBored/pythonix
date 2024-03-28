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