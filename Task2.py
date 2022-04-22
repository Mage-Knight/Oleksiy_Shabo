# Our string.
our_string = 'sTreSS'

# Function, which returns first nonrepeating character.
def first_non_repeating_letter(our_string):
    lowercase_string = our_string.casefold()
    for symbol in lowercase_string:
        if lowercase_string.count(symbol) == 1:
            return our_string[lowercase_string.find(symbol)]
    return ""

# Output result.
print (first_non_repeating_letter(our_string))
