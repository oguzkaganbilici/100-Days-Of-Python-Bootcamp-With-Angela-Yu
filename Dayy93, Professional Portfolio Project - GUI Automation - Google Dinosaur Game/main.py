import time

import pyautogui
import pyautogui as pyo
from PIL import ImageGrab, ImageOps
import numpy as np

replay_pos = (946, 384)
dinosaur_pos = (690, 413)


def start_game():
    pyautogui.press("up")

def click_restart():
    pyo.click(replay_pos)
    pyo.keyDown("down")

def press_space():
    pyo.keyUp("down")
    pyo.keyDown("space")

    time.sleep(0.15)

    pyo.keyUp("space")
    pyo.keyDown("down")


def image_grab():
    detect_box = (dinosaur_pos[0] + 30, dinosaur_pos[1], dinosaur_pos[0]+120, dinosaur_pos[1] + 2)
    box_img = ImageGrab.grab(detect_box)
    box_img_gray = ImageOps.grayscale(box_img)
    a = np.array(box_img_gray.getcolors())

    print(a.sum( ))
    return a.sum()


click_restart()
while 1:
    if (image_grab() != 435):
        press_space()
        time.sleep(0.1)





