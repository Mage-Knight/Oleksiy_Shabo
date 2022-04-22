# Our array of numbers and target number.
arr = [1, 3, 6, 2, 2, 0, 4, 5]
target_num = 5

# Function, that counts the number of pairs in the array, the sum of which will give target.
def count_num_pairs(arr, target_num):
    counter = 0
    arr_length = len(arr)
    if arr_length >= 2:
        for i in range(arr_length):
            for j in arr[i:]:
                if arr[i] + j == target_num:
                    counter += 1
        return counter
    else:
        return 0

# Output result.
print(count_num_pairs(arr, target_num))