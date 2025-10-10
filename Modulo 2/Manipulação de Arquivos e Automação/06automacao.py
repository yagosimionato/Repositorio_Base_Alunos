import pyautogui
import webbrowser
import time

# passo 1 : abri o youtube com uma musica especifica
url = 'https://www.youtube.com/watch?v=KQoZMAuFhww&list=RDKQoZMAuFhww&start_radio=1'
webbrowser.open(url)

# passo 2: aguardar o carregando da pagina 
time.sleep(5) # ajustar de acordo com a velocidade da internet utilizada

# passo 3: garantir que o video comece ( aperte o espaco para "play")
pyautogui.press('space') # toca ou pausa o video