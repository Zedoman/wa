import pyautogui as pg
#while True:
#       print(pg.position()) #wil show the coordinate of the txtbox
import time
c=1
while c<=5:
    pg.click(477,692) #to locate the txtbox
    time.sleep(0.1)
    pg.write("HI")
    time.sleep(0.1)
    pg.press("enter")
    time.sleep(0.1)
    c+=1