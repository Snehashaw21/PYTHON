#Find the first non-repeating element in an array:

def first_non_repeating(arr):
    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for num in arr:
        if freq[num] == 1:
            return num
    return None
arr = [9, 4, 9, 6, 7, 4]
print("First Non-Repeating Element:", first_non_repeating(arr))
