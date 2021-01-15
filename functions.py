import time
import random

import numpy

import pyautogui
from pyclick import HumanClicker
from pyclick.humancurve import HumanCurve

from PIL import ImageGrab

pyautogui.FAILSAFE = False

def generateRandomNumber(start, end):
    return random.randint(start, end)

def takeScreenShot(file_name=None):    
    pil_img = ImageGrab.grab()

    if file_name is not None:
        pil_img.save(file_name)
        
def checkImageOnScreen(file_name, confidence):
    on_screen = pyautogui.locateOnScreen(file_name, confidence=confidence)
    if on_screen is None:
        return False
    else:
        return True
        # return tuple(on_screen)

def write(text, seconds):
    text = text.replace("\\n", "\n")
    interval = seconds / len(text)
    pyautogui.write(text, interval=interval)



class MouseHandler:
    def __init__(self):
        self.hc = HumanClicker()

    def move(self, start:tuple, end:tuple, seconds:float):
        self.hc.move(start, seconds)
        self.hc.move(end, seconds)

    def click(self):
        self.hc.click()
    

class RandomWait:
    def __init__(self, wait_secs, random_wait):
        self.random_wait = random_wait / 1000
        self.wait_secs = wait_secs / 1000
    
    def wait(self):
        assert self.wait_secs > self.random_wait

        time.sleep(self.wait_secs + generateRandomNumber(int(-self.random_wait), int(self.random_wait)))

if __name__ == "__main__":
    random_up_and_down = 4

    mh = MouseHandler()
    rw = RandomWait(400, 2000)

    rw.wait()

    start = (
        int(input("Enter Start X: ")) + generateRandomNumber(-random_up_and_down, random_up_and_down), 
        int(input("Enter Start Y: ")) + generateRandomNumber(-random_up_and_down, random_up_and_down))
    end = (
        int(input("Enter End X: ")) + generateRandomNumber(-random_up_and_down, random_up_and_down),
        int(input("Enter End Y: ")) + generateRandomNumber(-random_up_and_down, random_up_and_down))

    seconds = int(input("Enter Seconds: "))

    mh.move(start, end, seconds)

    write("Hello", 2)

