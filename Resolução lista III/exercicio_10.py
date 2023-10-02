texto = input("Entre com um numero inteiro positvo: ")
resultado = ""
i = len(texto)-1
while i > -1:
    resultado += texto[i]
    i = i - 1
print(resultado)