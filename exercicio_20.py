#Uma rainha paga o monge com grãos dispostos em um tabuleiro de xadrez, de tal forma que o primeiro quadro contivesse apenas um grão e os quadros subsequentes, o dobro do quadro anterior. Faça um algoritmo para calcular o número de grãos que o monge esperava receber.

quadro = 1
pagamento = 0
while quadro <= 64:
    moedas = 2 ** (quadro-1)
    pagamento+=moedas
    quadro+=1
print(pagamento)