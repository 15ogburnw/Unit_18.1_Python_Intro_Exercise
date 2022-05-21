# For a list of words, prints out each word on a separate line, but in all uppercase.
# you should be able to pass in a set of letters, and it only prints words that start with one of those letters.

def print_upper_words(words,must_start_with={}):

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



# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})