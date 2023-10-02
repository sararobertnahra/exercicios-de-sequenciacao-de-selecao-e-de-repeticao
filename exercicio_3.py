#Prepare um algoritmo capaz de inverter um número, de 3 dígitos, fornecido, ou seja, apresentar primeiro a unidade e, depois, a dezena e centena.

num = int(input("Entre com um número de 3 dígitos: "))

a = num//100
b = (num%100)//10
c = num%10

num_invertido = c*100 + b*10 + a

print(f"O número invertido é: {num_invertido}")