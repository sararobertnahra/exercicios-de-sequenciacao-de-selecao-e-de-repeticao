#Elabore um algoritmo que imprima todos os números primos existentes entre N1 e N2, que são números naturais fornecidos pelo usuário.

N1 = int(input("Digite um número: "))
N2 = int(input("Digite outro número: "))

if N1 < N2:
    while N1 <= N2:
        i = 1
        mult = 0
        while i <= N1:  
            if N1 % i == 0:
                mult += 1
            i += 1
        if mult == 2:
            print(N1, end=" ")
        N1 += 1
if N2 < N1:
    while N2 <= N1:
        i = 1
        mult = 0
        while i <= N2:  
            if N2 % i == 0:
                mult += 1
            i += 1
        if mult == 2:
            print(N2, end=" ")
        N2 += 1