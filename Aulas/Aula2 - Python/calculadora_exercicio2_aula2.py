# ---------------------------- CALCULADORA ----------------------------------------------
    
try:
    num1 = float(input('Digite o primeiro Número: '))
    num2 = float(input('Digite o segundo Número:'))
    opera = input('Digite um operador: ')

    if opera == "+":
        print(f"O valor da Soma é {num1 + num2}")

    elif opera == "-":
        print(f"O valor da Subtração é {num1 - num2}")

    elif opera == "*":
        print(f"O valor da Multiplicação é {num1 * num2}")

    elif opera == "/":
        if num2 != 0:
            div = num1 / num2
            print(f'Divisão: {div}')
        else:
            print('Divisão por zero não é possivel')
    else:
        print("Você digitou um caracter não valido neste campo !")
        
    # except Exception as e:        
    # print(f'oi{type(e).__name__}')     ## ESTA LINHA E A DE CIMA É UTILIZADO PARA ENCONTRAR O TIPO DE ERRO. EM SEGUIDA ADERIR A CONDIÇÃO ABAIXO

except ValueError:
    print('Não é possivel digitar letras neste campo !')
