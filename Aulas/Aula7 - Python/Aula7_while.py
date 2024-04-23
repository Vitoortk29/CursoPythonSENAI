a = [2, 4, 7, 10, 12, 15]

#Chamar a Variavel dentro do print com um número dentro de chaves seleciona a posição do número que você quer selecionar na lista
#Lembrando que as listas sempre começam por 0
print(a[3])

nome = ['Pessoa1', 'Pessoa2', 'Pessoa3', 'Pessoa4']

print(nome[3])

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

valores = [3, 6, 10, 1, 2, -5]

#print(f'O indece 0 tem o valor {valores[0]}')


contador = 0
tamanhoDaLista = len(valores)

while contador < tamanhoDaLista:
    print(f'O indice {contador} tem valor {valores[contador]}')
    contador += 1
