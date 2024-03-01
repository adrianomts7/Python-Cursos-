import pyautogui

pyautogui.PAUSE = 2

# Abrir as ferramentas do sistema 
pyautogui.press("win")
pyautogui.write("Google Chrome")
pyautogui.press("enter")
pyautogui.click(x=832, y=622)
pyautogui.click(x=791, y=509)
pyautogui.write("Youtube")
pyautogui.press("enter")
pyautogui.click(x=336, y=421)





# Posição do Mouse
#import time
#time.sleep(3)
#pyautogui.position()
#Lembrando que os click´s são a posição do mouse é necéssario usar o codigo a cima para descobrir a posição do proprio