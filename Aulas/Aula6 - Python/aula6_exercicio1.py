def ladosTriangulos():
    lado1 = int(input('\nDigite o primeiro lado do Triângulo: '))
    lado2 = int(input('\nDiite o segundo lado do Triângulo: '))
    lado3 = int(input('\nDiite o terceiro lado do Triângulo: '))

    if lado1 == lado2 == lado3:
        print('\nEste Triângulo é um Equilátero !')

    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('\nEste Triângulo é um Isósceles !')

    else:
        print('\nEste Triângulo é um Escaleno !')

ladosTriangulos()



#--------------------------------------------------------------- OUTRA FORMA DE RESOLUÇÃO ---------------------------------------------------------------------------------------------


def ladosTriangulos():
    lado1 = int(input('\nDigite o primeiro lado do Triângulo: '))
    lado2 = int(input('\nDiite o segundo lado do Triângulo: '))
    lado3 = int(input('\nDiite o terceiro lado do Triângulo: '))

    if lado1 > 0 and lado2 > 0 and lado3 > 0:
        if lado1 == lado2 and lado2 == lado3:
            return 'O Triângulo é equilátero.'
        elif lado1 ==  lado2 or lado2 == lado3 or lado1 == lado3:
            return 'O Triângulo é isóceles.'
        return 'O Triângulo é escaleno.'
    return 'Os valores precisam ser maiores que zero.'
print(ladosTriangulos())