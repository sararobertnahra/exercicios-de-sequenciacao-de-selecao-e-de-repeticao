#Faça um algoritmo que seja capaz de obter o resultado da exponenciação para qualquer base e expoente inteiro fornecidos, sem utilizar a operação de exponenciação (pot).
base = float(input("Digite o valor da base: "))
expoente = float(input("Digite o valor do expoente: "))
resultado = 1

while expoente > 0:
    resultado *= base
    expoente -= 1
print(f"{resultado}")
