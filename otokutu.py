import dxcam
from PIL import Image
import win32gui
import win32api, win32con
from mss import mss
import cv2
import numpy as np
from time import time
from roboflow import Roboflow
from pynput.mouse import Button, Controller
import pyautogui
from ahk import AHK

ahk = AHK()

def mouse_click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

camera = dxcam.create()  # returns a DXCamera instance on primary monitor

rf = Roboflow(api_key="BXAeSDxRcJjnXMq1SaBD")
project = rf.workspace().project("knight-online-_-kutu")
model = project.version(1).model


hwnd = win32gui.FindWindow(None, "Knight OnLine Client")
win32gui.ShowWindow(hwnd,5)
#win32gui.SetForegroundWindow(hwnd)

#left, top, right, bottom = rect
sct = mss()
mouse = Controller()

    
while 1:
    rect = win32gui.GetWindowRect(hwnd)
    #begin_time = time()
    sct_img = sct.grab(rect)
    img = Image.frombytes('RGB', (sct_img.size.width, sct_img.size.height), sct_img.rgb)
    img_bgr = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    cv2.imwrite("test.jpg", img_bgr)
    #cv2.imshow('pirik3', np.array(img_bgr))
    print(model.predict("test.jpg", confidence=40, overlap=30).json())
    data = prediction = model.predict("test.jpg", confidence=40, overlap=30).json()# or
    #null = data['predictions'][None][[]]
    #print(null)
    global x1, y1
    try:    
        x1 = data['predictions'][0]['x']
        y1 = data['predictions'][0]['y']
        ahk.mouse_move(x=x1,y=y1)
        ahk.click()
    except:
        pass
    #intx1 = int(x1) # def mouse_click api icin float degerini calistirmiyor
    #inty1 = int(y1) # same
    #print(x1)
    #print(y1)
    # Set pointer position
    #mouse.position = (x1, y1)
    #pyautogui.moveTo(x1,y1)
    #pyautogui.click(x=x1, y=y1)
    #mouse.click(Button.left, 1)
    #mouse_click(intx1, inty1)
    
    #ahk.key_down('1')
    #ahk.key_up('1')
    #ahk.key_press('2')
    #print(data)
    #click(x,y)
    #print (x1,y1)
    #print('This frame takes {} seconds.'.format(time()-begin_time))
    #if cv2.waitKey(25) & 0xFF == ord('q'):
        #cv2.destroyAllWindows()
        #break


# ... Do Something
#camera.stop()
#camera.is_capturing  # False

#while True:
    #frame = camera.grab(region=rect)
    #Image.fromarray(frame).show()
    #camera.start(region=(0, 0, 1600, 900))  # Optional argument to capture a region
    #camera.is_capturing  # True
    #image = camera.get_latest_frame()
    #Image.fromarray(image).show()