import tkinter as tk
import re



App = tk.Tk()
App.geometry('800x500')
App.title('TESTS')


label = tk.Label(master=App)
label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

def findMarkdown(text: str) -> dict:
    patterns = {
    'bold': r'\*\*(.*?)\*\*',             # **bold text**
    'italic': r'\*(.*?)\*',               # *italic text*
    'code': r'\`(.*?)\`',                 # `code block here\n`
    'underline': r'~(.*?)~',              # ~underline text~
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

def formatTextHTML(originalText: str, indexAfterFormat: dict) -> str:
    styles = {
        'bold': ['<b>', '</b>'], 
        'italic': ['<i>', '</i>'], 
        'underline': ['<u>', '</u>']}
    for style, indexes in indexAfterFormat.items():
        # crashme


originalText = """This is some good text
wow very cool
it can go on **multiple lines**
and it can be *italic as well*
& ~underline too~"""

detectedMarkdown = findMarkdown(originalText)
detectedMarkdownIndex = findIndex(detectedMarkdown, originalText)
indexAfterFormat = findIndexAfterFormat(detectedMarkdownIndex)

print(detectedMarkdown)
print(detectedMarkdownIndex)

# App.mainloop()
