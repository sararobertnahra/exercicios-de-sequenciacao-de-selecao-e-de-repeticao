#Anacleto tem 1,50 metros e cresce 2 cm por ano, enquanto Felisberto tem 1,10 e cresce 3 cm por ano. Construa um algoritmo que calcule e imprima quantos anos serão necessários para que Felisberto seja maior que Anacleto.
anacleto = 1.50
felisberto = 1.10
i = 0
while felisberto < anacleto:
    anacleto = 1.50 + i*0.02
    felisberto = 1.10 + i*0.03
    i+=1
print(f"{anacleto:.2f} {felisberto:.2f}")
print(i)