#Construa um algoritmo que seja capaz de concluir qual dentre os seguintes animais foi escolhido, através de perguntas e respostas. Animais possíveis: leão, cavalo, homem, macaco, morcego, baleia, avestruz, pinguim, pato, águia, tartaruga, crocodilo e cobra.

a = int(input("É mamífero? Diga 1 se sim ou 2 se não: "))

if a == 1:
    b = int(input("É quadrúpede? Diga 1 se sim ou 2 se não: "))
    if b == 1:
        c = int(input("É carnívoro? Diga 1 se sim ou 2 se não: "))
        if c == 1:
            print("É leão")
        else: print("É cavalo")
    else:
        d = int(input("É bíbede? Diga 1 se sim ou 2 se não: "))
        if d == 1:
            e = int(input("É onívoro? Diga 1 se sim ou 2 se não: "))
            if e == 1:
                print("É homem")
            else: print("É macaco")
if a == 2:
    g = int(input("É ave? Diga 1 se sim ou 2 se não: "))
    if g == 1:
        h = int(input("É não voador? Diga 1 se sim ou 2 se não: "))
        if h == 1:
            i = int(input("É tropical? Diga 1 se sim ou 2 se não: "))
            if i == 1:
                print("É avestruz")
            else: print("É pinguim")
        else:
            j = int(input("É nadador? Diga 1 se sim ou 2 se não: "))
            if j == 1:
                print("É pato")
            else: print("É águia")
    if g == 2:
        k = int(input("É réptil com caso? Diga 1 se sim ou 2 se não: "))
        if k == 1: 
            print ("É tartaruga")
        elif k == 2:
            l = int(input("É réptil carnívoro? Diga 1 se sim ou 2 se não: "))
            if l == 1:
                print("É crocodilo")
            else: print("É cobra.")
