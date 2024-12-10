#Função que verifica se um número é par
def par(a):
    if a %2 ==0:
        return True
    else:
        return False
a=int(input('Informe o número: '))
é_par=par(a)
if é_par(a):
    print('Esse número é par')
else:
    print("O número é ímpar")
