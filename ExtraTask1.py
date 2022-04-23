# Our number.
num = 198765432

# Function, which filters the list.
def nextBigger(num):
    # Reverse the number and convert it into the list of digits.
    reverse_list_num = [int(digit) for digit in str(num)[::-1]]
    for i in range(1, len(reverse_list_num)):
        for digit in reverse_list_num[:i]:
            if digit > reverse_list_num[i]:
                # Swap digits.
                place = reverse_list_num.index(digit)
                save = reverse_list_num[i]
                reverse_list_num[i] = reverse_list_num[place]
                reverse_list_num[place] = save
                # Reverse the list again and convert it into int.
                return int("".join(map(str, reverse_list_num[::-1])))
    return -1

# Output result.
print(nextBigger(num))