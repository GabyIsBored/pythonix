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

unit_content1='''# Conditions If

## Introduction

Les conditions `if` en Python permettent d'exécuter des blocs de code uniquement si une certaine condition est vraie. Elles sont essentielles pour le contrôle de flux dans un programme.

## Syntaxe de base

La structure de base d'une instruction `if` en Python est la suivante :

'''
code_block1='''
```python
if condition:
    # Bloc de code à exécuter si la condition est vraie
```'''
unit_content2='''
L'indentation (décalage vers la droite) est cruciale en Python pour délimiter le bloc de code à exécuter.

La condition doit toujours renvoyer un booleen (Vrai ou Faux). Les comparaisons (vues dans le chapitre precedent) sont utilisées pour obtenir ce type de résultat. Elles permettent de réaliser une multitude de tests et de vérifications essentiels dans le bon déroulement d'un programme.

## Exemples

### Exemple 1 : Condition simple
'''
code_block2='''
```python
if 20 > 18:
    print("Condition validee")
```'''
unit_content3='''

Puisque 20 > 18 est vraie, le bloc de code contenu sous la condition s’execute, et donc la phrase `‘Condition validee”` s’affiche

### Exemple 2 : Condition simple avec variable

'''
code_block3='''```python
age = 18
if age >= 18:
    print("Vous êtes majeur.")
```
'''
unit_content4='''
Puisque 18 ≥ 18 est vraie, le bloc de code contenu sous la condition s’execute, et donc la phrase `‘Vous êtes majeur.”` s’affiche
'''

unit_content1Text = tk.Text(mainFrame,height='20')
code_block1Text = tk.Text(mainFrame,height='20')
unit_content2Text = tk.Text(mainFrame,height='20')
code_block2Text = tk.Text(mainFrame,height='20')
unit_content3Text = tk.Text(mainFrame,height='20')
code_block3Text = tk.Text(mainFrame,height='20')
unit_content4Text = tk.Text(mainFrame,height='20')
setTextWidget(unit_content1Text,unit_content1, 'p')
setTextWidget(code_block1Text,code_block1, 'c')
setTextWidget(unit_content2Text,unit_content2, 'p')
setTextWidget(code_block2Text,code_block2, 'c')
setTextWidget(unit_content3Text,unit_content3, 'p')
setTextWidget(code_block3Text,code_block3, 'c')
setTextWidget(unit_content4Text,unit_content4, 'p')

unit_content1Text.pack(fill=tk.X,side=tk.LEFT)
code_block1Text.pack(fill=tk.X,side=tk.LEFT)
unit_content2Text.pack(fill=tk.X,side=tk.LEFT)
code_block2Text.pack(fill=tk.X,side=tk.LEFT)
unit_content3Text.pack(fill=tk.X,side=tk.LEFT)
code_block3Text.pack(fill=tk.X,side=tk.LEFT)
unit_content4Text.pack(fill=tk.X,side=tk.LEFT)
tk.Button(mainFrame,text='Next Page >',).pack(side=tk.RIGHT)#command=nextPage
tk.Button(mainFrame,text='Back to dashboard',).pack(side=tk.RIGHT)#command=back

root.mainloop()