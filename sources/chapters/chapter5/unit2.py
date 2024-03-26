unit_content1:'''
# Listes

Une liste est une structure de données qui permet de stocker une collection ordonnée d'éléments.

Pour déclarer une liste en Python, vous pouvez utiliser les crochets `[]` et séparer les éléments de la liste par des virgules. Voici quelques exemples de déclaration de listes :

- Liste vide : `ma_liste_vide = []`
- Liste avec des éléments : `fruits = ['pomme', 'banane', 'orange']`
- Liste avec différents types de données :`mixte = [1, 'deux', 3.0, True]`

On peut aussi faire des listes contenant des listes, nommées matrices, ou liste multidimensionnelle:

`matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`

Et enfin on peux utiliser la fonction `list()` afin d’arranger des éléments dans une listes de façon dynamique:`jours_semaine = list(('lundi', 'mardi', 'mercredi','jeudi', 'vendredi'))`

### Indexation des éléments :

Pour faire reference a un element particulier de la liste, on mets :
'''
code_block1:'''
```
element = liste[indice]
```
'''
unit_content2:'''
Un indice est un un nombre entier utilisé pour identifier un élément en indiquant la position relative de l'élément à l'intérieur de la séquence.

En Python, les indices commencent généralement à 0. Ainsi, le premier élément d'une séquence a l'indice 0, le deuxième a l'indice 1, et ainsi de suite. Vous pouvez également utiliser des indices négatifs pour accéder aux éléments depuis la fin de la séquence, où -1 représente le dernier élément, -2 le deuxième en partant de la fin, et ainsi de suite.
'''
code_block2:'''
```
premier_element = liste[0]  # Accès au premier élément
dernier_element = liste[-1]  # Accès au dernier élément
```
'''
unit_content3:'''
### Modification des éléments :

Vous pouvez modifier les éléments d'une liste en utilisant leur indice.
'''
code_block3:'''
```
fruits = ['pomme', 'banane', 'orange']
fruits[1] = 'kiwi'
print(fruits)  # Affiche ['pomme', 'kiwi', 'orange']
```
'''

unit_content4:'''
### Ajout d'éléments :

Vous pouvez ajouter des éléments à une liste en utilisant la méthode `append()` ou avec l'opérateur
'''
code_block4:'''
```
fruits = ['pomme', 'banane', 'orange']

fruits.append('fraise')
print(fruits)  # Affiche ['pomme', 'banane', 'orange', 'fraise']

legumes = ['carotte', 'brocoli']
nourriture = fruits + legumes
print(nourriture)  # Affiche ['pomme', 'banane', 'orange', 'fraise', 'carotte', 'brocoli']
```
'''
unit_content5:'''
# Methodes

Voici quelques methodes qui nous permettent de manipuler les listes:

- La fonction `len()` renvoie la longueur d'une liste, c'est-à-dire le nombre d'éléments qu'elle contient.
'''
code_block5:'''
```
fruits = ['pomme', 'banane', 'orange']

nombre_elements = len(fruits)
print(nombre_elements)  # Affiche 3
```
'''
unit_content6:'''
extend(iterable) : Ajoute tous les éléments d'un itérable (tel qu'une autre liste) à la fin de la liste.
'''
code_block6:'''
```
my_list = [1, 2, 3]
other_list = [4, 5, 6]
my_list.extend(other_list)
print(my_list)  # Affichage : [1, 2, 3, 4, 5, 6]


```
'''
unit_content7:'''
insert(index, item) : Insère un élément à un index spécifié.
'''
code_block7:'''
```
my_list = [1, 2, 3]
my_list.insert(1, 10)
print(my_list)  # Affichage : [1, 10, 2, 3]


```
'''
unit_content8:'''
remove(item) : Supprime la première occurrence d'un élément spécifié dans la liste.
'''
code_block8:'''
```
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Affichage : [1, 3, 2]


```
'''
unit_content9:'''
pop([index]) : Supprime et retourne l'élément à l'index spécifié. Si aucun index n'est spécifié, supprime et retourne le dernier élément de la liste.
'''
code_block9:'''
```
my_list = [1, 2, 3]
popped_item = my_list.pop()
print(popped_item)  # Affichage : 3
print(my_list)      # Affichage : [1, 2]


```
'''
unit_content10:'''
index(item) : Retourne l'index de la première occurrence d'un élément spécifié dans la liste.
'''
code_block10:'''
```
my_list = [1, 2, 3, 2]
index = my_list.index(2)
print(index)  # Affichage : 1

```
'''
unit_content11:'''
count(item) : Retourne le nombre d'occurrences d'un élément spécifié dans la liste.
'''
code_block11:'''
```
my_list = [1, 2, 3, 2]
count = my_list.count(2)
print(count)  # Affichage : 2


```
'''
unit_content12:'''
sort(key=None, reverse=False) : Trie les éléments de la liste. Le paramètre key permet un tri personnalisé basé sur une fonction, et le paramètre reverse spécifie s'il faut trier par ordre décroissant.
'''
code_block12:'''
```
my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # Affichage : [1, 2, 3]

# Avec reverse=True
my_list.sort(reverse=True)
print(my_list)  # Affichage : [3, 2, 1]


```
'''
unit_content13:'''
reverse() : Inverse l'ordre des éléments dans la liste.
'''
code_block13:'''
```
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Affichage : [3, 2, 1]


```
'''
unit_content14:'''
clear() : Supprime tous les éléments de la liste.
'''
code_block14:'''
```
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Affichage : []


```
'''