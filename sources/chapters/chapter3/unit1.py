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

unit_content1Text = tk.Text(mainFrame,height='20')
code_block1Text = tk.Text(mainFrame,height='20')
unit_content2Text = tk.Text(mainFrame,height='20')
setTextWidget(unit_content1Text,unit_content1, 'p')
setTextWidget(code_block1Text,code_block1, 'c')
setTextWidget(unit_content2Text,unit_content2, 'p')
unit_content1Text.pack(fill=tk.X,side=tk.LEFT)
code_block1Text.pack(fill=tk.X,side=tk.LEFT)
unit_content2Text.pack(fill=tk.X,side=tk.LEFT)
tk.Button(mainFrame,text='Next Page >',).pack(side=tk.RIGHT)#command=nextPage
tk.Button(mainFrame,text='Back to dashboard',).pack(side=tk.RIGHT)#command=back

root.mainloop()