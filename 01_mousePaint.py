#Python Paint drawing program
from ctypes import pythonapi
import pyautogui, time as t

# py auto GUI

# py - python
# auto - automatic
# GUI - Graphical User Interface

pyautogui.press('win')
t.sleep(1)
pyautogui.write("Paint")
t.sleep(1)
pyautogui.press('enter')

t.sleep(5)

distance = 500

while distance > 0:
        pyautogui.drag(distance, 0, duration=0)   # move right
        distance -= 5 

        pyautogui.drag(0, distance, duration=0)   # move down
        distance -= 5

        pyautogui.drag(-distance, 0, duration=0)  # move left
        distance -= 5

        pyautogui.drag(0, -distance, duration=0)  # move up
        distance -= 5
        
