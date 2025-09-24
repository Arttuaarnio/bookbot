def get_book_text(path):
    with open(path) as f:
        book_data = f.read()
    return book_data

def main():
    book = get_book_text("./books/frankenstein.txt")
    print(book)

main()
    
