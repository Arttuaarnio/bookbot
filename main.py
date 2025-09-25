from stats import count_book_words, count_book_characters

def get_book_text(path):
    with open(path) as f:
        book_data = f.read()
    return book_data

def main():
    book = get_book_text("./books/frankenstein.txt")
    word_count = count_book_words(book)
    characters = count_book_characters(book)
    print(f"Found {word_count} total words")
    print(characters)

main()
    
