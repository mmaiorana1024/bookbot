def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    letter_count = get_count_letters(text)
    print(f"{letter_count}")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_count_letters(text):
    letter_count = {}
    words = text.split()
    for word in range(0, len(words)):
        for letter in words[word]:
            if letter.lower() in letter_count:
                letter_count[letter.lower()] += 1
            else:
                letter_count[letter.lower()] = 1
    return letter_count
                 

main()