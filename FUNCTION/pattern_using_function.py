# Write a python function to print following style pattern:
#*****
#****
#***
#**
#*


def pattern(n):
    if(n==0):
        return
    print("*"*n)
    pattern(n-1)

pattern(5)
