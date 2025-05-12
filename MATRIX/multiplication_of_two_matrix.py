#Multplication of the given matrixs(A*B)

A=[[2,3],
   [5,7]]
B=[[1,7],
   [7,3]]
result=[[0,0],
        [0,0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
         result[i][j]+=A[i][k]*B[k][j]
print("Result: ")
for row in result:
    print(row)
