# 1. We need to fix naming conventions for the functions and variables
# 2. We need to fix any false logic
# 3. We need to fix 



def readFileText(filePath):
    """function to read the parse the file as string"""
    with open(filePath) as f:
        fileContents = f.read()
    return fileContents


def countWords(fileText):
    """function to count the number of words"""
    Words = fileText.split()
    return len(Words)

def countLetters(fileText):
    """function to count number of characters in the file contents"""
    letterCount = dict()
    letters = list(fileText.lower())
    for i in set(letters):
        letterCount[i] = fileText.lower().count(i)
    #print(letterCount)
    return wordList(letterCount)

def wordList(letterCount):
    sortedList = []
    for k,v in letterCount.items():
        temp_dict = {}
        temp_dict["char"] = k
        temp_dict["nums"] = v
        sortedList.append(temp_dict)
    return sortedList

