# For a list of words, prints out each word on a separate line, but in all uppercase.
# you should be able to pass in a set of letters, and it only prints words that start with one of those letters.

def print_upper_words(words,must_start_with={}):

    """ 
    This function accepts a list of words and a set of letters (default to empty set if no letters provided)

    If no letters are provided, it will print each word out on a separate line in all caps

    If a set of letters is provided, it will only print the words that start with that letter (not case sensitive)
    
    """

    if must_start_with:
        
        for word in words:
            cap_word = word.upper()
            for letter in must_start_with:
                cap_letter = letter.upper()
                if cap_word.startswith(cap_letter):
                    print(cap_word)

    else:
        for word in words:
            print(word.upper())


