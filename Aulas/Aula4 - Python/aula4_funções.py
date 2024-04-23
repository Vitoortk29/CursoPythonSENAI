# -------------------------------------Funções-------------------------------------------------------------

#------------------------------------- Exemplo 1 --------------------------------------------------------
    
def somaDoisNumeros():
    numero1 = float(input('Digite o primeiro Número: '))
    numero2 = float(input('Digite o segundo Número: '))
    soma = numero1 + numero2
    return soma

print(somaDoisNumeros())

#------------------------------------- Exemplo 2 --------------------------------------------------------
    
def somaDoisNumerosComParametros(num1, num2):
    soma = num1 + num2
    return soma
numero1 = float(input('Digite o primeiro Número: '))
numero2 = float(input('Digite o segundo Número: '))
print(somaDoisNumerosComParametros(numero1, numero2))

""" Neste dois exemplos de funções !
    As duas executa a mesma coisa 
    Porém uma sem parametros e outa com parametros"""
