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


unit_content1='''
# Boucles imbriquees

Les boucles imbriquées en Python sont des boucles placées à l'intérieur d'une autre boucle. Cela signifie qu'il y a une boucle principale (extérieure) et une ou plusieurs boucles secondaires (intérieures) à l'intérieur de celle-ci. Les boucles imbriquées sont souvent utilisées pour parcourir et manipuler des structures de données bidimensionnelles, comme des listes de listes, des matrices ou des tableaux.

La structure générale d'un ensemble de boucles imbriquées ressemble à ceci :
'''
code_block1='''
```
for variable_externe in sequence_externe:
    # Instructions de la boucle externe

    for variable_interne in sequence_interne:
        # Instructions de la boucle interne

```
'''
unit_content2='''
Là où `sequence_externe` est la séquence parcourue par la boucle externe, et `sequence_interne` est la séquence parcourue par la boucle interne.

## Exemple
'''
code_block2='''
```
n = 3

# Boucle externe pour chaque ligne
for i in range(n):
    # Boucle interne pour chaque colonne dans une ligne
    for j in range(n):
        print("*", end=" ")
    print()
```
'''
unit_content3='''
Dans cet exemple, la boucle externe parcourt chaque ligne, et la boucle interne parcourt chaque colonne à l'intérieur de chaque ligne. Le résultat serait :
'''
code_block3='''
```
* * *
* * *
* * *
```
'''
unit_content4='''
Chaque ligne contient trois étoiles, et cela est généré en utilisant des boucles imbriquées pour itérer sur les lignes et les colonnes du motif.
'''
unit_content1Text = tk.Text(mainFrame,height='20')
code_block1Text = tk.Text(mainFrame,height='20')
unit_content2Text = tk.Text(mainFrame,height='20')
code_block2Text = tk.Text(mainFrame,height='20')
unit_content3Text = tk.Text(mainFrame,height='20')
code_block3Text = tk.Text(mainFrame,height='20')
unit_content4Text = tk.Text(mainFrame,height='20')
code_block4Text = tk.Text(mainFrame,height='20')

setTextWidget(unit_content1Text,unit_content1, 'p')
setTextWidget(code_block1Text,code_block1, 'c')
setTextWidget(unit_content2Text,unit_content2, 'p')
setTextWidget(code_block2Text,code_block2, 'c')
setTextWidget(unit_content3Text,unit_content3, 'p')
setTextWidget(code_block3Text,code_block2, 'c')
setTextWidget(unit_content4Text,unit_content3, 'p')


unit_content1Text.pack(fill=tk.X,side=tk.LEFT)
code_block1Text.pack(fill=tk.X,side=tk.LEFT)
unit_content2Text.pack(fill=tk.X,side=tk.LEFT)
code_block2Text.pack(fill=tk.X,side=tk.LEFT)
unit_content3Text.pack(fill=tk.X,side=tk.LEFT)
code_block4Text.pack(fill=tk.X,side=tk.LEFT)
unit_content4Text.pack(fill=tk.X,side=tk.LEFT)

tk.Button(mainFrame,text='Next Page >',).pack(side=tk.RIGHT)#command=nextPage
tk.Button(mainFrame,text='Back to dashboard',).pack(side=tk.RIGHT)#command=back
root.mainloop()