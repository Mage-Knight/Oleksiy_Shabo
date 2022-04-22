# Our number.
number = 493193

# Function, which returns the recursive sum of all the digits in a number.
def digital_root(number):
    str_number = str(number)
    while len(str_number) > 1:
        sum = 0
        for digit in str_number:
            sum += int(digit)
        str_number = str(sum)
    return int(str_number)

# Output result.
print(digital_root(number))