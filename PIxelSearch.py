import pyautogui as ag
import win32gui as wn


while True:
    hwnd = wn.FindWindow(None, "Task Manager")
    xy = left, top, right, bottom = wn.GetWindowRect(hwnd)

    if not hwnd:
        print("not found")
    else:
        print("found")
        print(xy)
