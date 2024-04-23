#   Exemplo de laço de repetição com for que percorre uma lista e exige a lista no print.
numeros = [1, 5, 6, 2, 8, 9]

for apresentar in numeros:
    print(apresentar)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#   Exemplo de laço de repetição com for que percorre a lista por 10 vezes pedido pela função range(10).
for index in range(10):
    print(index)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#   Exemplo de laço de repetição com for que chama uma função.
def soma(num1 , num2):
    total = num1 + num2
    return total

for index in range(5):
    print(soma(5, 6))


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#   Exemplo de laço de repetição com for que percorre a lista mostra a posição(index) e mostra o valor(valor)
numeros = [1, 5, 6, 2, 8, 9]

for index, valor in enumerate(numeros):
    print(f'\nO índice {index} tem valor {valor}')


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#   Exemplo de laço de repetição que percorre a lista e inicia em uma determinada posição e finaliza em outra determinada posição utilizando a função range(2, 10)
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for index in range(2, 11):
    print(index)


    
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------