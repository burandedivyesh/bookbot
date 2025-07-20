# Importing functions from our stats.py file
import sys
from stats import readFileText
from stats import countWords
from stats import countLetters

pathToBook = "/home/thatguy/Development/workspace/github.com/bookbot/books/" + sys.argv[1] 

def main():
    fileText = readFileText(pathToBook)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f'Found {countWords(fileText)} total words')
    print("--------- Character Count -------")
    charCounts = countLetters(fileText)
    
    #sort function to given as key for sorting out the list
    def sort_on(items):
        return items['nums']
    charCounts.sort(reverse=True,key = sort_on)

    for i in charCounts:
        print(f'{i["char"]}: {i["nums"]}')
    print("============= END ===============")

main()

#we have made a new function to read the contetns of the file and we can use this function anywhere
#to read the contetns of the file


