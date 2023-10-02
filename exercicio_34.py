#Um cinema possui capacidade de 100 lugares e está sempre com ocupação total. Certo dia, cada espectador respondeu a um questionário, no qual constava:· sua idade;· sua opinião em relação ao filme, segundo as seguintes notas:
#NOTA       SIGNIFICADO
#A              ÓTIMO
#B              BOM
#C              REGULAR
#D              RUIM
#E              PÉSSIMO  

#Elabore um algoritmo que, lendo estes dados, calcule e imprima:· a quantidade de respostas ótimo;· a diferença percentual entre respostas bom e regular;· a média de idade das pessoas que responderam ruim;· a percentagem de respostas péssimo e a maior idade que utilizou esta opção;· a diferença de idade entre a maior idade que respondeu ótimo e a maior idade que respondeu ruim.

# Inicializando variáveis
total_espectadores = 100
respostas_otimo = 0
respostas_bom = 0
respostas_regular = 0
respostas_ruim = 0
respostas_pessimo = 0
soma_idade_ruim = 0
maior_idade_ruim = -1
maior_idade_otimo = -1

# Loop para coletar informações dos espectadores
i = 0
while i < total_espectadores:
    idade = int(input(f"Informe a idade do espectador {i+1}: "))
    opiniao = input(f"Informe a opinião do espectador {i+1} (A/B/C/D/E): ")

    if opiniao == 'A':
        respostas_otimo += 1
        if idade > maior_idade_otimo:
            maior_idade_otimo = idade
    elif opiniao == 'B':
        respostas_bom += 1
    elif opiniao == 'C':
        respostas_regular += 1
    elif opiniao == 'D':
        respostas_ruim += 1
        soma_idade_ruim += idade
        if idade > maior_idade_ruim:
            maior_idade_ruim = idade
    elif opiniao == 'E':
        respostas_pessimo += 1
        if idade > maior_idade_ruim:
            maior_idade_ruim = idade
    else:
        print("Opinião inválida. Use A, B, C, D ou E.")

    i += 1

# a) Quantidade de respostas "ótimo"
# b) Diferença percentual entre respostas "bom" e "regular"
# c) Média de idade das pessoas que responderam "ruim"
# d) Percentagem de respostas "péssimo" e a maior idade que utilizou esta opção
# e) Diferença de idade entre a maior idade que respondeu "ótimo" e a maior idade que respondeu "ruim"

# a) Quantidade de respostas "ótimo"
print(f"Quantidade de respostas 'ótimo': {respostas_otimo}")

# b) Diferença percentual entre respostas "bom" e "regular"
diferenca_percentual = ((respostas_bom - respostas_regular) / total_espectadores) * 100
print(f"Diferença percentual entre respostas 'bom' e 'regular': {diferenca_percentual:.2f}%")

# c) Média de idade das pessoas que responderam "ruim"
if respostas_ruim > 0:
    media_idade_ruim = soma_idade_ruim / respostas_ruim
else:
    media_idade_ruim = 0
print(f"Média de idade das pessoas que responderam 'ruim': {media_idade_ruim:.2f}")

# d) Percentagem de respostas "péssimo" e a maior idade que utilizou esta opção
percentagem_pessimo = (respostas_pessimo / total_espectadores) * 100
print(f"Percentagem de respostas 'péssimo': {percentagem_pessimo:.2f}%")
print(f"Maior idade que utilizou a opção 'péssimo': {maior_idade_ruim}")

# e) Diferença de idade entre a maior idade que respondeu "ótimo" e a maior idade que respondeu "ruim"
diferenca_idade = maior_idade_otimo - maior_idade_ruim
print(f"Diferença de idade entre a maior idade que respondeu 'ótimo' e 'ruim': {diferenca_idade} anos")
