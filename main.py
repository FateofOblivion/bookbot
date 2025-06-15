from stats import get_book_text
from stats import get_num_words
from stats import num_of_letters
from stats import character_dict_to_sorted_list
import sys
def main():
    
    if len(sys.argv) != 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
    text_location = sys.argv[1]
    print("============ BOOKBOT ============") 
    
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text_location)} total words")
    print("--------- Character Count -------")
    for dicts in character_dict_to_sorted_list(num_of_letters(get_book_text(text_location))):
        print(f"{dicts['name']}: {dicts['num']}") 
    print("============= END ===============")

main()