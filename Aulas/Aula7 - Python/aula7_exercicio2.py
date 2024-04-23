def idade():
    contador = 0
    diMaio = 0

    while contador < 5:
        idade = int(input('Digite a idade: '))

        if idade >= 18:
            diMaio += 1
        contador += 1
    return diMaio
print(idade())

#----------------------------------------------------------------------   OUTRA FORMA DE EXECUÇÃO   ----------------------------------------------------------------------

def idade():
    contador = 0
    diMaio = 0

    while contador < 5:
        idade = int(input('Digite a idade: '))

        while idade <= 0:
             idade = int(input('Digite a idade maior que zero: '))
        if idade >= 18:
            diMaio += 1
        contador += 1
    return diMaio
print(idade())