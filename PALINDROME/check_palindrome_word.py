#Check the given string is palindrome or not.

num=(input("Enter the word: "))

rev=num[::-1]

if num==rev:
    print("It is a palindrome.")
else:
    print("It is not a  palindrome.")
