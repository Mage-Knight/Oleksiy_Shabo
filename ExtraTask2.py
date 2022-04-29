# Our number, which will be converted to IPv4 address.
num = 2149583361

# Function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.
def num_to_address(num):
    # List where will be stored digits of num converted to binary number system.
    binary_list = []
    # String where will be stored IPv4 address.
    octet_str = ""
    
    # Converting num from decimal to binary.
    while num > 1:
        modulus = num % 2
        num //= 2
        binary_list.append(modulus)
    binary_list.append(num)
    binary_list += [0 for i in range(32 - len(binary_list))]
    # Reverse number after division ending.
    binary_list = binary_list[::-1]

    # Form IPv4 address.
    for i in range(4):
        sum = 0
        for j in range(8):
            sum += binary_list[8 * i + j] * 2 ** (8 - (j + 1) )
        octet_str += str(sum)
        if i != 3:
            octet_str += '.'
    return octet_str

# Output result.
print(num_to_address(num))