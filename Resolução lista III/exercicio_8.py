numero = int(input("Entre com um numero: "))

mult = 0
i = 0

while i <= numero:

    i += 1
    x = numero%i
    if x == 0:
        mult+=1
        
if mult == 2:
    print("É primo")
else: 
    print("Não é primo")
