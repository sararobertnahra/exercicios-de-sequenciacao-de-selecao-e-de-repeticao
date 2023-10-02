#Construa um algoritmo que seja capaz de dar a classificação olímpica de 3 países informados. Para cada país é informado o nome, a quantidade de medalhas de ouro, prata e bronze. COnsidere que cada medalha de ouro tem peso 3m cada prata tem peso 2 e cada bronze, peso 1.

pais1 = input("Entre com pais 1: ")
quantidade_ouro_pais1 = int(input("Entre com a quantidade de medalhas de ouro do país 1: "))
quantidade_prata_pais1 = int(input("Entre com a quantidade de medalhas de prata do país 1: "))
quantidade_bronze_pais1 = int(input("Entre com a quantidade de medalhas de bronze do país 1: "))

a = (3 * quantidade_ouro_pais1) + (2 * quantidade_prata_pais1) + (1 * quantidade_bronze_pais1)

print(f"Quantidade total de medalhas do {pais1}: {a}")

pais2 = input("Entre com pais 2: ")
quantidade_ouro_pais2 = int(input("Entre com a quantidade de medalhas de ouro do país 2: "))
quantidade_prata_pais2 = int(input("Entre com a quantidade de medalhas de prata do país 2: "))
quantidade_bronze_pais2 = int(input("Entre com a quantidade de medalhas de bronze do país 2: "))

b = (3 * quantidade_ouro_pais2) + (2 * quantidade_prata_pais2) + (1 * quantidade_bronze_pais2)

print(f"Quantidade total de medalhas do {pais2}: {b}")

pais3 = input("Entre com pais 3: ")
quantidade_ouro_pais3 = int(input("Entre com a quantidade de medalhas de ouro do país 3: "))
quantidade_prata_pais3 = int(input("Entre com a quantidade de medalhas de prata do país 3: "))
quantidade_bronze_pais3 = int(input("Entre com a quantidade de medalhas de bronze do país 3: "))

c = (3 * quantidade_ouro_pais3) + (2 * quantidade_prata_pais3) + (1 * quantidade_bronze_pais3)

print(f"Quantidade total de medalhas do {pais3}: {c}")

if a < b and a < c and b < c:
    print(f"Classificação dos países: {pais3}, {pais2}, {pais1}")
elif a < b and a < c and c < b:
    print(f"Classificação dos países: {pais3}, {pais1}, {pais2}")
elif b < a and b < c and a < c:
    print(f"Classificação dos países: {pais2}, {pais3}, {pais1}")
elif b < a and b < c and c < a:
    print(f"Classificação dos países: {pais2}, {pais1}, {pais3}")
elif c < a and c < b and a < b:
     print(f"Classificação dos países: {pais1}, {pais3}, {pais2}")
else:  print(f"Classificação dos países: {pais1}, {pais2}, {pais3}") 