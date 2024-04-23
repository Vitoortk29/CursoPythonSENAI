# #   Imprimir números pares de 0 a 10.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for index in lista:
    if index % 2 == 0:
        print(f'O Número {index} é par !')

# #OUTRA FORMA DE FAZER O MESMO EXERCICIO 
def imprimiPar():
    for index in range (0, 11, 2):
        print(index)
print(imprimiPar())

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#   Imprimir o quadrado dos números de 1 a 5

for index in range(1, 6):
    soma = index ** 2
    print(soma)

#   OUTRA FORMA DE FAZER O MESMO EXERCICIO
def quadrado():
    for index in range(1, 6):
        print(index ** 2)
print(quadrado())

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#   Calcular a soma dos primeiros cinco números naturais.

soma = 0
for index in range(1, 6):
    soma += index

print("A soma dos primeiros cinco números naturais é:", soma)


#   OUTRA FORMA DE FAZER O MESMO EXERCICIO
def somaNatural():
    soma = 0 
    for index in range(1, 6):
        soma += index
    return soma
print(somaNatural())

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Fazer uma tabuada do 1 ao 10

for i in range(1, 11):
    print(f"Tabuada do {i}:")
    for j in range(1, 11):
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
    print()

#   OUTRA FORMA DE FAZER O MESMO EXERCICIO
def tabuada():
    for numero1 in range(11):
        for nummero2 in range(11):
            print(f'O {numero1} X {nummero2} = {numero1 * nummero2}')
        return ''
print(tabuada())