import pyautogui as pgui
import time
import pyperclip as pc
time.sleep(5)
for i in range(10):
    pc.copy('💖')
    pgui.hotkey('ctrl','v')
    time.sleep(0.1)
