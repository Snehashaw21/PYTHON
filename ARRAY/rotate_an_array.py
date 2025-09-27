#Rotate an array by k positions (left or right).
#Output:
#Original Array: [1, 2, 3, 4, 5]
#After left rotation: [3, 4, 5, 1, 2]


def rotate_left(arr, k):
    n = len(arr)
    k = k % n  # handle if k > n
    return arr[k:] + arr[:k]

arr = [1, 2, 3, 4, 5]
k = 2
print("Original Array:", arr)
print("After left rotation:", rotate_left(arr, k))
