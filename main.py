import sys
from stats import number_of_words, frequency, chars_dict_to_sorted_list

'''
 sys.argv is a list of strings representing the arguments passed to the script. The first argument is the script name, the rest are the arguments.
'''

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(book_path, word_count, word_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in word_sorted:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = number_of_words(text)
    word_freq = frequency(text)
    word_sorted = chars_dict_to_sorted_list(word_freq)
    print_report(book_path, word_count, word_sorted)

main()