def count_book_words(book):
    words = book.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def count_book_characters(book):
    characters = {}

    for i in range(len(book)):
        char = book[i]
        char = char.lower()

        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1

    return characters


