def primo(a):
    if a <2:
        return False
    for i in range(2,a):
        if a % i== 0:
            return False
    return True
a=int(input("Informe um numero:"))
é_primo=primo(a)
if é_primo:
    print(f"O número {a} é primo")
else:
    print(f"O número {a} não é primo")