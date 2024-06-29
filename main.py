import cv2
import pyautogui as pag
import time
import win32api, win32con
import random
import keyboard
import numpy as np

batStartX= 1643
batStartY=  607 

batEndX, batEndY = 1726, 780
elixirX, elixirY = 1725, 852  #check if elixir is >=4 xDD

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

cardlist = [1656,1724,1545,1850]
arenaXmin, arenaXmax = 1500, 1850
areaYmin, areaYmax = 510,600
Ycard = 790

while keyboard.is_pressed('q') == False:

    if pag.pixel(batStartX,batStartY) == (255,255,255):
        click(batStartX,batStartY)
        time.sleep(1)

    elif(pag.pixel(elixirX,elixirY)[0] >=220 and pag.pixel(elixirX,elixirY)[0] <= 245):
        Xcard = random.choice(cardlist)
        click(Xcard,Ycard)
        Xarena = random.randint(arenaXmin, arenaXmax)
        Yarena = random.randint(areaYmin, areaYmax)
        click(Xarena,Yarena)
        time.sleep(0.5)

    elif(pag.pixel(batEndX,batEndY)[2] == 255):
        click(batEndX,batEndY)
        time.sleep(1)

