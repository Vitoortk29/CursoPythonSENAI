#   Quando queremos adicionar algum número em uma lista podemos utilizar o comando abaixo(append).
numeros = [1, 2, 3]
numerosAdicionar = 5
numeros.append(numerosAdicionar)
print(numeros)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#   Quando queremos adicionar uma lista dentro de outra lista podemos utilizar o comando abaixo(extend).
valores = [1, 2, 3]
outros = [3, 5, 6]
valores.extend(outros)
print(valores)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#   Quando queremos adicionar um número em uma lista em um determinado lugar utilizamos o comando abaixo(insert e entre parenteses o numero da posição e a variavel com o numero que queremos adicionar)
valores = [2, 5, 6]
numero = 4
valores.insert(1, numero)
print(valores)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#   Quando queremos remover algum número dentro de uma lista usamos o comando abaixo(remove e entre parenteses o numero que queremos remover).
valores = [5, 7, 1, 10, 5, 6, 1]
valores.remove(1)
print(valores)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#   Quando queremos remover algum número de uma lista porém com a posição utilizamos o comando abaixo (pop e entre parenteses a posição do número que queremos remover da lista)
valores = [5, 7, 1, 10, 5, 6, 1]
valores.pop(4)
print(valores)
#----------------------------------------------- MAIS UMA OPÇÃO -------------------------------------------------------
valor = valores.pop(1)
print(valor, valores)

#   

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#   Quando queremos saber em qual posição um determinado número usamos o comando abaixo(index e entre parentes o numero que queremos saber a posição)
valores = [5, 7, 1, 10, 5, 6, 10]
indice = valores.index(10)
print(indice)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#   Quando queremos saber quantas vezes quantas vezes um determinado numero aparece em uma lista usamos o comando abaixo(index e entre parentes o numero que queremos saber)
valores = [5, 7, 1, 10, 5, 6, 10]
contagem = valores.count(10)
print(contagem)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#   Quando queremos colocar os numeros de uma lista em ordem numerica do menor para o maior usamos o comando abaixo.
valores = [5, 6, 4, 1, 7, 8]
valores.sort()
print(valores)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#   Quando queremos colocar os numeros de uma lista em ordem numerica do maior para o menor usamos o comando abaixo.
valores = [5, 6, 4, 1, 7, 8]
valores.reverse()
print(valores)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#   Quando queremos copia uma lista usamos o comando abaixo.
valores = [5, 6, 4, 1, 7, 8]
copia = valores.copy()
print(copia)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#   Quando queremos limpar uma lista utilizamos os comandos abaixo.
valores = [5, 6, 4, 1, 7, 8]
valores.clear()
print(valores)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------