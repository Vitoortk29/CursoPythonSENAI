# Dar um pip install em Pandas , Openpyxl , pyautogui
#Openpyxl é um complemento para o Pandas

import pyautogui
import pandas as pd

pyautogui.press('Win')
pyautogui.write('Chrome')
pyautogui.sleep(1)
pyautogui.press('Enter')
pyautogui.sleep(1)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('Enter')
pyautogui.sleep(1)
pyautogui.press('Tab')
pyautogui.press('Enter')
pyautogui.write('SenaiDaMassa')
pyautogui.press('Tab')
pyautogui.write('Senai123')
pyautogui.press('Tab')
pyautogui.press('Enter')
pyautogui.sleep(1)


tabela = pd.read_csv('produtos.csv')
# print(tabela)

for linha in tabela.index:
    
    pyautogui.click(837,274)
    
    pyautogui.write(tabela.loc[linha, 'codigo'])
    pyautogui.press('Tab')

    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press('Tab')

    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press('Tab')

    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('Tab')

    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('Tab')

    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('Tab')

    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):               # Este comando diz se a variavel obs não for vazia execute o comando abaixo do if e se for vazia pule o if 
        pyautogui.write(obs)

    pyautogui.press('Tab')

    pyautogui.press('Enter')
    pyautogui.press('Enter')
    pyautogui.scroll(5000)