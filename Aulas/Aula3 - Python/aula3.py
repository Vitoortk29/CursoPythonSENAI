# and = e
# or = ou
#not = Não (Inversão)


a = 6
b = 1
c = 10

# ---------------------------------------Exemplo de and----------------------------------------------------------------

if a> b and a > c:
    print('Entrou no if')
else:
    print('Não entrou no if')

# ---------------------------------------Exemplo de or------------------------------------------------------------------

if a > b or a > c:
    print('Entrou no if')
else:
    print('Não entrou no if')

#----------------------------------------Exemplo de not-------------------------------------------------------------------
a = 2
b = 2

if not a == b:
    print('Deu certo')