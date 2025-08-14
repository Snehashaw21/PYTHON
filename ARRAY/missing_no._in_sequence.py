#Find the missing number in a sequence of numbers:

def find_missing_number(arr, n):
    for i in range(1, n+1):
        if i not in arr:
            return i

arr = [1, 2, 4, 5, 6]
n = 6  # Total numbers expected
print("Missing number is:", find_missing_number(arr, n))
