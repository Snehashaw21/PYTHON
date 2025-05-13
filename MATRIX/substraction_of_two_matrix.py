#Substraction of two matrix

A=[[9,5,3],
   [7,4,1],
   [8,3,0]]
B=[[2,7,4],
   [3,6,9],
   [9,0,6]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j]=A[i][j]-B[i][j]
for r in result:
    print(r)
