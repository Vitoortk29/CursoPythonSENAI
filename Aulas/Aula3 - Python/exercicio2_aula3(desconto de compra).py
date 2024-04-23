#---------------------------------------Desconto de Compra-------------------------------------------------------

valor_compra = float(input('Qual o valor da compra: '))

if valor_compra >= 200 and valor_compra < 500:
    print(f'Você recebeu um desconto de {(valor_compra * 15) / 100} , referente a 15% !')
elif valor_compra >= 500:
    print(f'Você recebeu um desconto de {(valor_compra * 25) / 100} , referente a 25% !')
else:
    print('Valores menores que R$ 200,00 não aplicamos desconto !')