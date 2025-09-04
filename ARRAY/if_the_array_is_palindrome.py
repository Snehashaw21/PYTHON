#Check if the array is a palindrome:

def is_palindrome(arr):
    n = len(arr)
    for i in range(n // 2):
        if arr[i] != arr[n - i - 1]:
            return False
    return True

arr = [1, 2, 3, 2, 1]
print("Array:", arr)
print("Is Palindrome?", is_palindrome(arr))
