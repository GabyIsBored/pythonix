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
# Boucles: range()

La fonction `range()` en Python est utilisée pour générer une séquence d'entiers. Elle est couramment utilisée avec les boucles, en particulier avec les boucles `for`. Voici une explication détaillée de la fonction `range()` :

### Syntaxe :
'''
code_block1='''
```
range(stop)
range(start, stop)
range(start, stop, step)
```
'''
unit_content2='''
- **`start` (optionnel)** : La valeur de départ de la séquence. Si elle n'est pas spécifiée, elle est par défaut à 0.
- **`stop`** : La valeur de fin de la séquence. Elle est exclusive, ce qui signifie que la séquence s'arrête avant d'atteindre cette valeur.
- **`step` (optionnel)** : L'incrément (pas) entre les valeurs de la séquence. Si non spécifié, il est par défaut à 1.

### Exemples :

1. Utilisation de `range()` avec un seul argument (stop) :
'''
code_block2='''
```
for i in range(5):
    print(i)
```
'''
unit_content3='''
Output :
'''
code_block3='''
```
0
1
2
3
4
```
'''
unit_content4='''
- Utilisation de `range()` avec deux arguments (start, stop) :
'''
code_block4='''
```
for i in range(2, 8):
    print(i)
```
'''
unit_content5='''
Output :
'''
code_block5='''
```
2
3
4
5
6
7
```
'''
unit_content6='''
- Utilisation de `range()` avec trois arguments (start, stop, step) :
'''
code_block6='''
```
for i in range(1, 10, 2):
    print(i)
```
'''
unit_content7='''
Output :
'''
code_block7='''
```
1
3
5
7
9
```
'''
unit_content8='''
### Points clés :

- La fonction `range()` génère une séquence d'entiers, mais ne crée pas réellement une liste. Elle génère les valeurs au fur et à mesure des besoins, ce qui la rend plus efficace en termes de mémoire pour de grandes séquences.
- `start`, `stop`, et `step` peuvent être des entiers.
- Si `step` est négatif, `start` doit être plus grand que `stop`, sinon la séquence sera vide.
- `range()` est souvent utilisée dans les boucles `for` pour itérer sur une séquence d'entiers.

### Utilisation de `range()` avec les boucles `for` :

La fonction `range()` est fréquemment utilisée avec les boucles `for` pour créer des itérations sur une séquence d'entiers. L'objectif est de simplifier le processus d'itération en générant automatiquement une séquence d'entiers pour les valeurs de l'indice dans la boucle. Voici comment cela fonctionne en pratique :

1. **Itération sur une séquence de 0 à n-1 :**
'''
code_block8='''
```
n = 5
for i in range(n):
    print(i)
```
'''
unit_content9='''
Output :
'''
code_block9='''
```
0
1
2
3
4
```
'''
unit_content10='''
Dans cet exemple, la boucle `for` itère sur une séquence générée par `range(n)`, qui va de 0 à n-1. À chaque itération, la variable `i` prend la valeur de l'élément actuel de la séquence.

- **Itération avec une valeur de départ personnalisée :**
'''
code_block10='''
```
start = 2
stop = 8
for i in range(start, stop):
    print(i)
```
'''
unit_content11='''
Output :
'''
code_block11='''
```
2
3
4
5
6
7
```
'''
unit_content12='''
En spécifiant une valeur de départ (`start`) et une valeur de fin (`stop`), la boucle `for` itère sur la séquence générée par `range(start, stop)`.

