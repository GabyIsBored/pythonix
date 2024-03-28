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

unit_content1='''# Indentation

Python n’est pas seulement sensible sur l’ortographe, mais aussi l’indentation des lignes: 

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
unit_content = [(unit_content1, 'text'), (code_block1, 'code'),
                 (unit_content2, 'text')]
unit_title = 'Intendation'
