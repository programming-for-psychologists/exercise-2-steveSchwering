import time
import sys
import random
from psychopy import visual,event,core,gui

names = open('names.txt', 'r').readlines()
firstNames = [name.split(' ')[0] for name in names]

title_text = "Configure Participant" 
userInfo = {"Participant first name": "subID"}
dlg = gui.DlgFromDict(dictionary = userInfo, title = title_text)
ID = dlg.data[0].encode('ascii','ignore').strip()
while (ID not in firstNames):
    errorDlg = gui.Dlg(title = "Error: Name does not exist", pos = (200,400))
    errorDlg.show()
    dlg = gui.DlgFromDict(dictionary = userInfo, title = title_text)
    ID = dlg.data[0].encode('ascii','ignore').strip()