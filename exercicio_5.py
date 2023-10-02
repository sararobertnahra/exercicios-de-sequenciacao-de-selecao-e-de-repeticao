#Dada uma determinada data de aniversário (dia, mês e ano separadamente), elabore um algoritmo que solicite a data atual (dia, mês e ano separadamente) e calcule a idade em anos, em meses e em dias.

dia_niver = int(input("Digite o dia do nascimento: "))
mes_niver = int(input("Digite o número do mês do nascimento: "))
ano_niver = int(input("Digite o ano do nascimento: "))
dia_atual = int(input("Digite o dia atual: "))
mes_atual = int(input("Digite o número do mês atual: "))
ano_atual = int(input("Digite o ano atual: "))

idade_anos = ano_atual - ano_niver
idade_meses = mes_atual - mes_niver
idade_dias = dia_atual - dia_niver

print(f"A idade em anos é {idade_anos}, em meses é {idade_anos*12 + idade_meses} e em dias é {idade_anos*365 + idade_meses*30 + idade_dias}")