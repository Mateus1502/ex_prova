#matriz oposta
A=[
    [2,-3],
    [-1,4]

]
B=[]
for i in range (len (A)):
    linha = []
    for j in range(len(A[0])):
        linha.append(- A[i][j])
    B.append(linha)
print(B)
