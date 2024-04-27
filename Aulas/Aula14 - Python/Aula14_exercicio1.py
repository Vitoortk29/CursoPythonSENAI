import datetime 
import pandas as pd
from PIL import Image, ImageFont, ImageDraw

tabela = pd.read_excel('formandos.xlsx')

fonteNome = ImageFont.truetype('tahomabd.ttf', size=70)
fonteGeral = ImageFont.truetype('tahoma.ttf', size=35)
fonteData = ImageFont.truetype('tahoma.ttf', size=27)
imagem = Image.open('diploma_senai.jpg')
desenhar = ImageDraw.Draw(imagem)

for linha in tabela.index:
    nomeDoCaboclo = tabela.loc[linha, 'Nome do Caboco']
    rg = tabela.loc[linha, 'RG']
    cpf = tabela.loc[linha, 'CPF']
    atividade = tabela.loc[linha, 'Nome da Atividade']
    dataInicio  = tabela.loc[linha, 'Data Início']
    dataEmissao = datetime.datetime.today()
    data_formatada = dataEmissao.strftime("%d/%m/%Y")

    desenhar.text((300, 240), nomeDoCaboclo, fill='Black', font=fonteNome)
    desenhar.text((350, 360), rg, fill='Black', font=fonteGeral)
    desenhar.text((680, 360), cpf, fill='Black', font=fonteGeral)
    desenhar.text((380, 400), atividade, fill='Black', font=fonteGeral)
    desenhar.text((90, 555), dataInicio, fill='Black', font=fonteData)
    desenhar.text((90, 640), data_formatada, fill='Black', font=fonteData)

    imagem.save(f'{linha} {nomeDoCaboclo} - Certificado.png')