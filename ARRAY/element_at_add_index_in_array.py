#Print elements at odd indexes of an array:
#odd indexes (i.e., index 1, 3, 5, ...) of an array:

def odd_index_elements(arr):
    for i in range(1, len(arr), 2):   # step = 2
        print(f"Index {i} -> {arr[i]}")

arr = [10, 20, 30, 40, 50, 60]
print("Elements at odd indexes:")
odd_index_elements(arr)
