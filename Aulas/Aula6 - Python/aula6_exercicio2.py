def opMatematica ():
    print('1 - Adição +')
    print('2 - Subtração - ')
    print('3 - Multiplicação *')
    print('4 - Divisão /')

    opcao = int(input('\nEscolha umas das opções acima: '))
    num1 = float(input('\nDigite o primeiro Número: '))
    num2 = float(input('\nDigite o segundo Número: '))

    if opcao > 0 and opcao <= 4:
        if opcao == 1:
            soma = num1 + num2
            print(f'\nO resultado da sua Adição é {soma} !')

        elif opcao == 2:
            sub = num1 - num2
            print(f'\nO resultado da sua Subtração é {sub} !')

        if num1 > 0 and num2 > 0:
            if opcao == 3:
                multi = num1 * num2
                print(f'\nO resultado da Multiplicação é {multi} !')
                
            elif opcao == 4:
                div = num1 / num2
                print(f'\nO resultado da Divisão é {div} !')
        else:
            print('Valores precisam ser maiores que zero.')
    else:
        print('Opção inválida!')
        
opMatematica()




#--------------------------------------------------------------- OUTRA FORMA DE RESOLUÇÃO ---------------------------------------------------------------------------------------------


def opMatematica ():
    print('1 - Adição +')
    print('2 - Subtração - ')
    print('3 - Multiplicação *')
    print('4 - Divisão /')

    opcao = int(input('\nEscolha umas das opções acima: '))
    num1 = float(input('\nDigite o primeiro Número: '))
    num2 = float(input('\nDigite o segundo Número: '))

    if opcao > 0 and opcao <= 4:
        if opcao == 1:
            return f'\nA soma entre {num1} + {num2} é {num1 + num2}'
        
        elif opcao == 2:
            return f'\nA subtração entre {num1} - {num2} é {num1 - num2}'
        
        elif num1 > 0 and num2 > 0:
            if opcao == 3:
                return f'\nA multiplicação entre {num1} X {num2} é {num1 * num2}'
            
            else:
                return f'\nA divisão entre {num1} / {num2} é {num1 / num2}'
            
        else:
            return '\nOsvalores precisam ser maiores que zero.'
        
    else:
        return '\nOpção Inválida !'

print(opMatematica())