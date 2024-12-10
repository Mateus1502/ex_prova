'''vetor =[]
soma=0
for i in range(1,101):
    vetor.append(i)   
soma=sum(vetor)
media=soma/len(vetor)
maior=max(vetor)
menor=min(vetor)
print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")'''

vetor =[]
soma=0
for i in range(1,101):
    vetor.append(i)
maior=vetor[0]
menor=vetor[0]
for numero in vetor:
    soma += numero
    if numero <  menor:
        menor =numero
    if numero > maior:
        maior = numero
media=soma/len(vetor)
print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")