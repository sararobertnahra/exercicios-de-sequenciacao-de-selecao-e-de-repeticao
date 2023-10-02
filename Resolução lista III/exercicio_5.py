a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))
while a != b:
    if a > b:
        a = a - b
    else: b = b - a
n = a
print (f"O máximo divisor comum é {n}")