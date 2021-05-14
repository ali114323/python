import pyautogui, time

b = open("hi.txt", "r")
time.sleep(5)

for word in b:
    pyautogui.doubleClick()
