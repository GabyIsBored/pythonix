import re       # Regular expression operations lib
import tkinter as tk



class BLabel(object):
    b = "•"
    def __init__(self,master):
        import tkinter as tk
        self.l = tk.Label(master)
    def add_option(self,text):
        if self.l.cget("text") == "":
            self.l.config(text=self.b+" "+text)
        else:
            self.l.config(text=self.l.cget("text") +"\n"+ self.b + " "+text)

def findMarkdown(text: str) -> dict:
    patterns = {
        'bold': r'__(.*?)__',       # __bold text__
        'italic': r'_(.*?)_',       # _italic text_
        'code': r'\$(.*?)\$',       # $constexpr a = {0};$ (code block)
        'underline': r'~(.*?)~',    # ~underline text~
    }
    detectedMarkdown = {}
    for key, pattern in patterns.items():
        currentMarkdown = re.findall(pattern, text)
        correctMarkdown = []
        for markdown in currentMarkdown:
            if markdown != '':
                correctMarkdown.append(markdown)
        detectedMarkdown[key] = correctMarkdown
    
    return detectedMarkdown

def findIndex(detectedMarkdown: dict, originalText: str) -> dict:
    detectedMarkdownIndex = {}
    startIndex = 0
    stopIndex = 0

    for markdownType, subText in detectedMarkdown.items():
        detectedMarkdownIndex[markdownType] = []
        for currentSubText in subText:
            startIndex = originalText.find(currentSubText)
            stopIndex = startIndex + len(currentSubText) - 1
            if startIndex != -1:    
                detectedMarkdownIndex[markdownType].append((startIndex, stopIndex))
    
    return detectedMarkdownIndex

def sortMarkdown(detectedMarkdownIndex: dict) -> list:
    sortedMarkdown = []
    combinedIndex = []

    for markdownType, index in detectedMarkdownIndex.items():
        for start, end in index:
            combinedIndex.append((markdownType, start, end))
    
    sorted_indices = sorted(combinedIndex, key=lambda x: (x[1], x[0]))
    
    for markdownType, start, end in sorted_indices:
        sortedMarkdown.append((markdownType, start, end))
    
    return sortedMarkdown

def findIndexAfterFormat(detectedMarkdownIndex: dict) -> dict:
    indexAfterFormat = {}
    totalOffset = 0
    sortedMarkdown = sortMarkdown(detectedMarkdownIndex)

    for item in sortedMarkdown:
        markdownType = item[0]
        startIndex = item[1]
        stopIndex = item[2]

        if markdownType not in indexAfterFormat:
            indexAfterFormat[markdownType] = []

        if markdownType == 'bold':
            indexAfterFormat[markdownType].append((startIndex - totalOffset - 2, stopIndex - totalOffset - 2))
            totalOffset += 4
        else:
            indexAfterFormat[markdownType].append((startIndex - totalOffset - 1, stopIndex - totalOffset - 1))
            totalOffset += 2

    return indexAfterFormat

def setTextWidgetOnLine(textWidget: tk.Text, text: str, lineNumber: int):
    # find index of the detected markdown in the text
    detectedMarkdown = findMarkdown(text)
    detectedMarkdownIndex = findIndex(detectedMarkdown, text)
    indexAfterFormat = findIndexAfterFormat(detectedMarkdownIndex)

    # font
    pFont = ('Inter', 15)
    backgroundColor = '#d9d9d9'
    codeBackgroundColor = '#848484'
    textColor = '#000000'
    codeTextColor = '#C94053'

    # configure the custom tags
    textWidget.tag_config('bold', font=(pFont[0], pFont[1], 'bold'), background=backgroundColor)
    textWidget.tag_config('italic', font=(pFont[0], pFont[1], 'italic'), background=backgroundColor)
    textWidget.tag_config('underline', font=(pFont[0], pFont[1], 'underline'), background=backgroundColor)
    textWidget.tag_config('code', font=(pFont[0], pFont[1], 'bold'), background=codeBackgroundColor, foreground=codeTextColor)
    textWidget.tag_config('default', background=backgroundColor, foreground=textColor)

    # configure text widget
    for element in ['__', '_', '~', '$']:
        text = text.replace(element, '')

    textWidget.insert(tk.INSERT, text)
    textWidget.tag_add('default', f'{lineNumber}.0', f'{lineNumber}.end')

    # apply custom tags
    for markdownTag, markdownIndexArr in indexAfterFormat.items():
        for currentMarkdownIndex in markdownIndexArr:
            startIndex = currentMarkdownIndex[0]
            endIndex = currentMarkdownIndex[1] + 1

            if markdownTag == 'bold':
                textWidget.tag_add('bold', f'{lineNumber}.{startIndex}', f'{lineNumber}.{endIndex}')

            elif markdownTag == 'italic':
                textWidget.tag_add('italic', f'{lineNumber}.{startIndex}', f'{lineNumber}.{endIndex}')

            elif markdownTag == 'underline':
                textWidget.tag_add('underline', f'{lineNumber}.{startIndex}', f'{lineNumber}.{endIndex}')
            
            elif markdownTag == 'code':
                textWidget.tag_remove('default', f'{lineNumber}.{startIndex}', f'{lineNumber}.{endIndex}')
                textWidget.tag_add('code', f'{lineNumber}.{startIndex}', f'{lineNumber}.{endIndex}')


