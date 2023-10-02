#Uma agência de publicidade quer prestar serviços somente para as maiores companhias - em número de funcionários - em cada uma das classificações: grande, média, pequena e microempresa. Para tal, consegue um conjunto de dados com o código, o número de funcionários e o porte da empresa. Construa um algoritmo que liste o código da empresa com maiores recursos humanos dentro da sua categoria. Utiliza como finalizador o código de empresa igual a 0.

# Supondo que empresas seja uma lista de tuplas (codigo, num_funcionarios, porte)
empresas = [(1, 500, 'grande'), (2, 200, 'media'), (3, 50, 'pequena'), (4, 10, 'micro')]

# Inicializando variáveis para armazenar as maiores empresas de cada categoria
maior_grande = maior_media = maior_pequena = maior_micro = None

# Inicializando variáveis para armazenar os códigos das maiores empresas
codigo_maior_grande = codigo_maior_media = codigo_maior_pequena = codigo_maior_micro = 0

# Loop para percorrer a lista de empresas
i = 0
while i < len(empresas):
    codigo, num_funcionarios, porte = empresas[i]

    # Verifica se é uma grande empresa
    if porte == 'grande' and (maior_grande is None or num_funcionarios > maior_grande):
        maior_grande = num_funcionarios
        codigo_maior_grande = codigo
    
    # Verifica se é uma média empresa
    elif porte == 'media' and (maior_media is None or num_funcionarios > maior_media):
        maior_media = num_funcionarios
        codigo_maior_media = codigo
    
    # Verifica se é uma pequena empresa
    elif porte == 'pequena' and (maior_pequena is None or num_funcionarios > maior_pequena):
        maior_pequena = num_funcionarios
        codigo_maior_pequena = codigo
    
    # Verifica se é uma microempresa
    elif porte == 'micro' and (maior_micro is None or num_funcionarios > maior_micro):
        maior_micro = num_funcionarios
        codigo_maior_micro = codigo
    
    i += 1

# Imprime os códigos das maiores empresas de cada categoria
print(f"Código da maior empresa grande: {codigo_maior_grande}")
print(f"Código da maior empresa média: {codigo_maior_media}")
print(f"Código da maior empresa pequena: {codigo_maior_pequena}")
print(f"Código da maior microempresa: {codigo_maior_micro}")

