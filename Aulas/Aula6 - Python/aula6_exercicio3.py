def verifica():
    print('')
    print('\nVamos fazer alguma Verificações ! ')
    print('\n1º - Se o Número digitado é Par e Multiplo de 3 ! ')
    print('2º - Se o Número digitado é Impar e Multiplo de 3 ! ')
    
    num = float(input(f'\nDigite um Número: '))

    if num % 2 == 0 and num % 3 == 0:
        print(f'\nO {num} é par e divisivel por 3 !')

    elif num % 2 != 0 and num % 3 == 0:
        print(f'\nO {num} é impar e divisivel por 3 !')
    
    else:
        print(f'O {num} NÃO ATENDE OS CRITERIOS !')

verifica()



#--------------------------------------------------------------- OUTRA FORMA DE RESOLUÇÃO ---------------------------------------------------------------------------------------------


def verifica():
    num = float(input('\nDigite um número: '))

    if num % 2 == 0 and num % 3 == 0 :
        return f'\nO número {num} é par e múltiplo de três.'
    
    elif num % 2 != 0 and num % 3 == 0 :
        return f'\nO número {num} é impar e múltiplo de três.'
    
    return '\nO número não atende os parâmetros.'

print(verifica())