def setHeaders(textWidget: tk.Text, text: str, lineNumber: int):
    # font
    h1font = ('Inter', 40)
    h2font = ('Inter', 24)
    h3font = ('Inter', 20)
    
    backgroundColor = '#d9d9d9'
    h3textColor = '#9d68d3'
    
    # configure the custom tags
    textWidget.tag_config('h1', font=(h1font[0], h1font[1], 'bold'), background=backgroundColor)
    textWidget.tag_config('h2', font=(h2font[0], h2font[1], 'bold'), background=backgroundColor)
    textWidget.tag_config('h3', font=(h3font[0], h3font[1], 'bold'), foreground=h3textColor, background=backgroundColor)
    
    # set headers
    if len(text) >= 4:
        if text[0] == '#' and text[1] == ' ':
            textWidget.delete(f'{lineNumber}.0', tk.END)  # THE ERROR IS HERE TK.END DELETE EVERYTHING
            textWidget.insert(tk.INSERT, text[2:])
            textWidget.tag_add('h1', f'{lineNumber}.{0}', f'{lineNumber}.{tk.END}')
        elif text[0] == '#' and text[1] == '#' and text[2] == ' ':
            textWidget.delete(f'{lineNumber}.0', tk.END)
            textWidget.insert(tk.INSERT, text[3:])
            textWidget.tag_add('h2', f'{lineNumber}.{0}', f'{lineNumber}.{tk.END}')
        elif text[0] == '#' and text[1] == '#' and text[2] == '#' and text[3] == ' ':
            textWidget.delete(f'{lineNumber}.0', tk.END)
            textWidget.insert(tk.INSERT, text[4:])
            textWidget.tag_add('h3', f'{lineNumber}.{0}', f'{lineNumber}.{tk.END}')
    
    

def setTextWidget(textWidget: tk.Text, text: str, isCode:bool):
    splitlines = text.splitlines()

    # font
    pFont = ('Inter', 15)
    backgroundColor = '#d9d9d9'

    pFont2 = ('Inter', 15)
    backgroundColor2 = '#191919'
    foregroundColor = '#FFFFFF'

    if isCode==False:
        textWidget['font'] = pFont
        textWidget['background'] = backgroundColor
    if isCode==True:
        #new colors
        textWidget['font'] = pFont2
        textWidget['background'] = backgroundColor2
        textWidget['foreground'] = foregroundColor
    
    # itarate the splitlines & set the tags
    for i in range (len(splitlines)):
        newLineNumber = i + 1
        setTextWidgetOnLine(textWidget, splitlines[i], newLineNumber)
        setHeaders(textWidget, splitlines[i], newLineNumber)
        if i != len(splitlines) - 1:
            textWidget.insert(tk.END, '\n')

    # turn targetTextWidget in read only
    textWidget['state'] = tk.DISABLED
    

# TEST - TODELETE

root = tk.Tk()
root.geometry('800x400')


unit_content = """
# Affectation d’une variable

### L’opérateur ‘=’

Le symbole ‘=’ permet d’assigner à une variable une certaine valeur :

`x = 1`

- x étant la variable crée (son ‘nom’)
- 1 étant sa valeur d’initialisation (sa ‘valeur’)

On appel ce symbole un *opérateur* et fait partie des opérateurs d’assignation. Il existe de nombreux opérateurs, parmis lequels figurent les opérateurs **d’assignations**, les opérateurs **arithmétiques**, les opérateurs **de comparaison** etc… Ils seront donc introduits dans un prochain chapitre.

### Autre propriété d’affectation

Une variable peut également être initialisée à partir de la valeur stockée dans une autre variable.

De cette manière on peut utiliser la valeur d’une variable et lui faire subir des modifications sans modifier la variable dont la valeur a été copié.

### Exemple 1

`defaultValue = 50           # defaultVaue est initialisé avec 50`

`testValue = defaultValue    # testValue est initialisé avec defaultValue (50)`

`testValue = 20              # defaultValue est toujours égale à 50`

TIP: Lors de la déclaration d’une variable, elle doit avoir une valeur d’initialisation ou le programme resultera en une erreur.

- Ligne 1: la variable `defaultValue` est crée, et initialisée avec le nombre entier 50.
- Ligne 2: la variable `testValue` est crée, et initialisée avec la valeur qui est stockée dans la variable `defaultValue` , 50 dans ce cas.
- Ligne 3: la variable `testValue` subit une modification, sa valeur précédente se fait ‘écraser’ et se  fait remplacer par 20.
"""

widget = tk.Text()

setTextWidget(widget, unit_content, True)

widget.pack()

root.mainloop()
