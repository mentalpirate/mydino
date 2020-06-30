import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    
    
    # Draw the rectangle for birds
    for i in range(300, 280):
        for j in range(250,355):
            if data[i, j] < 100:
                hit("down")
                return

    # Draw for cactus
    for i in range(200, 280):
        for j in range(370, 425):
            if data[i, j] < 100:
                hit("up")
                return
    return
if __name__ == "__main__":
    print("dino run is ready.......!!!")
    time.sleep(2)
    # hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
        print(asarray(image))
        
        """
         
        # Draw the rectangle for cactus
        for i in range(200, 280):
            for j in range(370,425):
                data[i, j] = 0
        
        # Draw the rectangle for birds
        for i in range(230, 280):
            for j in range(250, 355):
                data[i, j] = 171

        image.show()
        break
        """