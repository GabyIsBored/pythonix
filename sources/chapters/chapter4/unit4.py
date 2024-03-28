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

unit_content1='''# Conditions imbriquees

Les conditions imbriquées, également appelées structures conditionnelles imbriquées, se produisent lorsque vous placez une structure conditionnelle à l'intérieur d'une autre. Cela permet de gérer des scénarios plus complexes en évaluant plusieurs conditions de manière hiérarchique. Voici un exemple d'utilisation de conditions imbriquées en Python :
'''
code_block1='''
```python
age = 25
sexe = "homme"

if age >= 18:
    print("Vous êtes majeur.")

    if sexe == "homme":
        print("Bienvenue, Monsieur!")
    else:
        print("Bienvenue, Madame!")

else:
    print("Vous êtes mineur.")
```
'''
unit_content2='''
Explication :
Explications :

1. La première condition (`if age >= 18:`) vérifie si l'âge est supérieur ou égal à 18.
    - Si cette condition est vraie, le bloc de code indenté sous cet `if` est exécuté.
    - À l'intérieur de ce bloc, une autre condition est évaluée.
2. La deuxième condition (`if sexe == "homme":`) vérifie si le sexe est égal à "homme".
    - Si cette condition est vraie, le bloc de code indenté sous cette deuxième `if` est exécuté et affiche "Bienvenue, Monsieur!".
    - Si la condition est fausse, le bloc de code indenté sous le `else` de la deuxième `if` est exécuté, affichant "Bienvenue, Madame!".
3. Si la première condition (`if age >= 18:`) est fausse, le bloc de code indenté sous le `else` de la première `if` est exécuté, affichant "Vous êtes mineur.".'''

unit_content = [(unit_content1, 'text'), (code_block1, 'code'),
                 (unit_content2, 'text')]
unit_title = 'Conditions imbriquees'

root.mainloop()
