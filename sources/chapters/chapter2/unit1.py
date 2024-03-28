unit_content1='''# Variables

### Introduction aux variables

En programmation, une variable est un espace de stockage qui porte **un nom**, et a **une valeur.** 

Cette valeur peut etre un nombre fit un int, ou une chaine de caractere dite une string, qu’on mets entre guillemets 

Une variable peut être représentée comme un tiroir portant une étiquette dans lequel on peut ranger des données. Les variables permettent de conserver et de manipuler des données au cours de l’exécution d’un programme.

### Exemple 1
'''
code_block1='''
python
nom = “John”
age = 32
'''
unit_content2='''

Dans ce block de code, le tiroir **nom** a pour valeur “John” et le tiroir **âge** a pour valeur 32.

Dans cet exemple, on utilise des guillemets pour indiquer que **John** n’est pas une variable mais bien du texte, aussi appelé chaîne de caractères en programmation.

### Exemple 2

Maintenant qu’on a nos variables, on peut les afficher à l’aide de la fonction **print()**

- **print** est le nom de la fonction que l’on va *appeler*
- **print** est une fonction *native* qui permet d’afficher dans la console les *arguments* qui ont été passés
- ce qu’il y a à l’intérieur des () correspond aux *paramètres* (ou *arguments*) de la fonction **print**.
'''
code_block2='''
python
nom = “John”
print(nom)
'''
unit_content3='''
Après l’exécution de ce programme, on voit dans la console le contenu (les données) stockées dans la variable nom.

Nommer des variables
Quand on crée une variable, il est important que son nom corresponde à son usage ou à sa fonction dans le programme
Le nom d’une variable ne peut pas contenir d’espace
Le nom d’une variable ne peut pas être un nombre
Crée deux variables ayant le même nom résultera en une erreur
Il est préférable d’éviter les noms de variables trop long
Il est préférable de ne pas utiliser d’accent dans le nom d’une variable

La casse significative
La notion de "casse significative" se réfère à l'utilisation intentionnelle de majuscules ou de minuscules dans les noms de variables pour transmettre des informations sur leur rôle ou leur nature. En spécifiant une seule casse significative vous améliorez la lisibilité de votre code et facilitez la compréhension des variables par d'autres développeurs.

La casse significative contribue ainsi à rendre le code plus clair et cohérent.

Vous pouvez retenir ces deux conventions courantes :

La camelCase
  Les mots commencent par des majuscules, sauf le premier.
  Exemple : nomDeVariable

La snake_case
  Les mots sont séparés par des underscores (tirets du 8) et sont généralement en minuscules.
Exemple : nom_de_variable'''

unit_content = [(unit_content1, 'text'), (code_block1, 'code'),
                 (unit_content2, 'text'), (code_block2, 'code'),
                   (unit_content3, 'text')]
unit_title = 'Variables'

import chapters.chapter2.quiz1 as nextFrame
from markdown import setTextWidget
import tkinter as tk
class Content(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__()
        self.root = master
        for block in unit_content:
            self.widget=tk.Text(master)
            setTextWidget(self.widget,block[0],block[1]) 
            self.widget.pack()   
        continuerImg=tk.PhotoImage(file='sources\assets\ElementDivers\continuer.png')
        self.nextButton = tk.Button(master,image=continuerImg,command=nextPage)
        def nextPage():
            nextFrame.Content(master)