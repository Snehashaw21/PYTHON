#Find the first repeating element in an array:

def first_repeating(arr):
    seen = set()
    for num in arr:
        if num in elem:
            return num   
        elem.add(num)
    return None  # No repeating element

arr = [10, 5, 3, 4, 3, 5, 6]
print("First Repeating Element:", first_repeating(arr))
