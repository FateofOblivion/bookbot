from stats import get_num_words
from stats import num_of_letters
from stats import character_dict_to_sorted_list 
def main():
    text_location = "/home/fateofoblivion/bookbot/books/frankenstein.txt"
    print("============ BOOKBOT ============") 
    
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text_location)} total words")
    print("--------- Character Count -------")
    for dicts in character_dict_to_sorted_list(num_of_letters(get_book_text(text_location))):
        print(f"{dicts[0]}: {dict[1]}") 
    print("============= END ===============")

main()