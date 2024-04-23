def media():
    nota1 = float(input('\nDigite a Primeira Nota: '))
    nota2 = float(input('Digite a Segunda Nota: '))
    nota3 = float(input('Digite a Terceira Nota: '))

    soma = (nota1 + nota2 + nota3) / 3

    if soma < 7.0:
        print(f'\nSua Média foi de {soma} e você foi REPROVADO !')
    elif soma >= 7.0:
        print(f'\nSua Média foi de {soma} e você foi APROVADO !')

media()


#------------------------------------------------------- OUTRA FORMA DE RESOLUÇÃO UTILIZANDO PARAMETROS E ATRIBUINDO VALORES -----------------------------------------------------------------------------------------------------


def media(med1, med2, med3):
    mediafinal = (med1 + med2 + med3) / 3

    if mediafinal < 7:
        return f'\nSua Média foi de {mediafinal} e você foi REPROVADO !'
    return f'\nSua Média foi de {mediafinal} e você foi APROVADO !'

print(media(5, 7, 10))