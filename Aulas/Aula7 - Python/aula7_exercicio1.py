def imprimiPar():
    contador = 0
    while contador <= 100:
        if contador % 2 == 0:
            print(f'O Número {contador} é par')
        contador += 1
print(imprimiPar())