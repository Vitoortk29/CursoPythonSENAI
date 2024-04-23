def verificaBonus():
    valorVendas = float(input('\nDigite os valor das Vendas: '))
    tempoDeCasa = int(input('\nQuantos anos o funcionário tem de empresa: '))

    if valorVendas > 50000 and tempoDeCasa >= 5:
        bonus =  valorVendas * 0.1
        return f'Bônus de {bonus}'
    return f'O funcionário não possui direito a bônus'
print(verificaBonus())