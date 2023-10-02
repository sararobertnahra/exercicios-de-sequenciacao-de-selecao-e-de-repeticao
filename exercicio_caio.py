a = range(1, 20)
i = 0
par = []
impar = []

while i <= len(a)-1:
    if a[i]%2 == 0:
        par.append(a[i])
    else: 
        impar.append(a[i])
    i+=1
print(par)
print(impar)