#Find the most frequent element in the array:

def most_frequent(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    max_count = max(freq.values())
    for key, value in freq.items():
        if value == max_count:
            return key

arr = [1, 3, 2, 3, 4, 3, 5, 2]
print("Most frequent element:", most_frequent(arr))
