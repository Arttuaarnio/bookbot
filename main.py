def get_book_text(path):
    with open(path) as f:
        book_data = f.read()
    return book_data

def count_book_words(book):
    words = book.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count


def main():
    book = get_book_text("./books/frankenstein.txt")
    word_count = count_book_words(book)
    print(f"Found {word_count} total words")

main()
    
