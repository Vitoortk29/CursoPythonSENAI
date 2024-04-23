numero = float(input('Digite um número entre 0 e 50: '))

if numero >= 0 and numero <= 50:
    if numero % 2 == 0:
        print('O Número é par.')
    else:                    #Nesta linha poderia se usar tbm um elif numero % 2 != 0:
        print('O Número é impar.')
else:
    print('O Número não está no intervalo.')