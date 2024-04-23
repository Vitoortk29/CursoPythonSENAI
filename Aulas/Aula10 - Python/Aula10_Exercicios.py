import pyautogui
import pandas as pd
import keyboard

pyautogui.PAUSE = 0.7
pyautogui.press('Win')
keyboard.write('Chrome')
pyautogui.press('Enter')
pyautogui.write('https://cadastro-produtos-devaprender.netlify.app/index.html')
pyautogui.press('Enter')

tabela = pd.read_excel('produtos_ficticios.xlsx')

for linha in tabela.index:
    
    pyautogui.click(922,341)

    keyboard.write(str(tabela.loc[linha, 'Nome do produto']))
    pyautogui.press('Tab')
    
    keyboard.write(str(tabela.loc[linha, 'Descrição']))
    pyautogui.press('Tab')
    
    keyboard.write(str(tabela.loc[linha, 'Categoria']))
    pyautogui.press('Tab')
    
    keyboard.write(str(tabela.loc[linha, 'Código do produto']))
    pyautogui.press('Tab')
    
    keyboard.write(str(tabela.loc[linha, 'Peso (em kg)']))
    pyautogui.press('Tab')
    
    keyboard.write(str(tabela.loc[linha, 'Dimensões (L x A x P)']))
    pyautogui.press('Tab')

    pyautogui.press('Enter')
    pyautogui.press('Tab')
    
    keyboard.write(str(tabela.loc[linha, 'Preço']))
    pyautogui.press('Tab')
    
    keyboard.write(str(tabela.loc[linha, 'Quantidade em estoque']))
    pyautogui.press('Tab')
    
    keyboard.write(str(tabela.loc[linha, 'Data de validade']))
    pyautogui.press('Tab')
    
    keyboard.write(str(tabela.loc[linha, 'Cor']))
    pyautogui.press('Tab')
    
    keyboard.write(str(tabela.loc[linha, 'Tamanho']))
    pyautogui.press('Tab')
    
    keyboard.write(str(tabela.loc[linha, 'Material']))
    pyautogui.press('Tab')

    pyautogui.press('Enter')
    pyautogui.press('Tab')
        
    keyboard.write(str(tabela.loc[linha, 'Fabricante']))
    pyautogui.press('Tab')
    
    keyboard.write(str(tabela.loc[linha, 'País de origem']))
    pyautogui.press('Tab')
    
    keyboard.write(str(tabela.loc[linha, 'Observações']))
    pyautogui.press('Tab')
    
    keyboard.write(str(tabela.loc[linha, 'Código de barras']))
    pyautogui.press('Tab')
    
    keyboard.write(str(tabela.loc[linha, 'Localização no armazém']))
    pyautogui.press('Tab')

    pyautogui.press('Enter')
    pyautogui.press('Enter')
    pyautogui.press('Tab')
    pyautogui.press('Enter')