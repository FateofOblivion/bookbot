def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words():
    word_list = []
    word_list = (get_book_text("/home/fateofoblivion/bookbot/books/frankenstein.txt")).split()
    num_words = len(word_list)
    print(f"{num_words} words found in the document")