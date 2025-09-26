from stats import count_book_words, count_book_characters, sort_characters

def get_book_text(path):
    with open(path) as f:
        book_data = f.read()
    return book_data

def main():
    book = get_book_text("./books/frankenstein.txt")
    word_count = count_book_words(book)
    characters = count_book_characters(book) 
    sorted_characters = sort_characters(characters)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for character in sorted_characters:
        if character["char"].isalpha():
            print(f"{character['char']}: {character['num']}")

main()
    
