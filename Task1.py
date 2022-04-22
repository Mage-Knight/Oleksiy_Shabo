# List, which will be passed to the function filter_list.
unfiltered_list = [1, 2, 'a', 3, 'a', '123']

# Function, which filters the list.
def filter_list(unfiltered_list):
    filtered_list=unfiltered_list.copy()
    for element in unfiltered_list:
        if type(element) is str:
            filtered_list.remove(element)

    return filtered_list

# Output result.
print(filter_list(unfiltered_list))