#Ao completar o tanque de combustível de um automóvel, faça um algoritmo que calcule o consumo efetuado, assim como a autonomia que o carro ainda teria antes do abastecimento. Considere que o veículo sempre seja abastecido até encher o tanque e que são fornecidas apenas a capacidade do tanque, a quantidade de litros abastecidos e a quilometragem percorrida desde o último abastecimento.

capacidade_tanque = float(input("Digite a capacidade do tanque: "))
quantidade_litros = float(input("Digite a quantidade de litros abastecido: "))
quilometros_percorridos = float(input("Digite a quilometragem percorrida: "))

consumo = quilometros_percorridos/quantidade_litros

autonomia = (capacidade_tanque - quantidade_litros)*consumo

print(f"O consumo efetuado foi {consumo} e a autonomia é {autonomia}")