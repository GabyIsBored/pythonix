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

# SOUS CHAPITRE: VARIABLES

unit_content = {
    "h1_mainTitle": ["Variables"],
    "h3_subTitle1": ["Introduction aux variables"],
    "p_text1": [
        "En programmation, une variable est un espace de stockage qui porte **un nom**, et a **une valeur.**",
        "Une variable peut être représentée comme un tiroir portant une étiquette dans lequel on peut ranger des données. Les variables permettent de conserver et de manipuler des données au cours de l’exécution d’un programme."
    ],
    "h3_subExemple1": ["Exemple 1"],
    "c_snippet1": ["`nom = “John”`", "`age = 32`"],
    "p_text2": ["Dans ce block de code, le tiroir nom a pour valeur “John” et le tiroir age a pour valeur 32.", "Dans cet exemple, on utilise des guillemets pour indiquer que John n’est pas une variable mais bien du texte, aussi appelé chaîne de caractères en programmation."],
    "h3_subExemple1": ["Exemple 2"],
    "c_snippet2": ["`John = “Wick”`", "`nom = John`"],
    "q_text1": ["D’après vous, quelle est la valeur stockée dans la variable nom?"],
    ## ____ <check results>
    "h3_subExemple3": ["Exemple 3"],
    "p_text3": ["Maintenant qu’on a nos variables, on peut les afficher à l’aide de la fonction print()"],
    "li_text1_1": ["print est le nom de la fonction que l’on va appeler"],
    "li_text1_2": ["print est une fonction native qui permet d’afficher dans la console les arguments qui ont été passés"],
    "li_text1_3": ["ce qu’il y a à l’intérieur des () correspond aux paramètres (ou arguments) de la fonction print."],
    "c_snippet3": ["`age = 32`", "`John = “Wick”`", "`nom = “John”`", "`nom = John`", "`print(nom)`"],
    "q_text": ["Lorsque on execute ce programme, on reçois une erreur.", "D’après vous, quelle ligne de code (le nombre à gauche) à causé cette erreur?"],
    "i_text1": ["(quand la bonne réponse est trouvée, ca ouvre ce qui suis)"],
    ## ____ <check results> + i_text1
    # if result matches input field -> unlock p_text4
    "p_text4": ["Maintenant que vous avez trouvé l’erreur, le code devrai ressembler à ça :"],
    "c_snippet4": ["`age = 32`", "`John = “Wick”`", "`nom = “John”`", "`print(nom)`"],
    "p_text5": ["Après l’exécution de ce programme, on voit dans la console le contenu (les données) stockées dans la variable nom."],
    "co_text1": [">>>python programme.py", "John"],
    "h3_subTitle2": ["Nommer des variables"],
    "li_text2_1": ["Quand on crée une variable, il est important que son nom corresponde à son usage ou à sa fonction dans le programme"],
    "li_text2_2": ["Le nom d’une variable ne peut pas contenir d’espace"],
    "li_text2_3": ["Le nom d’une variable ne peut pas être un nombre"],
    "li_text2_4": ["Crée deux variables ayant le même nom résultera en une erreur"],
    "li_text2_5": ["Pour des raisons de compréhension, il est préférable de favoriser des noms en anglais"],
    "li_text2_6": ["Il est préférable d’éviter les noms de variables trop long"],
    "li_text2_7": ["Il est préférable de ne pas utiliser d’accent dans le nom d’une variable"],
    "li_text2_8": ["L’utilisation de la “casse significative” :"],
    "h3_subTitle3": ["La casse significative"],
    "p_text6": ["La notion de \"casse significative\" se réfère à l'utilisation intentionnelle de majuscules ou de minuscules dans les noms de variables pour transmettre des informations sur leur rôle ou leur nature. En spécifiant une seule casse significative vous améliorez la lisibilité de votre code et facilitez la compréhension des variables par d'autres développeurs.", "**La casse significative contribue ainsi à rendre le code plus clair et cohérent.**\n\n Vous pouvez retenir ces deux conventions courantes :"],
    "li_text3_1": ["La camelCase"],
    "p_text7": ["Les mots commencent par des majuscules, sauf le premier. Exemple : nomDeVariable"],
    "li_text3_2": ["La snake_case"],
    "p_text8": ["Les mots sont séparés par des underscores (tirets du 8) et sont généralement en minuscules. Exemple : nom_de_variable"],
}