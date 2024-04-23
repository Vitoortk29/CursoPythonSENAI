def tabuada():
    contador = 0
    
    num = int(input('\nDigite o Número que você deseja saber a tabuada: '))

    while contador <= 10:
        resultado = num * contador
        print(f'{num} X {contador} = {resultado}')
        contador += 1
    return ''    # GANBIARRA PARA TIRAR O NONE KKK
print(tabuada())