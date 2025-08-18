#Find the index of the last occurrence of an element in an array:

def last_occurrence(arr, target):
    last_index = -1
    for i in range(len(arr)):
        if arr[i] == target:
            last_index = i
    return last_index

arr = [10, 20, 30, 20, 40, 50, 20]
target = 20

result = last_occurrence(arr, target)
if result != -1:
    print(f"Last occurrence of {target} is at index {result}")
else:
    print("Element not found")
