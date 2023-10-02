#Construa um algoritmo que leia um conjunto de dados contendo altura e sexo ('M' para masculino e 'F' para feminino) de 50 pessoas e, depois, calcule e escreva: a maior e menor altura do grupo; a média de altura entre as mulheres; o número de homens e a diferença percentual entre eles e as mulheres.

dados =range(1, 50)# Inicialização de variáveis
soma_alturas_mulheres = 0
quantidade_mulheres = 0
maior_altura = 0
menor_altura = float('inf')
numero_homens = 0
contador = 0

# Leitura dos dados
while contador < 50:
    altura = float(input("Digite a altura (em metros): "))
    sexo = input("Digite o sexo (M para masculino, F para feminino): ")

    if sexo == 'F':
        soma_alturas_mulheres += altura
        quantidade_mulheres += 1

    if altura > maior_altura:
        maior_altura = altura

    if altura < menor_altura:
        menor_altura = altura

    if sexo == 'M':
        numero_homens += 1

    contador += 1

# Cálculos finais
media_altura_mulheres = soma_alturas_mulheres / quantidade_mulheres
percentual_diferenca = (abs(numero_homens - (50 - numero_homens)) / 50) * 100

# Impressão dos resultados
print(f"Maior altura: {maior_altura} metros")
print(f"Menor altura: {menor_altura} metros")
print(f"Média de altura das mulheres: {media_altura_mulheres} metros")
print(f"Número de homens: {numero_homens}")
print(f"Diferença percentual entre homens e mulheres: {percentual_diferenca}%")
