#Faça um programa que dada a seguinte matriz A, gere a matriz transposta dela At. Matriz transposta é a que se obtém trocando-se ordenadamente as linhas pelas colunas.
a=[
    [-7,8],
    [4,9],
    [2,1]
]
transposta=[]
for j in range(len(a[0])):
    linha=[]
    for i in range (len(a)):
        linha.append(a[i][j])
    transposta.append(linha)
print(transposta)

'''a = [
    [-7, 8],
    [4, 9],
    [2, 1]
]
transposta = []

for j in range(len(a[0])):  # Itera sobre as colunas da matriz original
    linha = []  # Inicializa uma nova linha para a matriz transposta
    for i in range(len(a)):  # Itera sobre as linhas da matriz original
        linha.append(a[i][j])  # Adiciona o elemento da coluna como linha
    transposta.append(linha)  # Adiciona a linha à matriz transposta

# Exibe a matriz transposta
print("Matriz Transposta:")
for linha in transposta:
    print(linha)'''
