import pyautogui as p, time as t

contact=list(map(str, input("Enter a contact name: ").split(",")))

msg= "hi" #The message

t.sleep(5)
xloc=p.locateOnScreen('search.png')
locx, locy = p.center(xloc)

for i in contact:
    p.click(locx , locy)
    t.sleep(4)
    p.write(i)
    t.sleep(4)
    p.press('enter')
    t.sleep(4)
    p.write(msg)
    p.write(i) #Typing the message 
    t.sleep(4)
    p.press('enter')
    t.sleep(4)
