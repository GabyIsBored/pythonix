unit_content1:'''
# Boucles: break/continue

Les instructions `break` et `continue` sont utilisées dans les boucles (`for` ou `while`) pour contrôler le flux d'exécution du programme.

### `break` :

L'instruction `break` est utilisée pour sortir immédiatement d'une boucle, quel que soit l'état de la condition de la boucle. Cela permet de terminer prématurément l'exécution de la boucle.

### Exemple avec une boucle `for` :
'''
code_block1:'''
```
for i in range(5):
    if i == 3:
        break
    print(i)
```
'''
unit_content2:'''
Output :
'''
code_block2:'''
```
0
1
2
```
'''
unit_content3:'''
Dans cet exemple, la boucle `for` itère de 0 à 4. Lorsque `i` atteint la valeur 3, l'instruction `break` est rencontrée, et la boucle est immédiatement interrompue, sautant les itérations restantes.

### Exemple avec une boucle `while` :
'''
code_block3:'''
```
count = 0
while count < 5:
    print(count)
    if count == 2:
        break
    count += 1

```
'''
unit_content4:'''
Output :
'''
code_block4:'''
```
0
1
2
```
'''
unit_content5:'''
Ici, la boucle `while` s'exécute jusqu'à ce que `count` atteigne 5. Lorsque `count` atteint 2, l'instruction `break` est exécutée, interrompant la boucle prématurément.

### `continue` :

L'instruction `continue` est utilisée pour passer à l'itération suivante d'une boucle immédiatement, sautant le reste du bloc de code à l'intérieur de la boucle pour cette itération.

### Exemple avec une boucle `for` :
'''
code_block5:'''
```
for i in range(5):
    if i == 2:
        continue
    print(i)
```
'''
unit_content6:'''
Output :
'''
code_block6:'''
```
0
1
3
4

```
'''
unit_content7:'''
Ici, lorsque `i` atteint la valeur 2, l'instruction `continue` est exécutée. Cela provoque le saut du reste du bloc de code à l'intérieur de la boucle pour cette itération, passant immédiatement à l'itération suivante.

### Exemple avec une boucle `while` :
'''
code_block7:'''
```
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)
```
'''
unit_content8:'''
Output :
'''
code_block8:'''
```
1
2
4
5
```
'''
unit_content9:'''
Dans cet exemple, lorsque `count` atteint la valeur 3, l'instruction `continue` est exécutée, sautant l'impression de cette valeur et passant à l'itération suivante de la boucle `while`.

REMARQUE: Il est conseilé de n’utiliser ces fonctions que lorsque necessaire, car elle peuvent rendre le code plus compliqué et moins lisible dans la plupart des cas  simplifier le programme afin de ne plus necessiter leurs utilisation
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
Button(mainFrame,text='Next Page >',).pack(side=RIGHT)#command=nextPage
Button(mainFrame,text='Back to dashboard',).pack(side=RIGHT)#command=back
root.mainloop()