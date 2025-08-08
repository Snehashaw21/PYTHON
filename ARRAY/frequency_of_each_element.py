#Find the frequency of each element in an array.:

def find_frequency(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

arr = [1, 2, 2, 3, 4, 4, 4, 5]

frequency = find_frequency(arr)

for key, value in frequency.items():
    print(f"{key} occurs {value} times")
