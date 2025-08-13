#Check if the array is a palindrome:

def is_palindrome(arr):
    return arr == arr[::-1]

arr = [1, 2, 3, 2, 1]
if is_palindrome(arr):
    print("The array is a palindrome")
else:
    print("The array is not a palindrome")
