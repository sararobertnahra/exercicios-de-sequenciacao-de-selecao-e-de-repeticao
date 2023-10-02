#A conversão de graus Fahrenheit para cetígrados é obtida pela fórmula C = 5/9(F-32). Escreva um algoritmo que calcule e escreva uma tabela de graus centígrados em função de graus Fahrenheits que variem de 50 a 150 de I em I.

f = 49
i = 149
while f <= i:
    c = 5/9*(f-32)
    f+=1
    print(f, end=" ")