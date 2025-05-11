#Add two matrix and print the result

A=[[2,3,4],
   [5,7,1],
   [9,6,0]]
B=[[1,7,0],
   [7,3,1],
   [4,0,1]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j]=A[i][j]+B[i][j]
for r in result:
    print(r)
