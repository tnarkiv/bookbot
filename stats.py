""" Contains statistical analysis methods """

def count_number_of_words(text):
    """counts the number of words in a given text string

    Args:
        text (_type_): string

    Returns:
        _type_: integer
    """
    number_of_words = len(text.split())
    return number_of_words
