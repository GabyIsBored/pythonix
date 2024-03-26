unit_content1:'''
# Declarer un dictionnaire

Un dictionnaire Python est une collection d'éléments non ordonnés. Chaque élément est une paire clé-valeur, où chaque valeur a une clé unique qui nous permet de l’acceder.

Syntaxe : défini avec des accolades **`{}`**, les paires clé-valeur sont séparées par des virgules et les clés et les valeurs par **`:`**:
'''
code_block1:'''
```
mon_dictionnaire = {'clé1': valeur1, 'clé2': valeur2, ...}
```
'''
unit_content2:'''
### **Accès aux Valeurs**

Les valeurs dans un dictionnaire sont accessibles en utilisant la notation d'indexation avec la clé correspondante.
'''
code_block2:'''
```
eleves = {'premier': 'Jean', 'second': 'Paul', 'troisieme': 'Lea'}
secondEleve= eleves['second']
print(secondEleve) # Affiche 'Lea'
```
'''
unit_content3:'''
### **Modification des Valeurs**

Les valeurs dans un dictionnaire peuvent être modifiées en accédant à la clé et en lui attribuant une nouvelle valeur.
'''
code_block3:'''
```
eleves = {'premier': 'Jean', 'second': 'Paul', 'troisieme': 'Lea'}
eleves['second'] = 'Elias'
print(secondEleve) # Affiche 'Elias'
```
'''
unit_content4:'''
### **Ajout et Suppression d'Éléments**

Vous pouvez ajouter de nouvelles paires clé-valeur à un dictionnaire en assignant une valeur à une nouvelle clé. De même, vous pouvez supprimer des éléments en utilisant l'instruction **`del`** ou la méthode **`pop()`**.
'''
code_block4:'''
```
eleves = {'premier': Jean, 'second': Paul, 'troisieme': 'Lea'}
del mon_dictionnaire["troisieme"]
valeur_supprimée = eleves.pop("second")
print(eleves) # Affiche {'premier': 'Jean'}
print(valeur_supprimée) # Affiche 'Lea'
```
'''
unit_content5:'''
### **Parcours**

Vous pouvez parcourir un dictionnaire à l'aide de boucles **`for`**, généralement en itérant sur les clés, les valeurs ou les items (paires clé-valeur).
'''
code_block5:'''
```
for clé in mon_dictionnaire:
    print(clé, "->", mon_dictionnaire[clé])

for valeur in mon_dictionnaire.values():
    print(valeur)

for clé, valeur in mon_dictionnaire.items():
    print(clé, "->", valeur)
```
'''