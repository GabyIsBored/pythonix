import tkinter as tk


class BLabel(object):
    b = "•"
    def __init__(self,master):
        import tkinter as tk
        self.l = tk.Label(master, background='#D9D9D9')
    def add_option(self,text):
        if self.l.cget("text") == "":
            self.l.config(text=self.b+" "+text)
        else:
            self.l.config(text=self.l.cget("text") +"\n"+ self.b + " "+text)


def changeTags(targetTextWidget: tk.Text, targetText: str, arr: list):
    targetTextWidget.pack(expand=True, fill='both')

    # default paragraph font
    pFont = ('Yu Gothic Ui', 15)

    # configure the custom tags
    targetTextWidget.tag_config('bold_text', font=(pFont[0], pFont[1], 'bold'))
    targetTextWidget.tag_config('italic_text', font=(pFont[0], pFont[1], 'italic'))
    targetTextWidget.tag_config('underline_text', font=(pFont[0], pFont[1], 'underline'))
    targetTextWidget.tag_config('code_text', font=(pFont[0], pFont[1], 'bold'), background='#383e4a', foreground='#4794af')

    # configure text widget
    for element in ['__', '_', '~', '$']:
        targetText = targetText.replace(element, '')
    targetTextWidget.insert(tk.INSERT, targetText)
    targetTextWidget['font'] = pFont

    # apply custom tags
    for tag_text, startIndexes, stopIndexes in arr:
        targetTextWidget.tag_add(tag_text + '_text', str(startIndexes[0]) + '.' + str(startIndexes[1]), str(stopIndexes[0]) + '.' + str(stopIndexes[1]))

    # turn targetTextWidget in read only
    targetTextWidget['state'] = tk.DISABLED

def getTagsUnchanged(targetText: str) -> dict:      # [(type, [start_line, start_index], [stop_line, stop_index]), ...] Welcome to wheelchair function n°1
    # result = {'bold': [], 'italic': [], 'underline': [], 'code': []}
    # occurrence = [0, 0, 0]     # [*, $, ~]
    occurredValue = []         # [(type, start_index, stop_index), ()]
    startingIndex = 0
    stoppingIndex = 0
    isStartMatched = False
    currentLine = 1
    currentChar = 0
    startingLine = [0] * 4      #['bold', 'italic', 'code', 'underline']
    targetText = targetText + '/ENDSTR/'
    for i in range(len(targetText)):
        if targetText[i] == '\\' and targetText[i+1] == 'n':
            currentLine+=1
            currentChar = -1
        elif targetText[i] == '\n':
            currentLine+=1
            currentChar = 0
        if targetText[i] == '_' and targetText[i+1] == '_':
            if isStartMatched == False:
                isStartMatched = True
                startingIndex = currentChar - 1
                startingLine[0] = currentLine
            else:
                isStartMatched = False
                stoppingIndex = currentChar - 3          # To change if miscalculation
                occurredValue.append(('bold', [startingLine[0], startingIndex], [currentLine, stoppingIndex]))
                startingIndex = 0
                stoppingIndex = 0
        elif targetText[i] == '_' and targetText[i-1] != '_':
            if isStartMatched == False:
                isStartMatched = True
                startingLine[1] = currentLine
                if targetText[i-1] == '\n':
                    startingIndex = currentChar
                else:
                    startingIndex = currentChar + 1      # To change if miscalculation
            else:
                isStartMatched = False
                stoppingIndex = currentChar
                occurredValue.append(('italic', [startingLine[1], startingIndex - 1], [currentLine, stoppingIndex - 1]))
                startingIndex = 0
                stoppingIndex = 0
        elif targetText[i] == '$':
            if isStartMatched == False:
                isStartMatched = True
                startingLine[2] = currentLine
                if targetText[i-1] == '\n':
                    startingIndex = currentChar
                else:
                    startingIndex = currentChar + 1      # To change if miscalculation
            else:
                isStartMatched = False
                stoppingIndex = currentChar
                occurredValue.append(('code', [startingLine[2], startingIndex - 1], [currentLine, stoppingIndex - 1]))
                startingIndex = 0
                stoppingIndex = 0
        elif targetText[i] == '~' and targetText[i+1] == '~':
            if isStartMatched == False:
                isStartMatched = True
                startingIndex = currentChar - 1
                startingLine[3] = currentLine
            else:
                isStartMatched = False
                stoppingIndex = currentChar - 2
                occurredValue.append(('underline', [startingLine[3], startingIndex - 1], [currentLine, stoppingIndex - 1]))
                startingIndex = 0
                stoppingIndex = 0
        currentChar += 1
    return occurredValue

def formatTextWidget(textWidget: tk.Text, text: str):
    formatOccurrence = getTagsUnchanged(text)
    textWidget['background'] = '#D9D9D9'
    changeTags(textWidget, text, formatOccurrence)