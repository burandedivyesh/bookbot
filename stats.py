def count_words(content):
    return(len(content.split()))

def count_characters(content):
    count = {}
    for letter in set(content.lower()):
        count[letter] = content.lower().count(letter)
    return count

def sort_on(items):
    return count_characters

