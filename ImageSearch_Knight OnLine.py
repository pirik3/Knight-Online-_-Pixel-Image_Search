from PIL.ImageOps import grayscale
import pyautogui as ag
import win32gui as wn
import pytesseract as pt
from PIL import Image


while True:

    pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


    hwnd = wn.FindWindow(None, "Knight OnLine Client")  # pencere ismi
    xy = left, top, right, bottom = wn.GetWindowRect(hwnd)

    example1 = ag.locateCenterOnScreen('C:/Users/pirik3/Pictures/Forst_bite.png', region = xy, confidence=0.9)
    #asd2 = ag.locateOnWindow('C:/Users/pirik3/Pictures/8.png', "Untitled - Notepad")

    im_hp = ag.screenshot(region=(left+29, top+60, right*0+192, bottom*0+15)) # burasi weight ve hight olarak alinacak, point(dimension) olarak degil.
    im_hp.save("C:/Users/pirik3/Pictures/hp.png") # saves the screenshot in a file

    im_mp = ag.screenshot(region=(left+29, top+77, right*0+192, bottom*0+14))
    im_mp.save("C:/Users/pirik3/Pictures/mp.png") # saves the screenshot in a file

    
    if not hwnd:
        print("window not found")
    else:
        if example1 == None:
            ag.sleep(0.1)
            print(xy)
            print("not found")
        else:
            #ag.sleep(0.01)
            #print(xy)
            #print(example1, "found")
            #print(asd2, "asd2")
            print("HP = ", pt.image_to_string(im_hp))
            print("MP = ", pt.image_to_string(im_mp))

            #example1x, example1y = example1
            #ag.mouseDown(example1)
            #ag.sleep(0.01)
            #ag.mouseUp()
            #ag.sleep(2)
