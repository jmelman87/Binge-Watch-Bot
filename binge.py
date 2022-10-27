import time
import pyautogui


# THIS SCRIPT RUNS A SIMPLE LOOP THAT WILL MOVE THE MOUSE SLIGHTLY ON THE SCREEN EVERY 1 HOUR
# WILL PREVENT NETFLIX, HULU, DISNEY+ AND ALL STREAMING SERVICES FROM HAVING A TIMEOUT AFTER INACTIVITY FOR X TIME

# REMEMBER: The upper left corner of the computer screen is (0,0)

time.sleep(2)
print("Binge Watch Bot is now active")

while True:
    pyautogui.moveTo(500, 350) # moves mouse to somewhere in the middle of the screen (ok if not exactly in center - bot will work)

    time.sleep(3600) #sleep for 1 hour

    pyautogui.move(200, 100) #moves mouse right 200px, down 100px
    time.sleep(0.5)
    pyautogui.move(-200, -100) #moves mouse backwards - left 200px, up 100px
    

