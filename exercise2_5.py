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
targetKeys = [respFirst, respLast, quitKey]
corrResp = visual.TextStim(win, text = "O", height = 40, color = "green", pos = [0, 0])
incorrResp = visual.TextStim(win, text = "X", height = 40, color = "red", pos = [0, 0])
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
    win.flip()
    nameStim.draw()
    win.flip()
    event.clearEvents('keyboard')
    output = event.waitKeys(keyList = targetKeys)
    win.flip()
    core.wait(.15)
    if (targetKey in output):
        corrResp.draw()
        win.flip()
        core.wait(.5)
    elif (quitKey in output):
        break
    else:
        incorrResp.draw()
        win.flip()
        core.wait(.5)