def get_book():
    with open('books/frankenstein.txt') as f:
        return f.read()
        
def count_words(book):
    # print(type(book.split()))
    return len(book.split())

def count_letters(book):
    to_lower = book.lower()
    letter_dict = {}
    for letter in to_lower:
        if letter in letter_dict.keys():
            letter_dict[letter] = letter_dict[letter] + 1
        else:
            letter_dict[letter] = 1
    return letter_dict

def sorte_me(dictme):
    return dictme["letter_cnt"]

def main():
    my_book = get_book()
    # print(my_book)
    word_count = count_words(my_book)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    
    letter_count = count_letters(my_book)
    # print(letter_count)
    list_of_letters = []
    
    for letter_key in letter_count.keys():
        if letter_key.isalpha():
            list_of_letters.append({"letter" :letter_key, "letter_cnt": letter_count[letter_key]})
    # print(list_of_letters)

    list_of_letters.sort(reverse=True, key=sorte_me)

    for letter in list_of_letters:        
        print(f"The'{letter["letter"]}' character was found {letter["letter_cnt"]} times")
    print("--- End Report ---")


if __name__=="__main__":
    main()