unit_content='''
# Variables

### Introduction aux variables

En programmation, une variable est un espace de stockage qui porte **un nom**, et a **une valeur.** 

Une variable peut être représentée comme un tiroir portant une étiquette dans lequel on peut ranger des données. Les variables permettent de conserver et de manipuler des données au cours de l’exécution d’un programme.

### Exemple 1

1`nom = “John”`

2`age = 32`

Dans ce block de code, le tiroir **nom** a pour valeur “John” et le tiroir **âge** a pour valeur 32.

Dans cet exemple, on utilise des guillemets pour indiquer que **John** n’est pas une variable mais bien du texte, aussi appelé chaîne de caractères en programmation.

### Exemple 2

1`John = “Wick”`

2`nom = John`

D’après vous, quelle est la valeur stockée dans la variable **nom ?**

_____  <vérifier>

### Exemple 3

Maintenant qu’on a nos variables, on peut les afficher à l’aide de la fonction **print()**

- **print** est le nom de la fonction que l’on va *appeler*
- **print** est une fonction *native* qui permet d’afficher dans la console les *arguments* qui ont été passés
- ce qu’il y a à l’intérieur des () correspond aux *paramètres* (ou *arguments*) de la fonction **print**.

1`age = 32`

2`John = “Wick”`

3`nom = “John”`

4`nom = John`

5`print(nom)`

Lorsque on exécute ce programme, on reçois une erreur.

D’après vous, quelle ligne de code (le nombre à gauche) à causé cette erreur ?

_____  <vérifier> (quand la bonne réponse est trouvée, ca ouvre ce qui suis)

Maintenant que vous avez trouvé l’erreur, le code devrai ressembler à ça :

1`age = 32`

2`John = “Wick”`

3`nom = “John”`

4`print(nom)`

Après l’exécution de ce programme, on voit dans la console le contenu (les données) stockées dans la variable **nom.**

>>>python [programme.py](http://programme.py)    <i>

John

### Nommer des variables

- Quand on crée une variable, il est important que son nom corresponde à son usage ou à sa fonction dans le programme    <i>
- Le nom d’une variable ne peut pas contenir d’espace    <i>
- Le nom d’une variable ne peut pas être un nombre    <i>
- Crée deux variables ayant le même nom résultera en une erreur    <i>
- Pour des raisons de compréhension, il est préférable de favoriser des noms en anglais    <i>
- Il est préférable d’éviter les noms de variables trop long    <i>
- Il est préférable de ne pas utiliser d’accent dans le nom d’une variable    <i>
- L’utilisation de la “casse significative” :

### La casse significative

La notion de "casse significative" se réfère à l'utilisation intentionnelle de majuscules ou de minuscules dans les noms de variables pour transmettre des informations sur leur rôle ou leur nature. En spécifiant une seule casse significative vous améliorez la lisibilité de votre code et facilitez la compréhension des variables par d'autres développeurs.

**La casse significative contribue ainsi à rendre le code plus clair et cohérent.**

Vous pouvez retenir ces deux conventions courantes :

- La **camelCase**
    
    Les mots commencent par des majuscules, sauf le premier.
    
    Exemple : nomDeVariable
    

- La **snake_case**
    
    Les mots sont séparés par des underscores (tirets du 8) et sont généralement en minuscules.
    
    Exemple : nom_de_variable
    

### Exercice n°1

Consigne : 

### Exercice n°2

Consigne :

'''