#Calculate the sum of first n natural number using recursive function


def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n

print(sum(5))
