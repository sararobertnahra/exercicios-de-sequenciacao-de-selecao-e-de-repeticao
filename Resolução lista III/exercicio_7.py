conta = int(input("Digite o valor da conta a ser paga: "))
pagamento = int(input("Digite o valor dado: "))

valor = pagamento - conta

notas = [50, 20, 10, 5, 2, 1]
troco = []
resto = valor
i = 0
while i < len(notas)-1:
    quantidade, resto = divmod(resto, notas[i])
    troco.append({"nota": notas[i], "quantidade": quantidade})
    i=i+1

print(troco)


# def calcular_troco(valor):
#     notas = [50, 20, 10, 5, 2, 1]
#     troco = []
#     resto = valor
#     for _, nota in enumerate(notas):
#         quantidade, resto = divmod(resto, nota)
#         troco.append({"nota":nota, "quantidade":quantidade})
#     return troco

# print(calcular_troco(121))