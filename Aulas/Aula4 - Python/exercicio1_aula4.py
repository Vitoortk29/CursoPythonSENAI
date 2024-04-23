import math

def somaDoisNumeros():
    numero1 = float(input('Digite o primeiro Número da Soma: '))
    numero2 = float(input('Digite o segundo Número da Soma : '))
    soma = numero1 + numero2
    return soma

def subtraiDoisNumeros():
    numero1 = float(input('Digite o primeiro Número da Subtração: '))
    numero2 = float(input('Digite o segundo Número da Subtração : '))
    sub = numero1 + numero2
    return sub

def potencia():
    soma = somaDoisNumeros()
    sub = subtraiDoisNumeros()

    potenciacao = (soma ** sub) * math.pi
    return potenciacao
print(potencia())