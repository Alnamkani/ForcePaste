import pyperclip
import pyautogui
import time
########
# This program accesses the clipboard
# and write whatever text in there in the 
# current location of the writing cursor.
#######
pyautogui.hotkey('alt', 'tab') #When this script is run it's in it's own window (we don't see it because .pyw), 
#and we want to write in the window we are looking at. So, this line gets us there 
time.sleep(0.1) # for some programs the previous command happens Too fast, we need to slow it down. 
#this command wait 0.1 second before doing the next one.
pyautogui.typewrite(pyperclip.paste()) #This line simply gets the text and writes it.

