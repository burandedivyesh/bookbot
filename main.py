#we gonna need a with block to handle the file,
#with block helps us to open the file and closes automatically when the block is exited

# we would also need the path to the file

from stats import readFileText
from stats import countWords
from stats import countLetters

pathToBook = "/home/thatguy/Development/workspace/github.com/bookbot/books/frankenstein.txt"

def printReport():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")

def main():
    fileText = readFileText(pathToBook)
    #print(countWords(fileText), "words found in the document")
    #print(countLetters(fileText))
    printReport()
    print(f'Found {countWords(fileText)} total words')
    print("--------- Character Count -------")
    finalCounts = countLetters(fileText)
    
    def sort_on(items):
        return items['nums']

    finalCounts.sort(reverse=True,key = sort_on)

    for i in finalCounts:
        print(f'{i["char"]}: {i["nums"]}')
    print("============= END ===============")

main()

#we have made a new function to read the contetns of the file and we can use this function anywhere
#to read the contetns of the file


