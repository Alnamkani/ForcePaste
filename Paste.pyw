import pyperclip
import pyautogui
import time

pyautogui.hotkey('alt', 'tab')
time.sleep(0.1)
pyautogui.typewrite(pyperclip.paste())

