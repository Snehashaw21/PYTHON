#Find the second largest element in an array:

def find_second_largest(arr):
    if len(arr) < 2:
        return None  # Not enough elements
    
    largest = second = float('-inf')
    
    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
            
    return second if second != float('-inf') else None

arr = [10, 45, 99, 2, 56]
result = find_second_largest(arr)

if result is not None:
    print("Second largest element is:", result)
else:
    print("No second largest element found.")
