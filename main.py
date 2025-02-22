from stats import count_number_of_words
import sys

def count_characters(text):    
    text = text.lower()
    character_dictionary = {}
    for character in text:
        if(character in character_dictionary):
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1
    return character_dictionary

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = None
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    with open(path) as f:
        text = f.read()    
    number_of_words = count_number_of_words(text)
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    character_dictionary = count_characters(text)
    for key, value in character_dictionary.items():
        if(key >= 'a' and key <= 'z'):
            print(f"{key}: {value}")

main()