import pyautogui as gui
import random
import pytesseract
from PIL import Image

import time




def main():
  #readSceen()
  for i in range(100):
    movMouse(350,(244+60*random.randint(0,8)))
  #autoClicker()
  useKeyboard()

def readSceen():
  x,y,heith,width = 302,244+60*0,250,55
  screenshot = gui.screenshot(region=(x,y,heith,width))
  screenshot.save("region.jpg")


def movMouse(x,y):
  print(gui.position())
  gui.moveTo(x,y)
  #gui.moveTo(250,750,3)
  print(gui.position())
  gui.click()
  gui.moveTo(850,700)
  gui.click()

def useKeyboard():
  #print(gui.KEYBOARD_KEYS)
  text = "Prueba nuemero 4 del bot que esta hecho a medias"
  gui.typewrite(text)
  


def autoClicker():
  condition = True
  pos = (807,393)
  gui.moveTo(pos)
  while(condition):
    #print(gui.position())
    gui.tripleClick()
    gui.tripleClick()
    gui.tripleClick()
    if gui.position() != pos:
      condition = False



# HACER CLICK
#while(True):
#  pyautogui.doubleClick()
  


if __name__ == "__main__":
  main()