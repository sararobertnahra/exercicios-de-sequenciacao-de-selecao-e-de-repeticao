N = int(input("Informe o valor inteiro a ser analisado: "))

calculo_triangular = 0

y = 1

while calculo_triangular < N:
    calculo_triangular = y*(y+1)*(y+2)
    y += 1
if calculo_triangular == N:
    print(f"É trinagular.")
else: print(f"Não é triangular.")