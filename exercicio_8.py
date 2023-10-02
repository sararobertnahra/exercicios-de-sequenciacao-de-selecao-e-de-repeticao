#Elabore um algoritmo que, a partir de um dia, mês e ano fornecidos, valide se eles compôem uma data válida. Não deixe de considerar os meses com 30 ou 31 dias, e o tratamento de ano bissexto.

ano = int(input("Digite o ano: "))
mes = int(input("Digite o mês: "))
dia = int(input("Digite o dia: "))

if ano < 0:
    print("Ano inálido.")
else: print("Ano válido.")

if (mes < 0 or mes > 13):
    print("Mês inválido.")
else: print("Mês válido.")
if (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    if (dia < 0 or dia > 31):
        print("Dia inválido.")
    else: print("Dia válido.")
if mes == 2:
    if ano%400 == 0 or (ano%4 == 0 and ano%100 != 0):
        if dia < 0 or dia > 29:
            print("Dia inválido.")
        else: print("Dia válido.")
    elif dia < 0 or dia > 30:
        print("Dia inválido.")
    else: print("Dia válido.")
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    if dia < 0 or dia > 32:
        print("Dia inválido.")
    else: print("Dia válido.")