
import sys
from stats import (
    get_num_words,
    chars_dict_to_sorted_list,
    get_chars_dict,
)


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_sorted_list)
    return entryCheck()


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

def entryCheck():
    # entryOne = sys.argv[0] 
    # # sys.argv[2] = ['main.py']
    # # firstBook = sys.argv[1]
    # print(sys.argv)
# Prints ['main.py', 'books/frankenstein.txt']
    arguments = sys.argv[1:]
    usersInput = ""
    if len(arguments) != 2:
        message = "Usage: python3 main.py books/frankenstein.txt"
        print(message)
        sys.exit(1)
    else:
        book_choice = arguments[0].lower()
        book_path_from_arg = arguments[1]
        if book_path_from_arg == 'frank':
            frankBook = "books/frankenstein.txt"
            print(frankBook)
        elif book_path_from_arg == 'moby':
            mobyBook = "books/mobydick.txt"
            print(mobyBook)
        elif book_path_from_arg == 'pride':
            prideBook = "prideandprejudice.txt"
            print(prideBook)
        else:
            try: FileNotFoundError
            
            finally:
                sys.exit(1)
                
            
        

main()
