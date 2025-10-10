# Crie um programa que use um comando com o Pyautogui para abrir a calculadora do Windows e faça um calculo de 8 + 2 e apresente o resultado.
# Observação: Utilizando o Win + R
# para abrir o Executar, digitar "calc"
# e pressionar Enter.

import pyautogui
import time

# Espera alguns segundos para o usuário se preparar
time.sleep(2)

# Pressiona Win + R para abrir o Executar
pyautogui.hotkey('win', 'r')
time.sleep(1)

# Digita 'calc' para abrir a calculadora
pyautogui.write('calc')
pyautogui.press('enter')

# Aguarda a calculadora abrir
time.sleep(2)

# Digita 8 + 2
pyautogui.press('8')
pyautogui.press('+')
pyautogui.press('2')
pyautogui.press('enter')
