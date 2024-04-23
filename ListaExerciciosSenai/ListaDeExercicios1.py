#Exercicio 1

horas = int(input('Digite qual Horas são: '))


minutos = horas * 60
conversao = float(minutos)

print(f'A conversão da hora que você digitou é {minutos} !')


#----------------------------------------------------------------------------------------------------------------------------------

#Exercico 2

def bolsaTotal():
    bolsa_auxilio = float(input('\nDigite o valor da Bolsa Auxilio: '))
    vale_transporte = float(input('Digite o valor do Vale Transporte: '))
    vale_alimentacao = float(input('Digite o valor do Vale Alimentação: '))
    soma = bolsa_auxilio + vale_transporte + vale_alimentacao
    return soma

print(bolsaTotal())

#----------------------------------------------------------------------------------------------------------------------------------

#Exercicio 3

def trocar_valores(A, B):
    print("\nValores originais:")
    print("A =", A)
    print("B =", B)

    A, B = B, A

    print("\nValores trocados:")
    print("A =", A)
    print("B =", B)

A = 10
B = 20

# Chama a função ↓
trocar_valores(A, B)

#----------------------------------------------------------------------------------------------------------------------------------

#Exercicio 4

def lerNumComp():
    num1 = float(input('\nDigite o primeiro Número: '))
    num2 = float(input('Digite o segundo Número: '))

    if num1 > num2:
        print('\nO primeiro Número digitado é maior que segundo Número digitado !')
    elif num1 < num2:
        print('\nO primeiro Número digitado é menor que o segundo Número digitado !')
    else:
        print('\nO primeiro Número digitado é igual ao segundo Número digitado !')

# Chama a função ↓
lerNumComp()

#----------------------------------------------------------------------------------------------------------------------------------

#Exercicio 5

def menu():
    nummero = float(input('\nDigite um Número: '))
    codigo = int(input('Digite o Código do calculo desejado [101, 102, 103, 104]: '))

    if codigo == 101:
        if nummero % 2 == 0:
            print('Este Número é par !')
        else:
            print('Este Número é impar !')
    elif codigo == 102:
        print(f'A metade de {nummero} é {nummero / 2} !')
    elif codigo == 103:
        print(f'10% de {nummero} é {nummero * 0.1} !')
    elif codigo == 104:
        print(f'O dobro de {nummero} é {nummero *2} !')

# Chama a função ↓
menu()

#----------------------------------------------------------------------------------------------------------------------------------

#Exercicio 6

def bissexto():
    ano = int(input('\nDigite o Ano: '))

    if ano % 4 == 0:
        if ano % 100 != 0 or ano % 400 == 0:
            print('\nEste ano é Bissexto !')
    else:
        print('\nEste ano não é Bissexto !')

# Chama a função ↓
bissexto()

#----------------------------------------------------------------------------------------------------------------------------------

#Exercicio 7

def verificaNumero():
    num = float(input(f'\nDigite um Número: '))

    if num > 0:
        print('\nEste número é Positivo !\n')
    elif num < 0:
        print('\nEste número é Negativo !\n')
    else:
        print('\nEste número é Nulo !\n')


verificaNumero()

#----------------------------------------------------------------------------------------------------------------------------------


#Exercicio 8

def qualNumMaiorOuMenor():
    num1 = float(input('\nDigite o primeiro Número: '))
    num2 = float(input('\nDigite o primeiro Número: '))
    num3 = float(input('\nDigite o primeiro Número: '))

    if num1 >= num2 and num1 >= num3:
        print(f'\nO Número maior é o primeiro ({num1}) !')
    elif num2 >= num1 and num2 >= num3:
        print(f'\nO Número maior é o segundo ({num2}) !')
    else:
        print(f'\nO Número maior é o terceiro ({num3}) !')

# Chama a função ↓
qualNumMaiorOuMenor()