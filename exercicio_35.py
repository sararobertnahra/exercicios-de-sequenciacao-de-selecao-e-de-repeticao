#Em um prédio há três elevadores denominados A, B e C. Para otimizar o sistema de controle dos elevadores foi realizado um levantamento no qual cada usuário respondia: - o elevador que utilizava com mais frequencia; - o período em que utilizava o elevador, entre 'M' = matutino, 'V' = vespertino, 'N' = noturno. Construa um algoritmo que calcule e imprima: - qual o elevador mais frequentado e em que periodo  se concentra o maior fluxo; - qual o período mais usado de todos e a que elevador pertence; - qual a diferença porcentual entre o mais usado dos horários e o menos usado; qual a porcentagem sobre o total de serviços prestados do elevador de média utilização.

# Inicializando variáveis
total_usuarios = int(input("Informe o número total de usuários: "))
servicos_elevador_A = 0
servicos_elevador_B = 0
servicos_elevador_C = 0
periodo_m = 0
periodo_v = 0
periodo_n = 0

# Loop para coletar informações dos usuários
i = 0
while i < total_usuarios:
    elevador = input(f"Informe o elevador mais utilizado pelo usuário {i+1} (A/B/C): ")
    periodo = input(f"Informe o período de uso para o usuário {i+1} (M/V/N): ")

    if elevador == 'A':
        servicos_elevador_A += 1
    elif elevador == 'B':
        servicos_elevador_B += 1
    elif elevador == 'C':
        servicos_elevador_C += 1
    else:
        print("Elevador inválido. Use A, B ou C.")
        continue

    if periodo == 'M':
        periodo_m += 1
    elif periodo == 'V':
        periodo_v += 1
    elif periodo == 'N':
        periodo_n += 1
    else:
        print("Período inválido. Use M, V ou N.")
        continue

    i += 1

# a) Elevador mais frequentado e período com maior fluxo
mais_frequentado = max(servicos_elevador_A, servicos_elevador_B, servicos_elevador_C)
if mais_frequentado == servicos_elevador_A:
    elevador_mais_frequentado = 'A'
elif mais_frequentado == servicos_elevador_B:
    elevador_mais_frequentado = 'B'
else:
    elevador_mais_frequentado = 'C'

periodo_mais_fluxo = max(periodo_m, periodo_v, periodo_n)
if periodo_mais_fluxo == periodo_m:
    periodo_mais_fluxo_descricao = 'Matutino'
elif periodo_mais_fluxo == periodo_v:
    periodo_mais_fluxo_descricao = 'Vespertino'
else:
    periodo_mais_fluxo_descricao = 'Noturno'

# b) Período mais usado de todos e a que elevador pertence
periodo_mais_usado = max(periodo_m, periodo_v, periodo_n)
if periodo_mais_usado == periodo_m:
    elevador_periodo_mais_usado = elevador_mais_frequentado
    periodo_mais_usado_descricao = 'Matutino'
elif periodo_mais_usado == periodo_v:
    elevador_periodo_mais_usado = elevador_mais_frequentado
    periodo_mais_usado_descricao = 'Vespertino'
else:
    elevador_periodo_mais_usado = elevador_mais_frequentado
    periodo_mais_usado_descricao = 'Noturno'

# c) Diferença percentual entre o mais usado dos horários e o menos usado
min_periodo = min(periodo_m, periodo_v, periodo_n)
diferenca_percentual = ((periodo_mais_usado - min_periodo) / min_periodo) * 100

# d) Porcentagem sobre o total de serviços prestados do elevador de média utilização
total_servicos = servicos_elevador_A + servicos_elevador_B + servicos_elevador_C
if elevador_periodo_mais_usado == 'A':
    porcentagem_elevador_medio = (servicos_elevador_A / total_servicos) * 100
elif elevador_periodo_mais_usado == 'B':
    porcentagem_elevador_medio = (servicos_elevador_B / total_servicos) * 100
else:
    porcentagem_elevador_medio = (servicos_elevador_C / total_servicos) * 100

# Impressão dos resultados
print(f"Elevador mais frequentado: {elevador_mais_frequentado}")
print(f"Período com maior fluxo: {periodo_mais_fluxo_descricao}")
print(f"Período mais usado de todos: {periodo_mais_usado_descricao} (pertence ao elevador {elevador_periodo_mais_usado})")
print(f"Diferença percentual entre o mais usado e menos usado: {diferenca_percentual:.2f}%")
print(f"Porcentagem sobre o total de serviços prestados do elevador médio: {porcentagem_elevador_medio:.2f}%")
