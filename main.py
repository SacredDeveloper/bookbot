from stats import get_text_length, get_character_count
import sys

def get_book_text(file_path: str) -> str:
    with open(file_path) as file:
        book_text = file.read()
    return book_text

def main(args):
    try:
        filepath = args[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:   
        text = get_book_text(filepath)
        word_count = get_text_length(text)
        character_count = get_character_count(text)
        print(f"Found {word_count} total words")
        print(character_count)

main(sys.argv)
