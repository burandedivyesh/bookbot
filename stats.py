
# we are creating a separate function to read the contents of the file
def readFileText(filePath):
    with open(filePath) as f:
        fileContents = f.read()

    return fileContents


def countWords(fileText):
    Words = fileText.strip().split()
    #we are using the split method to split the words using the whitespaces
    return len(Words)

def countLetters(fileText):
    letterCount = dict()
    letters = list(fileText.lower())
    for i in set(letters):
        letterCount[i] = fileText.lower().count(i)
    #print(letterCount)
    return sortingDict(letterCount)

def sortingDict(letterCount):
    sortedList = []
    for k,v in letterCount.items():
        temp_dict = {}
        temp_dict["char"] = k
        temp_dict["nums"] = v
        sortedList.append(temp_dict)
    return sortedList

