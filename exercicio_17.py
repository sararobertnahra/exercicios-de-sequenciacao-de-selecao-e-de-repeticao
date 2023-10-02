#Construa um algoritmo que gere os 20 primeiros termos de uma série tal qual a de Fibonacci,as cujos 2 primeiros termos são fornecidos pelo usuário.

a = int(input("Digite o número 1: "))
b = int(input("Digite o número 1 de novo: "))

if a != 1 or b != 1:
    a = int(input("Digite o número 1: "))
    b = int(input("Digite o número 1 de novo: "))

c = 20
i = 0

while i <= c:
    a, b = b, a + b
    i +=1
    print(a, end=" ")
