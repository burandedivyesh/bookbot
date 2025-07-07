from stats import count_words
from stats import count_characters

path_to_frankenstein = "/home/thatguy/Development/workspace/github.com/bookbot/books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def main():
    print(get_book_text(path_to_frankenstein))
    words = count_words(get_book_text(path_to_frankenstein))
    print(words,"words found in the document")

    print(count_characters(get_book_text(path_to_frankenstein)))
    
main()

