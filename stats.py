def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words():
    word_list = []
    word_list = (get_book_text("/home/fateofoblivion/bookbot/books/frankenstein.txt")).split()
    num_words = len(word_list)
    print(f"{num_words} words found in the document")
    

    

def num_of_letters(full_text):
    letter_list = {}
    for letters in full_text:
        if letter_list[letters.lower()] == True and letter_list[letters.lower()] >= 1:
            letter_list[letters.lower()] += 1
        else:
            letter_list[letters.lower()] = 1
    return letter_list

get_num_words()
num_of_letters(get_book_text("/home/fateofoblivion/bookbot/books/frankenstein.txt"))