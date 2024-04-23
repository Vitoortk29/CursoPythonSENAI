def celsiusFah():
    celsius = float(input('\nDigite o grau Celsius: '))
    fahrenheit = (celsius * 1.8) + 32
    return f'O valor convertido de Celsius para fahrenheit é {fahrenheit}' 

print(celsiusFah())

def fahrenheit():
    Fahrenheit = float(input('\nDigite o grau em Fahrenheit: '))
    celsius = (Fahrenheit - 32) / 1.8
    return f'O valor de fahrenheit para Celsius é {celsius}'

print(fahrenheit())

#-----------------------------------      CONTINUAÇÃO DO EXERCICIO QUE ESTÁ NA PAGINA 19 DO SLIDE      -----------------------------------------
def escolheConversao():
    print('1 - Converter Celsius em Fahrenheit')
    print('2 - Converter Fahrenheit em Celsius')
    print('3 - Sair')

    try:
        opcao = int(input('\nEscolha uma das opções acimas: '))

        if opcao > 0 and opcao <= 3:
            if opcao == 1:
                return celsiusFah()
            elif opcao == 2:
                return fahrenheit()
            else:
                return '\nObrigado pela Visita!'
        else:
            return 'Opção inválida'
    # except Exception as e:                                        ESTA LINHA E A LINHA DE BAIXO SÃO USADAS PARA DESCOBRIR O ERRO APOS DESCOBRIR USAO EXCEPT ABAIXO |
    #     print(f'A exceção é {type(e).__name__}')                                                                                                                   |
    except ValueError:                                      # <------------------------------------------------------------------------------------------------------|
        print('\nNão é possivel digitar Letras neste campo !')
print(escolheConversao())