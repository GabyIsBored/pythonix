import tkinter as tk
import ttkbootstrap as tb

root = tk.Tk()
root.title('Chapter')
root.geometry('1280x720')
root.resizable(False, False)

font = ('Yu Gothic Ui Light', 12)
titleFont = ('Yu Gothic Ui Bold', 24)
titleFont2 = ('Yu Gothic Ui Bold', 12)

h1Font = ('Yu Gothic Ui', 34, "bold")
h3Font = ('Yu Gothic Ui', 18, "bold")
p_Font = ('Yu Gothic Ui', 16)

def changePage(currentFrame, nextFrame):
    nextFrame.pack(expand=True, fill='both',pady='10',padx='10')
    currentFrame.pack_forget()

# MAINFRAME
mainFrame = tb.Frame(root)
a_frame = tk.Frame(root)  # 2. Affectation d'un variable

button1 = tb.Button(mainFrame, text="Unit 2 : affectation d'une variable",command=lambda: changePage(mainFrame, a_frame))
button1.pack(pady=25)

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

#------------variables--------------------
a_p1 = tk.StringVar(value="Le symbole ‘=’ permet d’assigner à une variable une certaine \nvaleur :$x = 1$- x étant la variable crée (son ‘nom’)- 1 étant sa valeur \nd’initialisation (sa ‘valeur’). On appelle ce symbole un -opérateur-\n et fait partie des opérateurs d’assignation.\n Il existe de nombreux opérateurs, parmis lequels\n figurent les opérateurs --d’assignations--, \nles opérateurs --arithmétiques--, \nles opérateurs --de comparaison-- etc… Ils seront donc \nintroduits dans un prochain chapitre.")
a_p2 = tk.StringVar(value="Une variable peut également être initialisée à partir de la \nvaleur stockée dans une autre variable.De cette manière on peut utiliser \nla valeur d’une variable et lui faire subir des modifications sans \nmodifier la variable dont la valeur a été copié.")
a_p3 = tk.StringVar(value="$defaultValue = 50           # defaultVaue est initialisé avec 50$\n$testValue = defaultValue    # testValue est initialisé avec defaultValue (50)$\n$testValue = 20              # defaultValue est toujours égale à 50$")

a_frame.columnconfigure(0,weight=1) 
a_frame.columnconfigure(1,weight=1) 
a_frame.rowconfigure(0,weight=1) 
a_frame.rowconfigure(1,weight=10) 

coursFrame = tk.Frame(a_frame, bg='#D9D9D9')
exampleFrame = tk.Frame(a_frame, bg='#D9D9D9')

coursFrame.grid(row=1,column=0,sticky='nsew',padx='10',pady='10')
exampleFrame.grid(row=1,column=1,sticky='nsew',padx='10',pady='10')

# Cours
a_content = {
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

h1_titre = tb.Label(a_frame, text = a_content['h1_titre'], font=h1Font,background='#D9D9D9')
h1_titre.grid(row=0,column=0,columnspan=2,sticky='nsew')

h3_stitre1 = tb.Label(coursFrame, text="L'opérateur '='", font=h3Font,background='#D9D9D9')
h3_stitre1.pack(fill='x')

p_paragraphe1 = tb.Label(coursFrame, text=a_p1.get(), 
                         font=p_Font,background='#D9D9D9')
p_paragraphe1.pack(fill='x')

h3_stitre2 = tb.Label(coursFrame, text="Autre propriété d’affectation", font=h3Font,background='#D9D9D9')
h3_stitre2.pack(fill='x')

p_paragraphe3 = tb.Label(coursFrame, text=a_p2.get(), 
                         font=p_Font,background='#D9D9D9')
p_paragraphe3.pack(fill='x')
# Exercices
h3_stitre3 = tb.Label(coursFrame, text="Exemple 1", font=h3Font,background='#D9D9D9')
h3_stitre3.pack(fill='x')
c_ex2=tb.Label(coursFrame, text=a_p3.get(), font=h3Font,background='#D9D9D9')
c_ex2.pack(fill='x')


mainFrame.pack(expand=True, fill='both')

coursFrame.configure(bg='#D9D9D9')
exampleFrame.configure(bg='#D9D9D9')

root.mainloop()