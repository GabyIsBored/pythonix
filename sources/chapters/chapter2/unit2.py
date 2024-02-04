# symbol -> meaning
# h1 -> header 1
# h3 -> header 3
# p  -> paragraph
# c  -> code highlighted
# q  -> question -> prompt for answer
# li -> bulleted list
# i  -> indicator
# co -> simulate console output
# ## -> need implementation later
# notation : <symbol>_<representation><occurrence>

# SOUS CHAPITRE: AFFECTATION D'UNE VARIABLE
unit_content = {
    "h1_titre": ["Affectation d'une variable"],
    "h3_stitre1": ["L'opérateur '='"],
    "p_paragraphe1": ["Le symbole ‘=’ permet d’assigner à une variable une certaine \nvaleur :"],
    "c_ex2":["x = 1\n"],
    "li_text1_1":["x étant la variable crée (son ‘nom’)\n"],
    "li_text1_2":["1 étant sa valeur d’initialisation (sa ‘valeur’)\n"],
    "p_paragraphe2": ["On appelle ce symbole un -opérateur-\n et fait partie des opérateurs d’assignation.\n Il existe de nombreux opérateurs, parmi lesquels\n figurent les opérateurs --d’assignations--, \nles opérateurs --arithmétiques--, \nles opérateurs --de comparaison-- etc… Ils seront donc \nintroduits dans un prochain chapitre."],
    "h3_stitre2": ["Autre propriété d’affectation d'une variable"],
    "p_paragraphe3": ["Une variable peut également être initialisée à partir de la \nvaleur stockée dans une autre variable.De cette manière on peut utiliser \nla valeur d’une variable et lui faire subir des modifications sans \nmodifier la variable dont la valeur a été copié."],
    "h3_stitre3": ["Exemple 1"],
    "c_ex2": ["$defaultValue = 50           # defaultValue est initialisé avec 50$\n$testValue = defaultValue    # testValue est initialisé avec defaultValue (50)$\n$testValue = 20              # defaultValue est toujours égale à 50$"],
    "li_text2_1":["Ligne 1: la variable $defaultValue$ est crée, et initialisée avec \nle nombre entier 50."],
    "li_text2_2":["Ligne 2: la variable $testValue$ est crée, et initialisée avec la \nvaleur qui est stockée dans la variable $defaultValue$ , 50 dans ce cas."],
    "li_text2_3":["Ligne 3: la variable $testValue$ subit une modification, sa valeur \nprécédente se fait ‘écraser’ et se  fait remplacer par 20."]
    }