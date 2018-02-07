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
waitTime = 1

title_text = "Configure Participant" 
userInfo = {"Participant first name": "subID"}
dlg = gui.DlgFromDict(dictionary = userInfo, title = title_text)
ID = dlg.data[0].encode('ascii','ignore').strip()
while (ID not in firstNames):
    errorDlg = gui.Dlg(title = "Error: Name does not exist", pos = (200,400))
    errorDlg.show()
    dlg = gui.DlgFromDict(dictionary = userInfo, title = title_text)
    ID = dlg.data[0].encode('ascii','ignore').strip()

targetName = ID
matchKey = 'space'
targetKeys.append(matchKey)
timer = core.Clock()
def writeScore(score, file):
    for item in score:
        file.write(str(item)),
        file.write("\t"),
    file.write("\n")

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
