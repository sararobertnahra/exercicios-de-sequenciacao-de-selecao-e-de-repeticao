#Realizou- se uma pesquisa para determinar alguns dados estatisticos em relação ao conjunto de crianças nascidas em um certo periodo de uma determinada maternidade. Construa algortimo que leia n° de crianças nascidas desse período, depois, em um número indeterminado de vezes. O sexo de um recém nascido prematuro(M ou F) e o numero de dias que foi mantido na encubadora. Como finalizador, teremos a letra X no lugar do sexo da criança.Determine e imprima: a) Porcentagem de recém- nascidos prematuro. b) A porcentagem de recém-nascidos meninas e meninos do total de prematuro. c) A média de dias de permanência dos recém-nascidos prematuros na encubadora. d) O maior número de dias do recem-nascido prematuro permaneceu na encubadora.

# Inicializando as variáveis
prematuros = 0
meninos_prematuros = 0
meninas_prematuros = 0
total_dias_prematuros = 0
maior_dias = 0

# Coleta de informações sobre as crianças
while True:
    sexo = input("Informe o sexo da criança (M/F ou X para sair): ")

    if sexo == 'X':
        break

    if sexo == 'M' or sexo == 'F':
        dias_encubadora = int(input("Informe o número de dias na encubadora: "))
        
        if dias_encubadora > maior_dias:
            maior_dias = dias_encubadora

        if dias_encubadora > 0:  # Verifica se é prematuro
            prematuros += 1
            total_dias_prematuros += dias_encubadora

            if sexo == 'M':
                meninos_prematuros += 1
            else:
                meninas_prematuros += 1
    else:
        print("Entrada inválida. Use M para menino, F para menina ou X para encerrar.")

# Porcentagem de recém-nascidos prematuros
porcentagem_prematuros = (prematuros / (prematuros + (meninos_prematuros + meninas_prematuros))) * 100

# A porcentagem de recém-nascidos meninas e meninos do total de prematuros
porcentagem_meninos_prematuros = (meninos_prematuros / prematuros) * 100
porcentagem_meninas_prematuros = (meninas_prematuros / prematuros) * 100

# A média de dias de permanência dos recém-nascidos prematuros na encubadora
if prematuros > 0:
    media_dias_prematuros = total_dias_prematuros / prematuros
else:
    media_dias_prematuros = 0

# O maior número de dias que o recém-nascido prematuro permaneceu na encubadora
print(f"\nResultados:")
print(f"Porcentagem de recém-nascidos prematuros: {porcentagem_prematuros:.2f}%")
print(f"Porcentagem de recém-nascidos meninos prematuros: {porcentagem_meninos_prematuros:.2f}%")
print(f"Porcentagem de recém-nascidos meninas prematuras: {porcentagem_meninas_prematuros:.2f}%")
print(f"Média de dias de permanência dos recém-nascidos prematuros na encubadora: {media_dias_prematuros:.2f} dias")
print(f"Maior número de dias que um recém-nascido prematuro permaneceu na encubadora: {maior_dias} dias")
