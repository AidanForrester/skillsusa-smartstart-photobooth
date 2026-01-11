import board
import digitalio
import time
import cv2
import numpy as np
import subprocess

buzzer = digitalio.DigitalInOut(board.D18)
buzzer.direction = digitalio.Direction.OUTPUT

g = digitalio.DigitalInOut(board.D21)
g.direction = digitalio.Direction.OUTPUT

r = digitalio.DigitalInOut(board.D20)
r.direction = digitalio.Direction.OUTPUT

b = digitalio.DigitalInOut(board.D16)
b.direction = digitalio.Direction.OUTPUT

u_green = np.array ([85, 255, 255])
l_green = np.array([35, 40, 50])

imgframe = cv2.imread("frame.jpg")

camera = cv2.VideoCapture(0)

if True == True:
        g.value = True
        for buzz1 in range(200):
            buzzer.value = True
            time.sleep((1/320)/2)
            buzzer.value = False
            time.sleep((1/320)/2)
        r.value = True
        for buzz2 in range(200):
            buzzer.value = True
            time.sleep((1/420)/2)
            buzzer.value = False
            time.sleep((1/420)/2)
        b.value = True
        for buzz3 in range(200):
            buzzer.value = True
            time.sleep((1/520)/2)
            buzzer.value = False
            time.sleep((1/520)/2)

        ret, frame = camera.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        bg = cv2.imread("bg.jpg")
        mask = cv2.inRange(hsv, l_green, u_green)
        mask_inv = cv2.bitwise_not(mask)
        f = cv2.bitwise_and(frame, frame, mask = mask_inv)
        mask = cv2.bitwise_and(bg, bg, mask = mask)
        frame = cv2.add(f, mask)
        b.value = False
        g.value = False
        r.value = False
        roi = imgframe[40:41+562, 41:843+121]
        imgframe[41:562-41, 41:722-41] = frame
        cv2.imwrite("skills.jpg", imgframe)
#        file_path = "skills.jpg"
#        subprocess.run(["lpr", file_path], check=True)
        
