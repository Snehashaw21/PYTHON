#Count how many elements appear only once in the array:

def count_unique(arr):
    freq = {} 
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    count = 0
    for value in freq.values():
        if value == 1:
            count += 1
    return count

# Example
arr = [10, 20, 30, 10, 20, 40, 50]
print("Array:", arr)
print("Count of elements that appear only once:", count_unique(arr))
