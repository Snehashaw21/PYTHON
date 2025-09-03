#Check if an array contains only positive numbers:

def is_all_positive(arr):
    for num in arr:
        if num <= 0:
            return False
    return True

arr = [5, 12, 8, 1, 20]
print("Array:", arr)
print("Contains only positive numbers?", is_all_positive(arr))
