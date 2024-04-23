def imprima():
    contador = 0
    while contador >= -200 :
        print(contador)
        contador -= 1
    return ''   # GANBIARRA PARA TIRAR O NONE KKK
print(imprima())


#----------------------------------------------------------------   OUTRA FORMA DE RESOLVER COM LISTA   ------------------------------------------------------------------------------


def imprima():
    contador = 0
    lista = []
    while contador >= -200 :
        lista.append(contador)
        contador -= 1
    print(lista)
    return ''   # GANBIARRA PARA TIRAR O NONE KKK
print(imprima())