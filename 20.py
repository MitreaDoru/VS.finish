import pyautogui, time
wh = pyautogui.size()
print(wh)
while True:
    pozitia = pyautogui.position()
    px = pozitia[0]
    py = pozitia[1]
    pyautogui.moveTo(px+1, duration=0.1)
    time.sleep(10)
    