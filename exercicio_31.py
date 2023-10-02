#Foi realizada uma pesquisa sobre algumas características físicas da população de uma certa região, a qual coletou os seguintes dados referentes a cada habitante para análise: sexo (M - masculino ou F - feminino), cor dos olhos(A - azuis, V - verdes ou C - castanhos), cor dos cabelos(L - loiros, C - castanhos ou P - pretos), idade. Faça um algoritmo que determine e escreva: a maior idade dos habitantes; a porcentagem entre os individuos do sexo masculino, cuja idade está entre 18 e 35 anos; a porcentagem do total de indivíduos do sexo feminino cuja idade está entre 18 e 35 anos, inclusive, e que tenham olhos verdes e cabelos loiros. O final do conjunto de habitantes é reconhecido pelo valor de -1 entrando como idade.

# Inicializando variáveis
maior_idade = -1
cont_masculino_18_35 = 0
cont_feminino_18_35_verde_loiro = 0
total_habitantes = 0

# Loop para coletar informações dos habitantes
while True:
    sexo = input("Informe o sexo (M/F) do habitante: ")

    cor_olhos = input("Informe a cor dos olhos (A - azuis, V - verdes, C - castanhos): ")
    cor_cabelos = input("Informe a cor dos cabelos (L - loiros, C - castanhos, P - pretos): ")
    idade = int(input("Informe a idade do habitante (ou -1 para encerrar): "))

    # Verificando maior idade
    if idade > maior_idade:
        maior_idade = idade

    # Verificando porcentagem de homens entre 18 e 35 anos
    if sexo == 'M' and 18 <= idade <= 35:
        cont_masculino_18_35 += 1

    # Verificando porcentagem de mulheres entre 18 e 35 anos com olhos verdes e cabelos loiros
    if sexo == 'F' and 18 <= idade <= 35 and cor_olhos == 'V' and cor_cabelos == 'L':
        cont_feminino_18_35_verde_loiro += 1

    total_habitantes += 1

# Calculando as porcentagens
porcentagem_masculino_18_35 = (cont_masculino_18_35 / total_habitantes) * 100
porcentagem_feminino_18_35_verde_loiro = (cont_feminino_18_35_verde_loiro / total_habitantes) * 100

# Imprimindo os resultados
print(f"A maior idade dos habitantes é: {maior_idade} anos")
print(f"Porcentagem de homens entre 18 e 35 anos: {porcentagem_masculino_18_35:.2f}%")
print(f"Porcentagem de mulheres entre 18 e 35 anos com olhos verdes e cabelos loiros: {porcentagem_feminino_18_35_verde_loiro:.2f}%")
