#Construa um algoritmo que calcule a média ponderada entre 5 números quaisquer, sendo que os pesos a serem aplicados são 1, 2, 3, 4 e 5, respectivamente.

a = float(input("Digite o 1° número: "))

b = float(input("Digite o 2° número: "))

c = float(input("Digite o 3° número: "))

d = float(input("Digite o 4° número: "))

e = float(input("Digite o 5° número: "))

media = (a*1 + b*2 + c*3 + d*4 + e*5)/(1+2+3+4+5)

print(f"A média é {media}")