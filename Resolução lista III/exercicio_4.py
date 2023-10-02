n = int(input("Digite um número inteiro: "))
a = 1
b = 1
x = 1

while x <= (n-1):
    a, b = b, a+b
    x += 1
print(f"O número de fibonacci é {a}")
