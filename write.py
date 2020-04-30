import pyautogui as pgui
import time
import pyperclip as pc
run = 2
duration = 0.08
try:
        f = open("info.txt","r",encoding="utf-8")
except FileNotFoundError:
        print("please place info.txt in ./")
        exit(1)
print("Wait 5 sec to start...")
time.sleep(5)
infoList = f.readlines()
for i in range(run):
        for line in infoList:
                line = line[:-1]
                pc.copy(line)
                pgui.hotkey('ctrl','v')
                pgui.press('enter')
                time.sleep(duration)
print("End script...")
f.close()
