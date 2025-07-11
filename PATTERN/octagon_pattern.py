#Display octagon of stars:

#  **
# *  *
#*    *
#*    *
# *  *
#  **


size = 2
for i in range(size):
    stars = "*" * (size + 2 * i)
    if i != 0:
        stars = "*" + " " * (len(stars)-2) + "*"
    print(" " * (size - i) + stars)

for i in range(size):
    print("*" + " " * (size*3 - 2) + "*")

for i in range(size-1, -1, -1):
    stars = "*" * (size + 2 * i)
    if i != 0:
        stars = "*" + " " * (len(stars)-2) + "*"
    print(" " * (size - i) + stars)
