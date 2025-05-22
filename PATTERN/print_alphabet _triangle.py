#Print alphabet triangle like,
#A 
#A B 
#A B C 
#A B C D 
#A B C D E 

#Solution:
rows = 5
for i in range(rows):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()