- **Itération avec un pas personnalisé :**
'''
code_block12='''
```
start = 1
stop = 10
step = 2
for i in range(start, stop, step):
    print(i)


```
'''
unit_content13='''
Output :
'''
code_block13='''
1
3
5
7
9
```
'''
unit_content14='''
En ajoutant un troisième argument, `step`, on peut spécifier un pas personnalisé entre les valeurs de la séquence. Cela permet de sauter certaines valeurs pendant l'itération.

L'utilisation de `range()` avec les boucles `for` simplifie le processus d'itération sur une séquence d'entiers, ce qui est couramment utilisé dans de nombreux scénarios de programmation.
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
code_block5Text = Text(mainFrame,height='20')
unit_content6Text = Text(mainFrame,height='20')
code_block6Text = Text(mainFrame,height='20')
unit_content7Text = Text(mainFrame,height='20')
code_block7Text = Text(mainFrame,height='20')
unit_content8Text = Text(mainFrame,height='20')
code_block8Text = Text(mainFrame,height='20')
unit_content9Text = Text(mainFrame,height='20')
code_block9Text = Text(mainFrame,height='20')
unit_content10Text = Text(mainFrame,height='20')
code_block10Text = Text(mainFrame,height='20')
unit_content11Text = Text(mainFrame,height='20')
code_block11Text = Text(mainFrame,height='20')
unit_content12Text = Text(mainFrame,height='20')
code_block12Text = Text(mainFrame,height='20')
unit_content13Text = Text(mainFrame,height='20')
code_block13Text = Text(mainFrame,height='20')
unit_content14Text = Text(mainFrame,height='20')


setTextWidget(unit_content1Text,unit_content1, 'p')
setTextWidget(code_block1Text,code_block1, 'c')
setTextWidget(unit_content2Text,unit_content2, 'p')
setTextWidget(code_block2Text,code_block2, 'c')
setTextWidget(unit_content3Text,unit_content3, 'p')
setTextWidget(code_block3Text,code_block3, 'c')
setTextWidget(unit_content4Text,unit_content4, 'p')
setTextWidget(code_block4Text,code_block4, 'c')
setTextWidget(unit_content5Text,unit_content5, 'p')
setTextWidget(code_block5Text,code_block5, 'c')
setTextWidget(unit_content6Text,unit_content6, 'p')
setTextWidget(code_block6Text,code_block6, 'c')
setTextWidget(unit_content7Text,unit_content7, 'p')
setTextWidget(code_block7Text,code_block7, 'c')
setTextWidget(unit_content8Text,unit_content8, 'p')
setTextWidget(code_block8Text,code_block8, 'c')
setTextWidget(unit_content9Text,unit_content9, 'p')
setTextWidget(code_block9Text,code_block9, 'c')
setTextWidget(unit_content10Text,unit_content10, 'p')
setTextWidget(code_block10Text,code_block10, 'c')
setTextWidget(unit_content11Text,unit_content11, 'p')
setTextWidget(code_block11Text,code_block11, 'c')
setTextWidget(unit_content12Text,unit_content12, 'p')
setTextWidget(code_block12Text,code_block12, 'c')
setTextWidget(unit_content13Text,unit_content13, 'p')
setTextWidget(code_block13Text,code_block13, 'c')
setTextWidget(unit_content14Text,unit_content14, 'p')


unit_content1Text.pack(fill=X,side=LEFT)
code_block1Text.pack(fill=X,side=LEFT)
unit_content2Text.pack(fill=X,side=LEFT)
code_block2Text.pack(fill=X,side=LEFT)
unit_content3Text.pack(fill=X,side=LEFT)
code_block3Text.pack(fill=X,side=LEFT)
unit_content4Text.pack(fill=X,side=LEFT)
code_block4Text.pack(fill=X,side=LEFT)
unit_content5Text.pack(fill=X,side=LEFT)
code_block5Text.pack(fill=X,side=LEFT)
unit_content6Text.pack(fill=X,side=LEFT)
code_block6Text.pack(fill=X,side=LEFT)
unit_content7Text.pack(fill=X,side=LEFT)
code_block7Text.pack(fill=X,side=LEFT)
unit_content8Text.pack(fill=X,side=LEFT)
code_block8Text.pack(fill=X,side=LEFT)
unit_content9Text.pack(fill=X,side=LEFT)
code_block9Text.pack(fill=X,side=LEFT)
unit_content10Text.pack(fill=X,side=LEFT)
code_block10Text.pack(fill=X,side=LEFT)
unit_content11Text.pack(fill=X,side=LEFT)
code_block11Text.pack(fill=X,side=LEFT)
unit_content12Text.pack(fill=X,side=LEFT)
code_block12Text.pack(fill=X,side=LEFT)
unit_content13Text.pack(fill=X,side=LEFT)
code_block13Text.pack(fill=X,side=LEFT)
unit_content14Text.pack(fill=X,side=LEFT)



Button(mainFrame,text='Next Page >',).pack(side=RIGHT)#command=nextPage
Button(mainFrame,text='Back to dashboard',).pack(side=RIGHT)#command=back

root.mainloop()