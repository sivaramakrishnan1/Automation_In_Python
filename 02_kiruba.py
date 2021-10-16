import pyautogui as p, time as t

p.press('win')
t.sleep(1)
p.write('whatsapp')
t.sleep(1)
p.press('enter') 

t.sleep(20)
p.hotkey('ctrl','f')
p.write('kamalesh')
t.sleep(2)
p.press('enter')

t.sleep(5)
msg=["1", "2", "3", "4", "kiruba kiruba kirubaaaa", "kiruba kiruba kirubaaaaaaa"]

for i in msg:
    p.write(i)
    p.press('enter')
    t.sleep(1)
