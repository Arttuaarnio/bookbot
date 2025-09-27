from stats import count_book_words, count_book_characters, sort_characters
import sys

def get_book_text(path):
    with open(path) as f:
        book_data = f.read()
    return book_data

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        get_chosen_book = sys.argv[1]
        book = get_book_text(get_chosen_book)
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
    
