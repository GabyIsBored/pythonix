import re       # Regular expression operations lib
import tkinter as tk



def findMarkdown(text: str) -> dict:
    patterns = {
        'bold': r'__(.*?)__',       # __bold text__
        'italic': r'_(.*?)_',       # _italic text_
        'code': r'\$(.*?)\$',       # $constexpr a = {0};$ (code block)
        'underline': r'~(.*?)~'     # ~underline text~
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


def setTextWidget(textWidget: tk.Text, text: str):
    splitlines = text.splitlines()

    # font
    pFont = ('Inter', 15)
    backgroundColor = '#d9d9d9'

    textWidget['font'] = pFont
    textWidget['background'] = backgroundColor
    
    # itarate the splitlines & set the tags
    for i in range (len(splitlines)):
        newLineNumber = i + 1
        setTextWidgetOnLine(textWidget, splitlines[i], newLineNumber)
        if i != len(splitlines) - 1:
            textWidget.insert(tk.END, '\n')

    # turn targetTextWidget in read only
    textWidget['state'] = tk.DISABLED
