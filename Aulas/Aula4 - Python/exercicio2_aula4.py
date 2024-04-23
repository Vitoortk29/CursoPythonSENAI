import math

def areaCirculo():
    num1 = float(input('Digite o Raio: '))
    area = math.pi * (num1 ** 2)
    return f'A área do circulo é {area}'

print(areaCirculo())