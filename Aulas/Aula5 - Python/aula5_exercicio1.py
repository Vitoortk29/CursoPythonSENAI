def parimpar():
    num = int(input('\nDigite um Número: '))

    if num % 2 == 0:
        print(f'\nO Número {num} é Par !')
    else:
        print(f'\nO Número {num} é impar! ')

parimpar()


#--------------------------------------------------------- OUTRA FORMA DE RESOLUÇÃO - DESTA MANEIRA JÁ ATRIBUINDO O VALOR ---------------------------------------------------------------------------------------------------

def parimpar(num):
    if num % 2 == 0:
        return f'O Número{num} é par'
    return f'\nO Número {num} é impar'
print(parimpar(3))