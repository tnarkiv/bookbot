from stats import count_number_of_words

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
    path = "books/frankenstein.txt"
    text = None
    with open(path) as f:
        text = f.read()
    print(f"--- Begin report of {path} ---")
    number_of_words = count_number_of_words(text)
    print(f"{number_of_words} words found in the document\n")
    character_dictionary = count_characters(text)
    for key, value in character_dictionary.items():
        if(key >= 'a' and key <= 'z'):
            print(f"The \'{key}\' was found {value} times")

main()