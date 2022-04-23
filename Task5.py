# String that requires modification.
our_string = "Fred:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";

# Function that modifies the string.
def uppercase_sort(names_list):
    names_list = names_list.upper()
    # List for separated people's names and surnames.
    modified_names_list = []
    # Final list, which will be returned by the function.
    output_string = ""

    # Fill modified_names_list.
    while names_list:
        next_dot_coma = names_list.find(';')
        next_double_dot = names_list.find(':')
        if next_dot_coma == -1:
            modified_names_list.append([names_list[next_double_dot+1:], names_list[:next_double_dot]])
            names_list = False
        else:
            modified_names_list.append([names_list[next_double_dot+1:next_dot_coma], names_list[:next_double_dot]])
            names_list = names_list[next_dot_coma+1:]
    modified_names_list.sort()

    # Fill output_string.
    for people in modified_names_list:
        output_string += '(' + people[0] + ', ' + people[1] + ')'
    return output_string

# Output result.
print(uppercase_sort(our_string))
    