import pyautogui, time, pyperclip
time.sleep(10) #Timp sa activezi fereastra dorita
fw = pyautogui.getActiveWindow()
fw.center
pyautogui.click(fw.center)
pyautogui.hotkey('ctrl', 'a')
pyautogui.hotkey('ctrl', 'c')
continut = pyperclip.paste()
print(continut)

