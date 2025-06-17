#Finbing the greatest number using function


def greater():
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        print(c)

a=int(input("Enter the number: "))
b=int(input("Enter the number: "))
c=int(input("Enter the number: "))
print(f"{greater()} is the greater number.")
