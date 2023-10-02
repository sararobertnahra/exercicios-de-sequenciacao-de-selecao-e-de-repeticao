a = 80000
b = 200000
n = 0

while a <= b:
    a += a*0.03
    b += b*0.015
    n += 1

print (f"O país A ultrapassa o país B em {n} anos.")