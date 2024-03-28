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
# Boucles: break/continue

Les instructions `break` et `continue` sont utilisées dans les boucles (`for` ou `while`) pour contrôler le flux d'exécution du programme.

### `break` :

L'instruction `break` est utilisée pour sortir immédiatement d'une boucle, quel que soit l'état de la condition de la boucle. Cela permet de terminer prématurément l'exécution de la boucle.

### Exemple avec une boucle `for` :
'''
code_block1='''
```
for i in range(5):
    if i == 3:
        break
    print(i)
```
'''
unit_content2='''
Output :
'''
code_block2='''
```
0
1
2
```
'''
unit_content3='''
Dans cet exemple, la boucle `for` itère de 0 à 4. Lorsque `i` atteint la valeur 3, l'instruction `break` est rencontrée, et la boucle est immédiatement interrompue, sautant les itérations restantes.

### Exemple avec une boucle `while` :
'''
code_block3='''
```
count = 0
while count < 5:
    print(count)
    if count == 2:
        break
    count += 1

```
'''
unit_content4='''
Output :
'''
code_block4='''
```
0
1
2
```
'''
unit_content5='''
Ici, la boucle `while` s'exécute jusqu'à ce que `count` atteigne 5. Lorsque `count` atteint 2, l'instruction `break` est exécutée, interrompant la boucle prématurément.

### `continue` :

L'instruction `continue` est utilisée pour passer à l'itération suivante d'une boucle immédiatement, sautant le reste du bloc de code à l'intérieur de la boucle pour cette itération.

### Exemple avec une boucle `for` :
'''
code_block5='''
```
for i in range(5):
    if i == 2:
        continue
    print(i)
```
'''
unit_content6='''
Output :
'''
code_block6='''
```
0
1
3
4

```
'''
unit_content7='''
Ici, lorsque `i` atteint la valeur 2, l'instruction `continue` est exécutée. Cela provoque le saut du reste du bloc de code à l'intérieur de la boucle pour cette itération, passant immédiatement à l'itération suivante.

### Exemple avec une boucle `while` :
'''
code_block7='''
```
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)
```
'''
unit_content8='''
Output :
'''
code_block8='''
```
1
2
4
5
```
'''
unit_content9='''
Dans cet exemple, lorsque `count` atteint la valeur 3, l'instruction `continue` est exécutée, sautant l'impression de cette valeur et passant à l'itération suivante de la boucle `while`.

REMARQUE: Il est conseilé de n’utiliser ces fonctions que lorsque necessaire, car elle peuvent rendre le code plus compliqué et moins lisible dans la plupart des cas  simplifier le programme afin de ne plus necessiter leurs utilisation
'''
unit_content = [(unit_content1, 'text'), (code_block1, 'code'),
                 (unit_content2, 'text'), (code_block2, 'code'),
                 (unit_content3, 'text'), (code_block3, 'code'),
                 (unit_content4, 'text'), (code_block4, 'code'),
                 (unit_content5, 'text'), (code_block5, 'code')
                (unit_content6, 'text'), (code_block6, 'code'),
                 (unit_content7, 'text'), (code_block7, 'code'),
                 (unit_content8, 'text'), (code_block8, 'code'),
                 (unit_content9, 'text')]
unit_title = 'Boucles: break/continue'