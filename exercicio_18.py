#Construa um algoritmo que, dado um conjunto de valores inteiros e positivos, determine qual o menor e o maior valor do conjunto. O final do conjunto de valores é conhecido pelo valor -1, que não deve ser considerado.

import math


a = [28, 2, 4, 10, 17, 21, 30]
i = 0
minimo = math.inf
maximo = -math.inf
while i < len(a):
    if a[i] < minimo:
        minimo = a[i]
    if a[i] > maximo:
        maximo = a[i]
    i+=1

print(minimo)
print(maximo)