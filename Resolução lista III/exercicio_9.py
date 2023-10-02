n = int(input("Digite um número: "))
fator = 2

while n != 1:
    mult = 0
    while n%fator == 0:
        n = n/fator
        mult += 1
    if mult != 0:
        print(f"fator {fator} multiplicidade {mult}")
    fator += 1