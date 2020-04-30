import pyautogui as pgui
import time
import pyperclip as pc
run = 2
duration = 0.05
try:
    f = open("info.txt","r",encoding="utf-8")
except FileNotFoundError:
    print("please place info.txt in ./")
    exit(1)
try:
	run = int(input("Enter run times, default is 2:"))
except:
	print("Expect int but get other type.\nrun times is set to 2")
	run = 2
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
