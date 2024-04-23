nome = input('Digite seu Nome: ')
idade = int(input('Digite sua idade: ')) 
formAcad = input('Você tem Formação Acadêmica: ').lower()
expe = float(input('Quanto tempo você tem de experiência: '))

if idade >= 18 and formAcad == 'sim' and expe >= 2:
    print('Seu Currículo foi aprovado para a próxima etapa !')
else:
    print('Seu Currílo não atende os requistos porém enviaremos para nosso Banco de Talento !')