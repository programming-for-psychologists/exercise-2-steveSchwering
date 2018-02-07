import time
import sys
import random
from psychopy import visual,event,core,gui


names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]

"""
the two line above are a more compact way of writing: 
names = open('names.txt', 'r').readlines()
firstNames=[]
for name in names:
    firstNames.append(name.split(' ')[0])
"""	

win = visual.Window([800,600],color="black", units='pix')
partVis = visual.TextStim(win, text = "", height = 40, color = "white", pos = [0, 200])
partVis.setAutoDraw(True)
nameStim = visual.TextStim(win,text="", height=40, color="white",pos=[0,0])
cross = visual.TextStim(win, text = "+", height = 40, color = "white", pos = [0,0])

### Part 1
partVis.text = "Part 1"
while True:
    nameShown = random.choice(firstNames)
    nameStim.setText(nameShown)
    cross.draw()
    win.flip()
    core.wait(0.50)
    nameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()
    core.wait(.15)
    if event.getKeys(['q']):
        break

### Part 2
partVis.text = "Part 2"
lastNames = [name.split(' ')[1] for name in names]
lastNames = [name.strip('\n') for name in lastNames]
while True:
    nameShown = random.choice(lastNames)
    nameStim.setText(nameShown)
    cross.draw()
    win.flip()
    core.wait(0.50)
    nameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()
    core.wait(.15)
    if event.getKeys(['q']):
        break

partVis.text = "Part 3"
while True:
    nameShown = random.choice(random.choice([firstNames, lastNames]))
    nameStim.setText(nameShown)
    cross.draw()
    win.flip()
    core.wait(0.50)
    nameStim.draw()
    win.flip()
    core.wait(.75)
    win.flip()
    core.wait(.15)
    if event.getKeys(['q']):
        break

partVis.text = "Part 4"
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

partVis.text = "Part 5"
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

partVis.text = "Part 6"
waitTime = 1
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
    output = event.waitKeys(maxWait = 1, keyList = targetKeys)
    win.flip()
    core.wait(.15)
    if (output == None): # Messy
        incorrResp.draw()
        win.flip()
        core.wait(0.5)
    elif (targetKey in output):
        corrResp.draw()
        win.flip()
        core.wait(.5)
    elif (quitKey in output):
        break
    else:
        incorrResp.draw()
        win.flip()
        core.wait(.5)

partVis.text = "Part 7"
title_text = "Configure Participant" 
userInfo = {"Participant first name": "subID"}
dlg = gui.DlgFromDict(dictionary = userInfo, title = title_text)
ID = dlg.data[0].encode('ascii','ignore').strip()
while (ID not in firstNames):
    errorDlg = gui.Dlg(title = "Error: Name does not exist", pos = (200,400))
    errorDlg.show()
    dlg = gui.DlgFromDict(dictionary = userInfo, title = title_text)
    ID = dlg.data[0].encode('ascii','ignore').strip()

partVis.text = "Part 8"
targetName = ID
matchKey = 'space'
targetKeys.append(matchKey)
print(targetKeys)
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
    output = event.waitKeys(maxWait = 1, keyList = targetKeys)
    win.flip()
    core.wait(.15)
    if (output == None):
        incorrResp.draw()
    elif (quitKey in output):
        break
    elif (nameShown == targetName):
        if (matchKey in output):
            corrResp.draw()
        else:
            incorrResp.draw()
    elif (targetKey in output):
        corrResp.draw()
    else:
        incorrResp.draw()
    win.flip()
    core.wait(0.5)

partVis.text = "Part 9"
timer = core.Clock()
while True:
    score = []
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
    timer.reset() # Or may immediately after the flip
    win.flip()
    event.clearEvents('keyboard')
    output = event.waitKeys(maxWait = 1, keyList = targetKeys)
    time = timer.getTime()
    print(time)
    win.flip()
    core.wait(.15)
    if (output == None):
        incorrResp.draw()
    elif (quitKey in output):
        break
    elif (nameShown == targetName):
        if (matchKey in output):
            corrResp.draw()
        else:
            incorrResp.draw()
    elif (targetKey in output):
        corrResp.draw()
    else:
        incorrResp.draw()
    win.flip()
    core.wait(0.5)


partVis.text = "Part 10"
def writeScore(score, file):
    for item in score:
        file.write(str(item)),
        file.write("\t"),
    file.write("\n")

timer = core.Clock()
filename = "outputFile.txt"
outFile = open(filename, "w")
while True:
    score = [None, None, None]
    nameShown = random.choice(random.choice([firstNames, lastNames]))
    if nameShown in firstNames:
        targetKey = respFirst
    else:
        targetKey = respLast
    nameStim.setText(nameShown)
    score[0] = nameShown # I also added the name shown, could also add first/last
    cross.draw()
    win.flip()
    core.wait(0.50)
    win.flip()
    nameStim.draw()
    timer.reset()
    win.flip()
    event.clearEvents('keyboard')
    output = event.waitKeys(maxWait = 1, keyList = targetKeys)
    RT = timer.getTime()
    win.flip()
    core.wait(.15)
    if (output == None):
        incorrResp.draw()
        score[1] = 0
    elif (quitKey in output):
        break
    elif (nameShown == targetName):
        if (matchKey in output):
            corrResp.draw()
            score[1] = 1
        else:
            incorrResp.draw()
            score[1] = 0
    elif (targetKey in output):
        corrResp.draw()
        score[1] = 1
    else:
        incorrResp.draw()
        score[1] = 0
    score[2] = RT*1000
    writeScore(score, outFile)
    win.flip()
    core.wait(0.5)
outFile.close()

partVis.text = "Part 11"
### Interested in measuring the effect of staggered case on recognition
timer = core.Clock()
filename = "outputFile.txt"
outFile = open(filename, "w")
while True:
    score = [None, None, None, None]
    score[0] = random.choice(random.choice([firstNames, lastNames]))
    score[1] = random.choice([0, 1])
    text = list(score[0])
    if score[1] == 1:
        for i in range(0, len(text), 2):
            text[i] = text[i].upper()
    text = ''.join(text)
    if score[0] in firstNames:
        targetKey = respFirst
    else:
        targetKey = respLast
    nameStim.setText(text)
    cross.draw()
    win.flip()
    core.wait(0.50)
    win.flip()
    nameStim.draw()
    timer.reset()
    win.flip()
    event.clearEvents('keyboard')
    output = event.waitKeys(maxWait = 1, keyList = targetKeys)
    RT = timer.getTime()
    win.flip()
    core.wait(.15)
    if (output == None):
        incorrResp.draw()
        score[2] = 0
    elif (quitKey in output):
        break
    elif (score[0] == targetName):
        if (matchKey in output):
            corrResp.draw()
            score[2] = 1
        else:
            incorrResp.draw()
            score[2] = 0
    elif (targetKey in output):
        corrResp.draw()
        score[2] = 1
    else:
        incorrResp.draw()
        score[2] = 0
    score[3] = RT*1000
    writeScore(score, outFile)
    win.flip()
    core.wait(0.5)
outFile.close()

sys.exit()
