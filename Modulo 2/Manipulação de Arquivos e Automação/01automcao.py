# 1) passo: instalat o pyautogui com o comando:
# pip install pyautogui

# crie uma automaçao que abra automaticamente um navegador 

# importamos a biblioteca para script em uso
import pyautogui

# 'press' é um comando que utilizamos
# para pressionar a tecla desejada
pyautogui.press('win') # para pressionar a tecla windows

# 'sleep' é um comando que utilizamos para deixar o codigo
# em espera por alguns segundos
pyautogui.sleep(1)

# 'write' é um comando que utilizamos para passar o que queremos
# escrever
pyautogui.write('google chrome')

pyautogui.press('enter')
