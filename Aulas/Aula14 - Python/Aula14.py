import pandas as pd
from PIL import Image, ImageFont, ImageDraw

tabela = pd.read_excel('planilha_alunos.xlsx')

# print(tabela)          #Este print serve apenas para verificar se o codigo a cima chamou mesmo a planilha

fonteNome = ImageFont.truetype('tahomabd.ttf', size=90)
fonteGeral = ImageFont.truetype('tahoma.ttf', size=80)
fonteData = ImageFont.truetype('tahoma.ttf', size=55)
imagem = Image.open('certificado_padrao.jpg')
desenhar = ImageDraw.Draw(imagem)

for linha in tabela.index:
    nomeParticipante = tabela.loc[linha, 'Nome Participante']
    curso = tabela.loc[linha, 'Nome do Curso']
    participacao = tabela.loc[linha, 'Tipo de Participação']
    cargaHoraria = str(tabela.loc[linha, 'Carga Horária (horas)'])
    dataInicio = tabela.loc[linha, 'Data de Início']
    dataTermino = tabela.loc[linha, 'Data de Término']
    dataEmissao = tabela.loc[linha, 'Data de Emissão do Certificado']
    
    desenhar.text((1050, 810), nomeParticipante, fill='black', font=fonteNome)
    desenhar.text((1050, 950), curso, fill='black', font=fonteGeral)
    desenhar.text((1450, 1060), participacao, fill='black', font=fonteGeral)
    desenhar.text((1480, 1190), cargaHoraria, fill='black', font=fonteGeral)
    desenhar.text((750, 1780), dataInicio, fill='black', font=fonteData)
    desenhar.text((750, 1930), dataTermino, fill='black', font=fonteData)
    desenhar.text((2220, 1930), dataEmissao, fill='black', font=fonteData)

    imagem.save(f'{linha} {nomeParticipante} - Certificado.png')