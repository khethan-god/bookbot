def get_text(path):
    with open(path) as f:
        # read the total bytes and return a string
        return f.read()


def word_count(text):
    words = text.split()
    return len(words)


def character_count(text):
    text_lower = text.lower()  # convert the text to lower case
    char_count = {}
    for c in text_lower:
        char_count[c] = char_count.get(c, 0) + 1
    return char_count


def report(char_count):
    # sort the dictionary based on reverse of values (descending order)
    sorted_char_count = {k: v for k, v in sorted(char_count.items(), key= lambda item: item[1], reverse=True)}
    for c in sorted_char_count:
        if c.isalpha():
            print(f"The '{c}' character was found {char_count[c]} times")


def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = word_count(text)
    char_count = character_count(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    report(char_count)
    print("--- End report ---")
    

if __name__ == "__main__":
    main()
