from stats import get_words_count
from stats import get_characters_count
from stats import get_sorted_characters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_content = get_book_text(book_path)
    num_words = get_words_count(book_content)
    characters_count = get_characters_count(book_content)
    sorted_characters = get_sorted_characters(characters_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_characters:
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()
