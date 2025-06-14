def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(text):
    word_list = []
    word_list = (get_book_text(text)).split()
    num_words = len(word_list)
    return num_words
    

    

def num_of_letters(full_text):
    letter_list = {}
    for letters in full_text:
        if letters.lower() in letter_list and letter_list[letters.lower()] >= 1:
            letter_list[letters.lower()] += 1
        else:
            letter_list[letters.lower()] = 1

    return letter_list

def character_dict_to_sorted_list(dict):
    sorted = []
    for keys in dict:
        if keys.isalpha():
            sorted.append({"name":keys, "num":dict[keys]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

# [{'name': 'plane', 'num': 10}, {'name': 'car', 'num': 7}, {'name': 'boat', 'num': 2}]