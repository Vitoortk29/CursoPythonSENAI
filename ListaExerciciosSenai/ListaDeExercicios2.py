#Exercicio 1

def verificaNumeroMaior():
    numeros = []
    maior = 0

    for i in range(3):
        numero =  float(input('\nDigite um Número: '))
        numeros.append(numero)

    if testePositivo(numeros):
        return retornaMaior(numeros, maior)
    
    maior = numeros[0]
    return retornaMaior(numeros, maior)

def testePositivo(valores):
    for valor in valores:
        if valor > 0:
            return True

def retornaMaior(numeros, maior):
    for valor in numeros:
        if valor > maior:
            maior = valor
    return f'\nO Número maior é {maior}'

print(verificaNumeroMaior())


#-------------------------------------------------------------------------  OUTRA FORMA DE RESOLVER   ---------------------------------------------------------------------------------

def verificaNumeroMaior():
    numeros = []

    for i in range(3):
        numero = float(input('Digite um Número: '))
        numeros.append(numero)

        for numero in numeros:
            if numeros[0] <= numero:
                maior = numero
    return f'\nO Número maior é {maior}'
print(verificaNumeroMaior())


#-------------------------------------------------------------------------  OUTRA FORMA DE RESOLVER   ---------------------------------------------------------------------------------

def verificaNumero():
    numeros = []

    for i in range(3):
        numero = float(input('Digite um Número: '))
        numeros.append(numero)

    print(f'\nO valor Maior digita foi: {max(numeros)}')
    return ''
print(verificaNumero())


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Exercico 5


def verificaIdade():
    quantidade = 0
    maioresDeIdade = 0
    menoresDeIdade = 0

    while quantidade == 0:
        idade = int(input('Digite a Idade: '))

        if idade >= 18:
            maioresDeIdade += 1
        else:
            menoresDeIdade += 1

        opcao = int(input('Deseja verificar outra idade? 1-Sim 2-Não: '))

        if opcao == 2:
            quantidade += 1
    return f'\nMaiores de Idade: {maioresDeIdade}. \nMenores de idade: {menoresDeIdade}.'

print(verificaIdade())