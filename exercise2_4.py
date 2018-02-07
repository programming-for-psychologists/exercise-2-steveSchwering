import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]

win = visual.Window([800,600],color="black", units='pix')
nameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
cross = visual.TextStim(win, text = "+", height = 40, color = "white", pos = [0,0])

lastNames = [name.split(' ')[1] for name in names]
lastNames = [name.strip('\n') for name in lastNames]

respFirst = 'f'
respLast = 'l'
quitKey = 'q'
while True:
    nameShown = random.choice(random.choice([firstNames, lastNames]))
    if nameShown in firstNames:
        targetKey = respFirst
    else:
        targetKey = respLast
    nameStim.setText(nameShown)
    cross.draw()
    win.flip()
    core.wait(0.50)
    nameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()
    event.clearEvents('keyboard') # Necessary?
    output = event.waitKeys(keyList = [targetKey, quitKey])
    core.wait(.15)
    if (quitKey in output):
        break