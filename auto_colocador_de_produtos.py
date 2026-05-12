import pyautogui
from time import sleep

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "contateste16082012@gmail.com"
senha = "senhafoda1234"

pyautogui.press("win")
pyautogui.write("navegador opera gx")
sleep(1.5)
pyautogui.press("enter")
sleep(3)

pyautogui.hotkey("ctrl", "t")
pyautogui.write(link)
pyautogui.press("enter")
sleep(3)
pyautogui.click(x=465, y=369)
pyautogui.write(email)
pyautogui.click(x=224, y=460)
pyautogui.write(senha)
pyautogui.click(x=493, y=527)
sleep(1.5)
pyautogui.click(x=381, y=255)
pyautogui.write("76980")
pyautogui.click(x=297, y=351)
pyautogui.write("ML")
pyautogui.click(x=323, y=444)
pyautogui.write("Material_De_contrucao")
pyautogui.click(x=390, y=536)
pyautogui.write("Makita")
pyautogui.scroll(-300)
pyautogui.click(x=250, y=398)
pyautogui.write("R$ 169,99")
pyautogui.click(x=263, y=494)
pyautogui.write("R$ 237,49")
pyautogui.click(x=273, y=590)
pyautogui.write("Makita braba")
pyautogui.click(x=426, y=645)
pyautogui.scroll(-400)
