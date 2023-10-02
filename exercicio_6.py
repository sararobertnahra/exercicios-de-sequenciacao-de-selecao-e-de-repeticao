#Um dado comerciante maluco cobra 10% de acréscimo para cada prestação em atraso e depois dá um desconto de 10% sobre esse valor. Faça um algoritmo que solicite o valor da prestação em atraso e apresente o valor final a pagar, assim como o prejuízo do comerciante na operação.

prest_atraso = float(input("Digite o valor da prestação em atraso: "))

cobra = prest_atraso + prest_atraso*0.1

total = cobra - cobra*0.1

prejuizo = prest_atraso - total

print(f"O valor final a pagar é de {total} e o prejuízo foi de {prejuizo}")