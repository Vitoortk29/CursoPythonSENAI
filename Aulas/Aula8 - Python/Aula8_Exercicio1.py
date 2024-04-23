
#Vamos criar uma lista de números e vamos percorrer toda ela adicionando um a cada um dos valores da lista.

numeros = [1, 5, 6, 2, 7, -2, -5]
numerosAdicionados = []

for numero in numeros:
    numero += 1
    numerosAdicionados.append(numero)
print(numerosAdicionados)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Criar um laço que imprima valores de 0 a 10 (range).


for index in range(11):
    print(index)


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Criar uma lista de frutas e imprimir o índice e seu valor(enumerate)


frutas = ['Melancia', 'Uva', 'Abacate', 'Laranja', 'Melão']

for index, valor in enumerate(frutas):
    print(f'\nO indice {index} tem valor {valor}')


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------