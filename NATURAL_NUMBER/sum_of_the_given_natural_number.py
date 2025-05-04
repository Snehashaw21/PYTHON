#Finding the sum of the given natural number 
#Enter the input is 5 so the answer is 1+2+3+4+5
#The output is 15

num=int(input("Enter the number:"))

if num > 0:
    sum = num*(num+1)//2
    print("The sum of given natural number is :", sum)
else:
    print("Please enter the positive number.")
