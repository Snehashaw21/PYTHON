#Find the most frequent element in the array:

def most_frequent(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    max_freq = max(freq.values())
    for key, value in freq.items():
        if value == max_freq:
            return key

arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print("Array:", arr)
print("Most frequent element:", most_frequent(arr))
