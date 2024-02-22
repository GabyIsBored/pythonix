import re       # Regular expression operations lib


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


# todo: 
# def setTextWidget(textWidget: tk.Text, text: str):
# this function should do all of the formatting job
# maybe create a function to detect where the line is located
