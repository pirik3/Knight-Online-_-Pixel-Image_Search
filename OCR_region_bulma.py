import pyautogui as ag
import win32gui as wn
import pytesseract as pt
import tkinter as tk
from PIL import Image, ImageTk
import threading
import time

pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

root = tk.Tk()

label = tk.Label(root)
label.pack()

canvas = tk.Canvas(root, width=30, height=20)
canvas.pack()

hp_label = tk.Label(root, text="HP = 0", font=("Arial", 14))
hp_label.pack()

region_coords = [99, 65, 30, 20]  # left, top, width, height

def region_bul():
    while True:
        hwnd = wn.FindWindow(None, "FIGHTKO:PRIME(18 APRIL)")
        if hwnd:
            left, top, right, bottom = wn.GetWindowRect(hwnd)

            region_hp_current = (left + region_coords[0], top + region_coords[1], region_coords[2], region_coords[3])

            im_hp_current = ag.screenshot(region=region_hp_current)

            im_hp_current_tk = ImageTk.PhotoImage(im_hp_current)

            label.config(image=im_hp_current_tk)
            label.image = im_hp_current_tk 

            hp_text = pt.image_to_string(im_hp_current, config='--dpi 70 --psm 8 -c tessedit_char_whitelist=0123456789')

            hp_label.config(text=f"HP = {hp_text.strip()}")

        #time.sleep(0.1)

def region_guncelle():
    try:
        region_coords[0] = int(entry_left.get())  # left
        region_coords[1] = int(entry_top.get())   # top
        region_coords[2] = int(entry_width.get())  # width
        region_coords[3] = int(entry_height.get())  # height
    except ValueError:
        print("dogru degerler yazilmadi.")

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Left:").grid(row=0, column=0)
entry_left = tk.Entry(frame)
entry_left.insert(0, region_coords[0])  
entry_left.grid(row=0, column=1)

tk.Label(frame, text="Top:").grid(row=1, column=0)
entry_top = tk.Entry(frame)
entry_top.insert(0, region_coords[1])  
entry_top.grid(row=1, column=1)

tk.Label(frame, text="Width:").grid(row=2, column=0)
entry_width = tk.Entry(frame)
entry_width.insert(0, region_coords[2]) 
entry_width.grid(row=2, column=1)

tk.Label(frame, text="Height:").grid(row=3, column=0)
entry_height = tk.Entry(frame)
entry_height.insert(0, region_coords[3]) 
entry_height.grid(row=3, column=1)

btn_update = tk.Button(frame, text="guncelle", command=region_guncelle)
btn_update.grid(row=4, columnspan=2)

update_thread = threading.Thread(target=region_bul, daemon=True)
update_thread.start()

root.mainloop()
