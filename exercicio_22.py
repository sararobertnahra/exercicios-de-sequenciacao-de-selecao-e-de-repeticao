#Escreva um algoritmo que imprima todas as possibilidades de que no lançamento de dois dados tenhamos o valor 7 como resultado da soma dos valores de cada dado.

possibilidade = 0

dado1 = [1, 2, 3, 4, 5, 6]
dado2 = [1, 2, 3, 4, 5, 6]

i = 0
while i < 6:
    j = 0
    while j < 6:
        if dado1[i] + dado2[j] == 7:
            possibilidade += 1
        j += 1
    i += 1

print(possibilidade)
