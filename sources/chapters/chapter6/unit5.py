<<<<<<< HEAD
unit_content='''# Comparaisons

Python est capable d'effectuer toute une série de comparaisons entre le contenu de deux variables,

en renvoyant un **booleen** `True` ou `False` si la comparaisons est verifiee ou pas.

### Egalite et inegalites

Pour tester l’égalité de contenu entre deux valeurs, on utilise l’operateur `==` :

`>>> 2 == 3`  

`>>> False` 

`>>> 3 == 3`  

`>>> True`    

Pour tester l’inégalité de contenu entre deux valeurs, on utilise l’operateur `!=` :

`>>> 2 != 3`  

`>>> False` 

### **Infériorité et supériorité, stricts ou larges**

Pour savoir si un objet est:

- **Strictement inférieur/superieur** à un autre, on utilise les operateurs `<` et `>` respectivement
- **Inférieur ou egal/superieur ou egal** à un autre, on utilise les operateurs `<=` et `>=` respectivement

`>>> 120 > 5` 

`>>> False`      

`>>> 3 <= 3`     

`>>> True`      

### Exercice

x=250, y=120. Faire un programme qui donne `True, True, False` avec les operateurs `==, <, >=`'''
=======
unit_content1:'''
# Boucles imbriquees

Les boucles imbriquées en Python sont des boucles placées à l'intérieur d'une autre boucle. Cela signifie qu'il y a une boucle principale (extérieure) et une ou plusieurs boucles secondaires (intérieures) à l'intérieur de celle-ci. Les boucles imbriquées sont souvent utilisées pour parcourir et manipuler des structures de données bidimensionnelles, comme des listes de listes, des matrices ou des tableaux.

La structure générale d'un ensemble de boucles imbriquées ressemble à ceci :
'''
code_block1:'''
```
for variable_externe in sequence_externe:
    # Instructions de la boucle externe

    for variable_interne in sequence_interne:
        # Instructions de la boucle interne

```
'''
unit_content2:'''
Là où `sequence_externe` est la séquence parcourue par la boucle externe, et `sequence_interne` est la séquence parcourue par la boucle interne.

## Exemple
'''
code_block2:'''
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
unit_content3:'''
Dans cet exemple, la boucle externe parcourt chaque ligne, et la boucle interne parcourt chaque colonne à l'intérieur de chaque ligne. Le résultat serait :
'''
code_block3:'''
```
* * *
* * *
* * *
```
'''
unit_content4:'''
Chaque ligne contient trois étoiles, et cela est généré en utilisant des boucles imbriquées pour itérer sur les lignes et les colonnes du motif.
'''
>>>>>>> 5e4795ad3db8bd44e219213fe62ebf5e5b4ef899
