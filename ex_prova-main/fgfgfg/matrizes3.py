#A + B
A =[
    [-10,1,4,6],
    [2,3,2,8]
]
B=[
    [1,8,4,-1],
    [0,6,3,-3]
]
C=[]
for i in range (len (A)):
    linha = []
    for j in range(len(A[0])):
        linha.append(A[i][j]+ B[i][j])
    C.append(linha)
print(C)   