#Calcule o imposto de renda de um grupo de 10 contribuintes, considerando que os dados de cada contribuinte, número de CPF, número de dependentes e renda mensal são valores fornecidos pelo usuário. Para cada contribuinte será feito um desconto de 5% do salário mínimo por dependente.

# Definindo as faixas de imposto
faixas_imposto = [
    (1045 * 2, 0),      # Até 2 salários mínimos é isento
    (1045 * 3, 0.05),   # De 2 a 3 salários mínimos: 5%
    (1045 * 5, 0.10),   # De 3 a 5 salários mínimos: 10%
    (1045 * 7, 0.15),   # De 5 a 7 salários mínimos: 15%
    (float('inf'), 0.20)  # Acima de 7 salários mínimos: 20%
]

# Inicializando uma lista para armazenar os resultados
resultados = []

# Loop para coletar informações dos contribuintes
i = 0
while i < 10:
    cpf = input(f"Informe o CPF do contribuinte {i+1}: ")
    dependentes = int(input(f"Informe o número de dependentes do contribuinte {i+1}: "))
    renda_mensal = float(input(f"Informe a renda mensal do contribuinte {i+1} (em reais): "))

    # Calculando o desconto por dependente
    desconto_dependentes = 0.05 * 1045 * dependentes

    # Calculando a renda tributável
    renda_tributavel = renda_mensal - desconto_dependentes

    # Calculando o imposto de renda
    imposto = 0
    for faixa, taxa in faixas_imposto:
        if renda_tributavel <= faixa:
            imposto = taxa * renda_tributavel
            break

    # Adicionando o resultado à lista de resultados
    resultados.append((cpf, imposto))

    i += 1

# Imprimindo os resultados
print("\nResultados:")
for cpf, imposto in resultados:
    print(f"CPF: {cpf} - Imposto de Renda: R$ {imposto:.2f}")
