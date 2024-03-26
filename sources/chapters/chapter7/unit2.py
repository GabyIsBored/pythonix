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


unit_content1='''
# Parametres et la fonction return
Paramètres positionnels : Ce sont les paramètres les plus courants. Vous les utilisez en spécifiant les valeurs dans l'ordre où les paramètres sont définis dans la fonction.
Exemple :
'''
code_block1='''
```
def addition(a, b):
    return a + b
result = addition(3, 5)  # a = 3, b = 5
```
'''
unit_content2='''
**Définition de la fonction :**

- **`def addition(a, b):`** : Cette ligne crée une fonction appelée **`addition`** qui prend deux nombres comme entrées (**`a`** et **`b`**).

**Appel de la fonction :**

- **`result = addition(3, 5)`** : Cette ligne appelle la fonction **`addition`** avec les nombres **`3`** et **`5`** comme arguments.

**Calcul dans la fonction :**

- Dans la fonction **`addition`**, **`a`** est **`3`** et **`b`** est **`5`**.
- La fonction ajoute ces deux nombres ensemble : **`3 + 5`**, ce qui donne **`8`**.

**Affectation du résultat :**

- Le résultat de l'addition, **`8`**, est stocké dans la variable **`result`**.

**Paramètres par mots-clés :** Vous pouvez spécifier le nom des paramètres lors de l'appel de la fonction. Cela vous permet de ne pas vous soucier de l'ordre des paramètres.
2. **Paramètres par mots-clés :** Vous pouvez spécifier le nom des paramètres lors de l'appel de la fonction. Cela vous permet de ne pas vous soucier de l'ordre des paramètres.
    
    Exemple :
'''
code_block2='''
```
def addition(a, b):
    return a + b

result = addition(b=5, a=3)  # a = 3, b = 5 (ordre différent)
```
'''
unit_content3='''
3. **Paramètres par défaut :** Vous pouvez définir des valeurs par défaut pour les paramètres de fonction. Si vous n'en fournissez pas lors de l'appel de la fonction, les valeurs par défaut sont utilisées.
    
    Exemple :
'''
code_block3='''
```
def saluer(nom='Mon ami'):
    return 'Bonjour, ' + nom

print(saluer())  # "Bonjour, Mon ami"
print(saluer('Alice'))  # "Bonjour, Alice"
```
'''
unit_content4='''
4. **Paramètres variables :** Vous pouvez accepter un nombre variable d'arguments en utilisant **`args`** pour les positionnels et **`*kwargs`** pour les arguments par mots-clés.
    
    Exemple :
'''
code_block4='''
```
def fonction_var_pos(*args):
    for arg in args:
        print(arg)

fonction_var_pos(1, 2, 3, 4)

def fonction_var_kw(**kwargs):
    for cle, valeur in kwargs.items():
        print(f"{cle}: {valeur}")

fonction_var_kw(a=1, b=2, c=3)
```
'''
unit_content5='''
En utilisant ces différentes techniques, vous pouvez rendre vos fonctions plus flexibles et plus faciles à utiliser dans différentes situations.
'''

unit_content1Text = Text(mainFrame,height='20')
code_block1Text = Text(mainFrame,height='20')
unit_content2Text = Text(mainFrame,height='20')
code_block2Text = Text(mainFrame,height='20')
unit_content3Text = Text(mainFrame,height='20')
code_block3Text = Text(mainFrame,height='20')
unit_content4Text = Text(mainFrame,height='20')
code_block4Text = Text(mainFrame,height='20')
unit_content5Text = Text(mainFrame,height='20')
setTextWidget(unit_content1Text,unit_content1, 'p')
setTextWidget(code_block1Text,code_block1, 'c')
setTextWidget(unit_content2Text,unit_content2, 'p')
setTextWidget(code_block2Text,code_block2, 'c')
setTextWidget(unit_content3Text,unit_content3, 'p')
setTextWidget(code_block3Text,code_block3, 'c')
setTextWidget(unit_content4Text,unit_content4, 'p')
setTextWidget(code_block4Text,code_block4, 'c')
setTextWidget(unit_content5Text,unit_content5, 'p')
unit_content1Text.pack(fill=X,side=LEFT)
code_block1Text.pack(fill=X,side=LEFT)
unit_content2Text.pack(fill=X,side=LEFT)
code_block2Text.pack(fill=X,side=LEFT)
unit_content3Text.pack(fill=X,side=LEFT)
code_block3Text.pack(fill=X,side=LEFT)
unit_content4Text.pack(fill=X,side=LEFT)
code_block4Text.pack(fill=X,side=LEFT)
unit_content5Text.pack(fill=X,side=LEFT)

Button(mainFrame,text='Next Page >',).pack(side=RIGHT)#command=nextPage
Button(mainFrame,text='Back to dashboard',).pack(side=RIGHT)#command=back

root.mainloop()