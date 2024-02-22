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
    sortedStartIndex = []

    for index in detectedMarkdownIndex.values():
        for currentIndex in index:
            sortedStartIndex.append(currentIndex[0])
    sortedStartIndex.sort()

    for markdownType, index in detectedMarkdownIndex.items():
        for i in range(len(sortedStartIndex)):
            for currentIndex in index:
                if sortedStartIndex[i] == index[0]:
                    sortedMarkdown.append((markdownType, currentIndex[0], currentIndex[1]))

# this function need to be fixed
# this function need to be fixed

    return sortedMarkdown


def findIndexAfterFormat(detectedMarkdownIndex: dict) -> dict:
    indexAfterFormat = {}
    totalOffset = 0

    for markdownType, index in detectedMarkdownIndex.items():
        indexAfterFormat[markdownType] = []
        for currentIndex in index:
            if markdownType == 'bold':
                indexAfterFormat[markdownType].append((currentIndex[0] - totalOffset - 2, currentIndex[1] - totalOffset - 2))
                totalOffset += 4
            else:
                indexAfterFormat[markdownType].append((currentIndex[0] - totalOffset - 1, currentIndex[1] - totalOffset - 1))
                totalOffset += 2
    
    return indexAfterFormat


def setTextWidget(textWidget: tk.Text, text: str):
    # find index of the detected markdown in the text
    detectedMarkdown = findMarkdown(text)
    detectedMarkdownIndex = findIndex(detectedMarkdown, text)

    # default paragraph font
    pFont = ('Inter', 15)

    # configure the custom tags
    textWidget.tag_config('bold_text', font=(pFont[0], pFont[1], 'bold'))
    textWidget.tag_config('italic_text', font=(pFont[0], pFont[1], 'italic'))
    textWidget.tag_config('underline_text', font=(pFont[0], pFont[1], 'underline'))
    textWidget.tag_config('code_text', font=(pFont[0], pFont[1], 'bold'), background='#383e4a', foreground='#4794af')
    # to be continued
