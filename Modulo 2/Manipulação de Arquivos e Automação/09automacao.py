import pyautogui
import time

pyautogui.press('win')
time.sleep(1)
pyautogui.write("bloco de notas")
pyautogui.press("enter")
time.sleep(2)

arvore = [
    "   ^   ", # 4 intervalos para cada lado
    "  ^^^  ",
    " ^^^^^ ",
    "  |||   ",
    "  |||   ",
]

for linha in arvore:
    pyautogui.write(linha, interval=0.1)
    pyautogui.press("Enter")
print("Desenho da árvore concluido!")