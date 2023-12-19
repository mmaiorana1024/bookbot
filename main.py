def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n\n")
    letter_count = get_count_letters(text)
    get_list_of_char(letter_count)
    print("--- End report ---")

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

def get_list_of_char(text):
    list_of_letters = []
    
    for letter in text:
        if letter.isalpha():
          list_of_letters.append(letter)
    
    list_of_letters.sort()
    
    for letter in range(0, len(list_of_letters)):
        print(f"The '{list_of_letters[letter]}' character was found {text[list_of_letters[letter]]} times")
    

main()