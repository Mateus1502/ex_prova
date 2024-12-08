#Faça um programa que leia um vetor com N elementos formados por valores do tipo inteiro. Crie então dois novos vetores, um com os valores pares e outro com os valores ímpares do vetor original
user=int(input("Informe o tamanho do vetor:"))
vet1=[]
pares=[]
impares=[]
for i in range(user):
    vet1.append(i)
for i in vet1:
    if i %2==0:
        pares.append(i)
    else:
        impares.append(i)
print(pares)
print(impares)