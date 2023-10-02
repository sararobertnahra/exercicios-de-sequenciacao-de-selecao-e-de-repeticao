#Em uma eleição presidencial existem 4 candidatos, sendo 1, 2, 3, 4 = voto para os respectivos candidatos. 5 = voto nulo; 6 = voto em branco. Elabore um algoritmo que calcula e escreva o total de votos de caad um e o percentual sobre o total.

candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulo = 0
branco = 0
i = 0
voto = [1, 2, 3, 4, 1, 1, 2, 5, 6]

while i<=len(voto)-1:
    if voto[i] == 1:
        candidato1+=1
    if voto[i] == 2:
        candidato2+=1
    if voto[i] == 3:
        candidato3+=1
    if voto[i] == 4:
        candidato4+=1
    if voto[i] == 5:
        nulo+=1
    if voto[i] == 6:
        branco+=1
    i+=1
print(candidato1, float(candidato1/(len(voto))*100))
print(candidato2, candidato2/(len(voto))*100)
print(candidato3, candidato3/(len(voto))*100)
print(candidato4, candidato4/(len(voto))*100)
print(nulo, nulo/(len(voto))*100)
print(branco, branco/(len(voto))*100)