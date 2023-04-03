
import time

# time.sleep(2)
# import pyautogui
# # the game may bot take this format so using other format to output rspaonse
# print("down")
# pyautogui.keyDown("w")
# pyautogui.keyDown("w")

# time.sleep(2)
# print("up")
# pyautogui.keyDown("space")
# pyautogui.keyDown("sapce")



# NEW METHOD OF SENDING 
from keyboard_contoller import PressKey ,ReleaseKey,w,a,s,d
time.sleep(2)
while 1:
    PressKey(w)
    time.sleep(1)
    ReleaseKey(w)
    PressKey(a)
    
    time.sleep(1)
    ReleaseKey(a)
    PressKey(d)
    
    time.sleep(1)
    ReleaseKey(d)



    




    