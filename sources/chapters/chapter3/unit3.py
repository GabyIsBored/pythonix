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

unit_content1='''# Operateurs 3: Operateurs d’assignation

### **Opérations d'affectation**

Dans **Operateurs 2** on a vu comment stocker des resultats dans des variables, et comment performer des operations sur celles ci
Par consequences, on peut stocker les resultats des operations que l’on performe dans une variable **dans la meme variable:**
'''
code_block1='''
x=1

x=x+1

print(x)
'''
unit_content2='''
Dans cette exemple, on obtient 2, car `x = 1`, donc on subsititue x par 1 dans  `x = x + 1` ce qui nous donne `x = 1 + 1 = 2`

Un autre exemple:'''
code_block2='''

a = 3

a = a * (2 + a)

print(a)
'''
unit_content3='''
Le programme affiche 15 car en substituant a pour 3, on obtient `a = 3 * (2 + 3) = 3 * 5 = 15`

### **Opérateurs d'affectation**

Ce type d’operations est utilise tres frequemment dans Python afin de mettre a jour des variables, au point que Python comporte un operateurs dit **d’assignations** pour chaque une des 7 operations basiques qui permettent **d’effectuer l’operation sur la variable qu’on assigne sans avoir a la referencier 2 fois:**
'''
code_block3='''
x = 1

x += 1

print(x)
'''
unit_content4='''
Ce programme effectue la meme operation que l’**Exemple 1.**

L’operateur `+=` est l’operateur d’assignation qui permet d’ajouter une valeur a la valeur stockee dans la variable.

Le reste des operateurs d’assignations sont:

`-=`: **Soustrait** une valeur a la valeur stockee dans la variable.

`*=`: **Multiplie** une valeur par la valeur stockee dans la variable.

`/=`: **Divise** une valeur par la valeur stockee dans la variable.

`//=`: Obtient le **quotient** de la division une d’valeur par la valeur stockee dans la variable.

`%=`: Obtient le **reste** de la division d’une valeur par la valeur stockee dans la variable.

`**=`: Mets la valeur stockee dans la variable **a la puissance** d’une valeur'''
unit_content = [(unit_content1, 'text'), (code_block1, 'code'),
                 (unit_content2, 'text'), (code_block2, 'code'),
                 (unit_content3, 'text'), (code_block3, 'code'),
                 (unit_content4, 'text'), (code_block4, 'code')]
unit_title = "Operateurs 3 (operateurs d'assignations)"
