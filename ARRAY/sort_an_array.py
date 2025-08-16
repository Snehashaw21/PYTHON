#Sort an array in ascending order without using sort():
#Using Bubble Sort approach:


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [64, 25, 12, 22, 11]
print("Original array:", arr)
print("Sorted array:", bubble_sort(arr))
